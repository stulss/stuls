import pyautogui
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 작동


# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)