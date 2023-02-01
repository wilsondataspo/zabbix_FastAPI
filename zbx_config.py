from os import environ
from environs import Env
from zabbix_api import ZabbixAPI

BASE_DIR = environ["PWD"] + "/"

Env.read_env("{}.env".format(BASE_DIR), recurse=False)

class ZBX_Config:
	URL = environ["ZABBIX_URL"]
	USR = environ["ZABBIX_USR"]
	PAS = environ["ZABBIX_PAS"]
	AUT = environ["ZABBIX_AUTH"]
    
    
zapi = ZabbixAPI(ZBX_Config.URL, timeout=300)
zapi.auth = ZBX_Config.AUT







