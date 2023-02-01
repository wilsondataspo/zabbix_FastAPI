from fastapi import FastAPI
from configparser import ConfigParser
from zabbix_api import ZabbixAPI


config = ConfigParser()
config.read('.config.ini')
zapi = ZabbixAPI(config['zabbix']['ZABBIX_URL'], timeout=300)
zapi.auth = config['zabbix']['ZABBIX_AUTH']


# Nome da instancia
app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World."}
    
  
@app.get("/hosts_all")
async def hosts_all():
    """
    
    """
    response = zapi.host.get({
        #"output":["name","host"],
        "output":"extend",
        "sortfield":"name",
        "monitored_hosts":True,
        #"groupids":14
    })
    
    if response:
        return response