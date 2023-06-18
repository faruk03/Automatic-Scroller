

import pyautogui
import time
import keyboard

if pyautogui.confirm(" !! Alert !! Within 3 seconds of clicking 'OK', this program will start working. So, go to the PDF reader's window within 3 seconds of clicking 'OK'. Press and hold 'q' to completely quit the programme") == 'OK':

    while True:
        
        if keyboard.is_pressed('q'):
        
            print(keyboard.read_key(), keyboard.is_pressed('q'))
            pyautogui.alert('Program closed')
            break
        # elif keyboard.is_pressed('p'):
        #     pyautogui.alert('Program Paused')
        #     while True:
        #         if keyboard.is_pressed('s'):
        #             pyautogui.alert('Program Started')
        #             break
        #         else:
        #             while True:
        #                 pass
        else:
            time.sleep(5)
            pyautogui.scroll(-1000)
           
            
            
            #pip install -r requirements.txt
            #pyinstaller --onefile --noconsole cwh.py
            
