import subprocess, time, pyautogui, pygetwindow as gw
from helpers import config


def run(url, size=(1920, 1080), position=(0, 0), kiosk=False):
    path = config.read('MAIN', 'uc_path')

    args = ["start", f"{path}", "--app=" + url]

    if (kiosk == True):
        args.append("--kiosk")

    process = subprocess.run(args, shell=True)
    time.sleep(2)
    window = pyautogui.getActiveWindow()
    window.size = size
    window.moveTo(position[0], position[1])
    time.sleep(4)

    return process


def close():
    gw.getActiveWindow().close()


def closeAllDkWindows():
    windows = gw.getAllWindows()
    for window in windows:
        if "Dragon Knight" in window.title:
            window.close()
    time.sleep(2)