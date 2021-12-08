from easysnmp import Session
import math
import time
import matplotlib.pyplot as plt
import json
from netmiko import ConnectHandler
import re


session_router2_rw = Session(hostname='172.16.1.2', community='lab123', version=2)



def connect_to_device(router_ip, username, password):
    device = {
        "device_type": "cisco_ios",
        "ip": router_ip,
        "username": username,
        "password": password
    }
    conn = ConnectHandler(**device)
    return conn


def fetch_params(value1,value2,value3):
    session = session_router2_rw
    print(value1 +":" +value2+":"+value3)
    value_map = {"Name": "ifName.1", "Description": "ifDescr.1", "Status": "ifOperStatus.1"}

    name = session_router2_rw.get(value_map["Name"]).value
    description = session_router2_rw.get(value_map["Description"]).value
    operate_status = session_router2_rw.get(value_map["Status"]).value

    print(name + ":" + description +":"+ operate_status)
    return "Success"


def get_info_by_snmp():

    r2_connection = connect_to_device("172.16.1.2", "netman", "lab123")
    fetch_params("Name","Description","Status")

get_info_by_snmp()