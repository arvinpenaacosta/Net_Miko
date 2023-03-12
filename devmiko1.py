from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

user='admin'
password = 'C1sco12345'

def send_show_command(device, commands):
    result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            for command in commands:
                output = ssh.send_command(command)
                result[command] = output
        return result
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)



device = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": user,
    "password": password,
}
result = send_show_command(device, ["sh ip int br"])
pprint(result, width=120)
