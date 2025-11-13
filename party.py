import pyautogui, time
from helpers import game, browser, config, accounts

print("PROJECT: DK PARTY")
print("VERSION: 1.0.1")


def loadAllWindows(positions):
    load = True
    for t in range(0, 30, 2):
        load = True
        for window, position in enumerate(positions):
            loadGame = game.load(positions[window])
            print(loadGame)
            if not loadGame:
                load = False
                break
        if not load:
            time.sleep(2)
        else:
            break
    return load


try:
    pyautogui.PAUSE = float(config.read('MAIN', 'speed_click'))
    positions = [[0, 0], [960, 0], [0, 520], [960, 520]]
    accounts = accounts.getAccounts()

    for account in accounts:
        # Авторизируемся в фулл-экране
        start_page = config.read('LINKS', 'start_page')
        browser.run(start_page + '/user/logout', kiosk=True)
        auth = game.auth(account['login'], account['password'])
        browser.close()
        time.sleep(2)

        # Сценарий в 4 окнах
        windows = 0
        for server in account['servers']:
            browser.run(server, (950, 500), positions[windows])
            windows = windows + 1

            # Запущены 4 окна
            if windows == 4:
                # При успешной загрузке игры во всех окнах - фестивалим
                if loadAllWindows(positions):
                    # Убираем побочки и броним вечерины
                    for window, position in enumerate(positions):
                        game.removeFlaws(position)

                        if (window == 0 or window == 2):
                            game.registerParty(position)

                    time.sleep(10)

                    # Выдаем подарки
                    for window, position in enumerate(positions):
                        game.giveGifts(position)

                browser.closeAllDkWindows()
                windows = 0
except Exception as e:
    print("Error: " + e)

input("Press ENTER to exit")
