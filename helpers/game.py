import time
import pyautogui as auto


def auth(login, password):
    overtime = 20
    while True:
        # на странице есть кнопка входа
        if auto.pixel(600, 680) == (51, 122, 183):
            auto.click(666, 580)
            auto.write(login)
            auto.click(666, 640)
            auto.write(password)
            auto.press('enter')
            time.sleep(2)
            return True
        time.sleep(2)
        overtime -= 2
        if overtime <= 0:
            return False


def load(position):
    x = position[0]
    y = position[1]
    return auto.pixel(x + 210, y + 70) == (63, 170, 200)


def removeFlaws(position):
    x = position[0]
    y = position[1]

    # закрываем "Ограниченный возврат"
    if auto.pixel(x + 790, y + 145) == (219, 167, 106):
        auto.click(x + 790, y + 145)
        auto.click(x + 444, y + 333)


def registerParty(position):
    x = position[0]
    y = position[1]
    auto.click(x + 15, y + 40)
    auto.press('H')
    auto.click(x + 600, y + 300)
    auto.click(x + 300, y + 255)
    auto.click(x + 430, y + 330)
    auto.click(x + 790, y + 70)
    auto.click(x + 800, y + 70)


def giveGifts(position):
    x = position[0]
    y = position[1]

    lock_parties_icon = auto.pixel(x + 40, y + 210)

    if lock_parties_icon == (123, 128, 142):
        auto.click(x + 150, y + 210)
    else:
        # поиск второй иконки
        second_party_icon = auto.pixel(110, 200)

        if second_party_icon == (118, 50, 128):
            auto.click(x + 100, y + 200)
        else:
            time.sleep(2)
            auto.click(x + 100, y + 200)

    auto.click(x + 500, y + 240)
    auto.click(x + 500, y + 370)
    auto.click(x + 440, y + 330)
