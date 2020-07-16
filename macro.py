import pyautogui

#내용 입력받는 창 띄우기
name = pyautogui.prompt('이름을 입력해 주세요.')
print(name)

#비밀번호 입력받는 창 띄우기
password = pyautogui.password('비밀번호를 입력해 주세요.')
print(password)

#마우스 현재 위치 얻어오기
x, y = pyautogui.position() 
print(x, y)

#마우스 위치 클릭하기
pyautogui.click(x,y)

#내용입력
pyautogui.typewrite(password, interval=0.1) #입력한 패스워드를 자동으로 타이프

#엔터키 입력
pyautogui.hotkey('\n')



