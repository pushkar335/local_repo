import pytest
from utilities.readConfigParser import Config
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures('setup')
class Test_case_login:

    def test_login(self, setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        lp.EnterUsername(Config.get_username())
        lp.EnterPassword(Config.get_password())
        lp.click_login()
        assert True

