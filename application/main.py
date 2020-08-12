import datetime

import schedule
import vk
from sqlalchemy.orm import sessionmaker

from config import service_key, engine
from models import Groups, Parser

Session = sessionmaker(bind=engine)
session = Session()


def get_members(group_id, vk_api):
    members = vk_api.groups.getMembers(group_id=group_id, v=5.92)
    count = members["count"]
    return count


def parsing():
    vk_session = vk.Session(access_token=service_key)
    vk_api = vk.API(vk_session)
    groups = session.query(Groups).filter(Groups.is_active)

    for group in groups:
        now_date = datetime.datetime.now()
        all_members = get_members(group_id=group.url.split('/')[1], vk_api=vk_api)
        parser = Parser(date=now_date, group=group.id, people_count=all_members)
        session.add(parser)
        session.commit()

    return "Parsing is done"


schedule.every().day.at("16:05").do(parsing)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
