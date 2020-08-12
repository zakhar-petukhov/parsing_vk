from main import parsing


class TestParsing:
    def test_parsing(self, mocker):
        mocker.patch('main.get_members',
                     return_value=123)
        assert parsing() == "Parsing is done"


