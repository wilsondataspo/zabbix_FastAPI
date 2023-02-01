from os import environ, path
from environs import Env

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/FastAPI"
#env = Env()
Env.read_env("{}.env".format(BASE_DIR), recurse=False)

class ZBX_Config:
	URL = environ["ZABBIX_URL"]
	USR = environ["ZABBIX_USR"]
	PAS = environ["ZABBIX_PAS"]
	AUT = environ["ZABBIX_AUTH"]