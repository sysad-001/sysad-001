import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def scanner():
        input("Move mouse to first position and then hit enter...")
        pos1 = pyautogui.position()

        input("Move mouse to second position and then hit enter...")
        pos2 = pyautogui.position()

        def screenshot(posa,posb):
                x=posa[0]
                y=posa[1]
                w=posb[0]-posa[0]
                l=posb[1]-posa[1]
          
                pyautogui.screenshot('test.png', region=(x,y,w,l))
                print(x,y,w,l)
        try:
                screenshot(pos1,pos2)
                print(pytesseract.image_to_string('test.png', config='--psm 6'))
        except SystemError:
                print("invalid selection!")

repeater=input("go?")
        
if 'no' in repeater:
        print('why bother asking?')
while 'no' not in repeater:
        scanner()
        repeater=input("again?: ")
