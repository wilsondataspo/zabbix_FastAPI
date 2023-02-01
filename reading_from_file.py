from configparser import ConfigParser

config = ConfigParser()
config.read('.config.ini')

URL = config['zabbix']['ZABBIX_URL']
user = config['zabbix']['ZABBIX_USR']
passwd = config['zabbix']['ZABBIX_PAS']
secretkey = config['zabbix']['ZABBIX_AUTH']

print('Zabbix configuration:')

print(f'Link: {URL}')
print(f'User: {user}')
print(f'Password: {passwd}')
print(f'SessionID: {secretkey}')

# https://zetcode.com/python/configparser/