import configparser
import os

config = configparser.ConfigParser()
config.read(os.getcwd() + r'\bin\modules\client\address.ini')
ip = config.get('server', 'ip')
port = config.get('server', 'ip')