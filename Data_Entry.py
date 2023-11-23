import pyautogui
import time
import pandas as pd

input_file = r"C:\Users\marte\Desktop\ANAS\ANAS\PROJECTS\QR_CODE Attendance system\members.xls"
file = pd.read_excel(input_file)
Names = list(file['Name'])
TeamID = list(file['TeamID'])
Contact = list(file['Contact'])
Modules = list(file['Modules'])

PNumber = len(Names)
for Index in range(PNumber):
    time.sleep(10)
    pyautogui.typewrite(Names[Index])
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(TeamID[Index])
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(str(Contact[Index]))
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(Modules[Index])
    pyautogui.press('enter')
    print("Enter")
    time.sleep(2)
    pyautogui.press('enter')
    print("Enter")
    time.sleep(5)
    pyautogui.typewrite("SCINN0VA5")
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.press('1')
    pyautogui.press('enter')




