import pyautogui

# 마우스 이동
# pyautogui.moveTo(500,500) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
# pyautogui.moveTo(500,500, duration=5) # 5초 동안 500,500 위치로 이동

# pyautogui.moveTo(100,100, duration=0.25)
# pyautogui.moveTo(200,100, duration=0.25)
# pyautogui.moveTo(300,100, duration=0.25)

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로 부터)
# pyautogui.moveTo(100,100, duration=0.25)
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100,100, duration=0.25)
# print(pyautogui.position()) # point(x, y)
# pyautogui.move(100,100, duration=0.25)
# print(pyautogui.position()) # point(x, y)

p = pyautogui.position()
print((p[0], p[1]))
print(p.x, p.y)