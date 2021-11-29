import pyscreenshot
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\1615444\AppData\Local\Programs\Tesseract-OCR/tesseract.exe' 
import pyautogui
import random
import time
import keyboard
nonbreak= True 
abc = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuopasdfghjklizxcvbnm'"
while 1:
    print("Press 1 when your cursor is on top left corner of the area you want to scan")
    keyboard.wait("1")
    cmx1,cmy1= pyautogui.position()
    print("Press 2 when your cursor is on top left corner of the area you want to scan")
    keyboard.wait("2")
    cmx2,cmy2= pyautogui.position()
    print("Click enter when your cursor is in the position you want for it to type, it will automatically click and start to type everything that is in the area you selected")
    keyboard.wait("enter")
    pyautogui.click() 
    print("hold s to stop")
    word = ""
    while nonbreak:
        img = pyscreenshot.grab(bbox=(cmx1,cmy1,cmx2,cmy2)) 
        text = tess.image_to_string(img) 
        if text == "":
            break
        for a in range(0,len(text)):
            if keyboard.is_pressed('q'):  
                print('STOPPING')
                nonbreak=False
                break
            
            if text[a] in abc:
                word = word + text[a]
            else:
                pyautogui.write(word)
                word = ""
                pyautogui.press('space')
    time.sleep(0.01)
