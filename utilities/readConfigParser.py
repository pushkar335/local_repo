import configparser


config = configparser.RawConfigParser()
config.read("C:\\Users\\hp\\PycharmProjects\\swag_lab\\configuration\\config.ini")


class Config:

    @staticmethod
    def get_base_URL():
        loginurl = config.get("common_info", "base_url")
        return loginurl

    @staticmethod
    def get_username():
        username = config.get("common_info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common_info", "password")
        return password

    @staticmethod
    def get_title():
        title = config.get("common_info", "login_title")
        return title
