import configparser


def read(section, option = ''):
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    if (option != '') :
        return parser[section][option]
    else:
        return parser[section]