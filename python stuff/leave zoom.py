import pyautogui
import pytesseract
import time

def leave():

    leave_btn = pyautogui.locateCenterOnScreen("leave_btn.png", grayscale=True)
    print(leave_btn)
    pyautogui.moveTo(leave_btn)
    pyautogui.click()

    leave_meeting = pyautogui.locateCenterOnScreen('leave_meeting_btn.png', grayscale=True)
    pyautogui.moveTo(leave_meeting)
    pyautogui.click()

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

while True:
    time.sleep(1)
    participants=pyautogui.screenshot(imageFilename="cumster.png",region=(292, 1030, 16, 17))
    try:
        participantcount = int(pytesseract.image_to_string("cumster.png", config='--psm 6'))
        print(participantcount)
        if participantcount < 20:
            leave()

    except ValueError:
        print('bruh')

    
    
