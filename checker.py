#!/usr/bin/python3

import requests
import paramiko

try:
    requests.get('http://ftp.devgrandgold.ru')
except Exception:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname='77.222.52.231', username='root', password='eeok5dhsa-61k3wJ', port='22')
        stdin, stdout, stderr = client.exec_command('reboot')
    except paramiko.ssh_exception.AuthenticationException as e:
        print(e)
    client.close()
