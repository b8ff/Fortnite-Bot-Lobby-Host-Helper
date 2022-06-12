# READ THIS!!!
# 1) This script uses colors to detect buttons and other stuff so MAKE SURE to use the default Fortnite color settings.
# 2) This script SHOULD be compatible with any screen resolution (if not edit the variable "default_size" in "Zen.calculate()" to your screen resolution).
# 3) Fortnite MUST be windowed and maximized (look at "fortnite.png").
# 4) This script might get some updates in the future depending on Fortnite updates.
# 5) This script has been tested ONLY on Windows 10 with the small taskbar setting.
#
# IMPORTANT!!!
# 1) If the script does nothing you can look at "fortnite_settings.png" which are the settings that the script has been developed on.
# 2) Look at "fortnite.mov" to see how the script should work.
#
# Thank you for using this script and have fun!

from win32api import GetSystemMetrics
import pyautogui
import keyboard
import win32api
import win32con
import ctypes
import time
import os

class Zen:
    class fix:
        def get_mouse_position():
            start_key = input("\nEnter a start key: ")
            stop_key = input("Enter a stop key: ")
            delay = input("Delay: ")
            while True:
                time.sleep(float(delay))
                if keyboard.is_pressed(start_key):
                    print(pyautogui.position())
                elif keyboard.is_pressed(stop_key):
                    exit()

        def get_mouse_position_color():
            start_key = input("\nEnter a start key: ")
            stop_key = input("Enter a stop key: ")
            delay = input("Delay: ")
            while True:
                time.sleep(float(delay))
                if keyboard.is_pressed(start_key):
                    print(pyautogui.screenshot().getpixel((pyautogui.position())))
                elif keyboard.is_pressed(stop_key):
                    exit()

    def screen():
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        return width, height
    
    def calculate():
        default_size = (1920, 1080)
        screen_size = Zen.screen()

        offset_values = (screen_size[0] - default_size[0], screen_size[1] - default_size[1])

        ready_up_pixel = (1538 + offset_values[0], 732 + offset_values[1])
        health_pixel = (157 + offset_values[0], 947 + offset_values[1])
        exit_pixel = (15 + offset_values[0], 984 + offset_values[1])
        return_to_lobby_pixel = (206 + offset_values[0], 981 + offset_values[1])
        confirm_pixel = (206 + offset_values[0], 981 + offset_values[1])

        reset_pixel = (round(screen_size[0] / 2), round(screen_size[1] / 2))

        ready_up_pixel_fix = (944 + offset_values[0], 1011 + offset_values[1])

        return ready_up_pixel, health_pixel, exit_pixel, return_to_lobby_pixel, confirm_pixel, reset_pixel, ready_up_pixel_fix

    def colors():
        ready_up_color = (0,0,116)
        health_color = (14,191,35)
        exit_color = (14,24,52)
        return_to_lobby_color = (0,73,169)
        confirm_color = (0,73,169)

        return ready_up_color, health_color, exit_color, return_to_lobby_color, confirm_color

    def mouse_click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.1)

    def keyboard_click(key):
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)

    def log(progress):
        if progress == 0:
            print("Successfully stored values!")
        elif progress == 1:
            print('\nDetected "Ready Up" button, entering game...')
        elif progress == 2:
            print('Detected "Health" color, pressing escape...')
        elif progress == 3:
            print('Detected "Exit" button, pressing button...')
        elif progress == 4:
            print('Detected "Return To Lobby" button, pressing button...')
        elif progress == 5:
            print('Detected "Confirm" button, pressing button...')
            print("Done!")

    def start():
        ctypes.windll.kernel32.SetConsoleTitleW("Zen v3.0")
        os.system("color 06")

        print("""    ______    ______    __   __     """)
        print("""   /\___  \  /\  ___\  /\ "-.\ \    """)
        print("""   \/_/  /__ \ \  __\  \ \ \-.  \   """)
        print("""     /\_____\ \ \_____\ \ \_\\\\"\_\  """)
        print("""     \/_____/  \/_____/  \/_/ \/_/  \n\n""")

        positions = Zen.calculate()
        colors = Zen.colors()

        fix = input("Do you need to fix some values? (y/n): ")
        if fix == "y":
            selection = input("\nWhat do you need to fix:\n 1 -> positions\n 2 -> colors\n\nNumber: ")
            if selection == "1":
                Zen.fix.get_mouse_position()
            elif selection == "2":
                Zen.fix.get_mouse_position_color()

        start_key = input("\nEnter a start key: ")
        stop_key = input("Enter a stop key: ")
        delay = input("Delay: ")
        Zen.log(0)

        while True:
            time.sleep(0.05)
            if keyboard.is_pressed(start_key):
                
                progress = 0
                while True:
                    time.sleep(float(delay))

                    if pyautogui.screenshot().getpixel((positions[6])) == colors[0] and progress == 0:
                        Zen.mouse_click(positions[0][0], positions[0][1]); win32api.SetCursorPos((positions[5]))
                        progress += 1
                        Zen.log(progress)
                        
                    elif pyautogui.screenshot().getpixel((positions[1])) == colors[1] and progress == 1:
                        Zen.keyboard_click("escape")
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[2])) == colors[2] and progress == 2:
                        Zen.mouse_click(positions[2][0], positions[2][1]); win32api.SetCursorPos((positions[5]))
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[3])) == colors[3] and progress == 3:
                        Zen.mouse_click(positions[3][0], positions[3][1]); win32api.SetCursorPos((positions[5]))
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[4])) == colors[4] and progress == 4:
                        Zen.mouse_click(positions[4][0], positions[4][1]); win32api.SetCursorPos((positions[5]))
                        progress += 1
                        Zen.log(progress)
                        break
            
            elif keyboard.is_pressed(stop_key):
                exit()

Zen.start() # Start Zen
