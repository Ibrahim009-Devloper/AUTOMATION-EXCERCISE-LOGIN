import configparser
import os


config = configparser.RawConfigParser()
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(base_dir)
config_path = os.path.join(project_root,"configration","config.ini")
config.read(config_path)


class read_popertice():
    @staticmethod
    def get_url():
        url = config.get('get website url','url')
        return url
    
    @staticmethod
    def get_email_address():
        Email = config.get("get email address","Email")
        return Email

    @staticmethod
    def get_password():
        password = config.get("get password","Password")
        return password