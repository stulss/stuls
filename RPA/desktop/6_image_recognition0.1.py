from PIL.ImageOps import grayscale
import pyautogui
from pyscreeze import locateOnScreen
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

# checkbox = pyautogui.locateOnScreen("checkbox.png") # 화면 전체에서 찾다가 찾으면 체크후 수행 종료
# pyautogui.click(checkbox)


# 속도개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)


# 2. 범위지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881-1488, 137))
# pyautogui.moveTo(trash_icon)


# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90%의 정확도
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속기다리는 경우
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad in None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# pyautogui.click(file_menu_notepad)

# 2. 일정시간동안 기다리기
import time
import sys
timeout = 10 # 10대기
# start = time.time() # 시작시간설정
file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()





def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target
    

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s Target not found ({img_file}). Terminate program")
        sys.exit()

# pyautogui.click(file_menu_notepad)

my_click("file_menu_notepad.png", 1)