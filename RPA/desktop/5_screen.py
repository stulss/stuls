import pyautogui
from pyscreeze import pixel

# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 974,7 56,167,241 #38A7F1

pixel = pyautogui.pixel(974, 7)
print(pixel)
# print(pyautogui.pixelMatchesColor(974, 7, (56,167,241)))
print(pyautogui.pixelMatchesColor(974, 7, pixel))