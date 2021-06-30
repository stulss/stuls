import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")

# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"): # 화면 전체에서 찾다가 찾으면 체크, 반복수행
#     print(i)
#     pyautogui.click(i)

checkbox = pyautogui.locateOnScreen("checkbox.png") # 화면 전체에서 찾다가 찾으면 체크후 수행 종료
pyautogui.click(checkbox)
