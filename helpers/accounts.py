import os.path
from helpers import config


def getAccounts():
    accounts = []
    accounts_path = config.read('MAIN', 'accounts_path')
    server_path = config.read('LINKS', 'server_page')

    if not os.path.exists(accounts_path):
        raise Exception('Файл со списком аккаунтов не найден')

    with open(accounts_path) as file:
        while line := file.readline().rstrip():
            data = line.split(':')
            servers = data[2].split('.')
            server_links = []
            for server in servers:
                link = server_path.replace(':server:', server)
                server_links.append(link)

            accounts.append(
                {
                    'login': data[0],
                    'password': data[1],
                    'servers': server_links,
                }
            )
    return accounts
