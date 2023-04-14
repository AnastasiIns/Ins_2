import pytest


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get('https://www.bmw.ru/ru/index.html')
        assert self.driver.title == "BMW - официальный сайт в России"
