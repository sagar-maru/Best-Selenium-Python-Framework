import configparser
import os

def read_config():
    config = configparser.ConfigParser()
    config_path = os.path.abspath(os.path.join(os.path.join(os.path.dirname(__file__), os.pardir),'config.ini'))
    # print(config_path)
    config.read(config_path)

    return config['DEFAULT']
