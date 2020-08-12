from sqlalchemy import create_engine

CONNECTION_STR = 'sqlite:///parsing_groups_dev.db'  # auto create
engine = create_engine(CONNECTION_STR, echo=True)
service_key = ''  # put yours secret key from https://vk.com/apps?act=manage
