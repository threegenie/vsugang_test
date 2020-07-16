import pyautogui
import time

#수강신청 홈페이지에 자동으로 로그인하기

confirm = pyautogui.confirm('학번 창에 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    a,b = pyautogui.position()
    

confirm = pyautogui.confirm('비번 창을 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    c,d = pyautogui.position()

confirm = pyautogui.confirm('로그인 버튼에 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    e,f = pyautogui.position()

id = pyautogui.prompt('학번을 입력해 주세요')
pw = pyautogui.password('비번을 입력해 주세요')

#학번 입력하기
pyautogui.click(a,b) 
pyautogui.typewrite(id, interval=0.1)

time.sleep(1)

#비번 입력하기
pyautogui.click(c,d)
pyautogui.typewrite(pw, interval=0.1)

#로그인 버튼 누르기
pyautogui.click(e,f)

#로그인 이후..

confirm = pyautogui.confirm('수강신청함 버튼에 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    g,h = pyautogui.position()

confirm = pyautogui.confirm('로그아웃 버튼에 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    i,j = pyautogui.position()

pyautogui.click(g,h) #수강신청함 클릭하기

confirm = pyautogui.confirm('Search버튼에 마우스를 올리고 엔터를 쳐주세요')
if confirm == 'OK':
    k,l = pyautogui.position()

pyautogui.click(k,l) #search버튼 클릭하기

num = pyautogui.prompt('잡을 강의 개수를 입력해 주세요')
num = int(num)

lecture_position = [] #강의 위치

for i in range(num):
    confirm = pyautogui.confirm('resister버튼에 마우스를 올리고 엔터를 쳐주세요')
    if confirm == 'OK':
        lecture_position.append(pyautogui.position())

while(True);
for k in range(38): #38번 실행하기
    pyautogui.click(k,l)
    for j in range(num):
        pyautogui.click(lecture_position[j], interval=0.1)
        

pyautogui.click(i,j)

pyautogui.click(a,b)
pyautogui.typewrite(id, interval = 0.1)
    
pyautogui.click(c,d)
pyautogui.typewrite(pw, interval = 0.1)

pyautogui.click(e,f)
    

    
    
                    

    



