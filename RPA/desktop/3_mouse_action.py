import pyautogui

# pyautogui.sleep(3) # 지연
# print(pyautogui.position()) # 마우스좌표확인

# pyautogui.click(1547, 549, duration=2) #좌클릭
# pyautogui.click()
# pyautogui.mouseDown() # 마우스 버튼 누른상태
# pyautogui.mouseUp() # 마우스 버튼 땐 상태

# pyautogui.doubleClick()
# pyautogui.click(clicks=10)

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(400,400)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# pyautogui.rightClick() # 우클릭
# pyautogui.middleClick() # 휠버튼클릭

# print(pyautogui.position())
# pyautogui.moveTo(1114,249)
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100 만큼, y 0 만큼 드래그
# pyautogui.drag(100, 0, duration=0.25) # 동작이 너무 빨라 동작이 안될때는 duration으로 지연을 줘 가능
# pyautogui.dragTo(1514, 349, duration=0.25)
pyautogui.scroll(-300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤