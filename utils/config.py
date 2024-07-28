import configparser
import os

config = configparser.ConfigParser()

# Ensure the config.ini file is located in the project root directory
config_path = os.path.join(os.path.dirname(__file__), '../config.ini')
print(config_path)
config.read(config_path)

# Configuration settings
BROWSER = config['default'].get('browser', 'chrome')
HEADLESS = config['default'].getboolean('headless', False)
