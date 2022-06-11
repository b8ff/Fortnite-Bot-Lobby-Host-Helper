# READ THIS!!!
#
# 1) This script uses colors to detect buttons and other stuff so MAKE SURE to use the default Fortnite color settings
# 2) This script SHOULD be compatible with any screen resolution (if not edit the variable "default_size" in "Zen.calculate()" to your screen resolution)
# 3) Fortnite MUST be windowed and maximized (look at "fortnite.png")
# 4) This script might get some updates in the future depending on Fortnite updates
# 5) This script has been tested ONLY on Windows 10 with the small taskbar setting
# 6) If there are any other problems look at the end of this file
#
# Thank you for using this script and have fun!

from win32api import GetSystemMetrics
import pyautogui
import keyboard
import win32api
import win32con
import time
import os

class Zen():
    class fix():
        def get_mouse_position():
            trigger_key = input("Enter a trigger key: ")
            stop_key = input("Enter a stop key: ")
            delay = input("Delay: ")
            while True:
                time.sleep(float(delay))
                if keyboard.is_pressed(trigger_key):
                    print(pyautogui.position())
                elif keyboard.is_pressed(stop_key):
                    break

        def get_mouse_position_color():
            trigger_key = input("Enter a trigger key: ")
            stop_key = input("Enter a stop key: ")
            delay = input("Delay: ")
            while True:
                time.sleep(float(delay))
                if keyboard.is_pressed(trigger_key):
                    print(pyautogui.screenshot().getpixel((pyautogui.position())))
                elif keyboard.is_pressed(stop_key):
                    break

    def screen():
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)

        return width, height
    
    def calculate():
        default_size = (1920, 1080)
        screen_size = Zen.screen()

        offset_values = (screen_size[0] - default_size[0], screen_size[1] - default_size[1])

        ready_up_pixel = (1538 + offset_values[0], 794 + offset_values[1])
        health_pixel = (157 + offset_values[0], 947 + offset_values[1])
        exit_pixel = (15 + offset_values[0], 984 + offset_values[1])
        return_to_lobby_pixel = (206 + offset_values[0], 981 + offset_values[1])
        confirm_pixel = (206 + offset_values[0], 981 + offset_values[1])

        return ready_up_pixel, health_pixel, exit_pixel, return_to_lobby_pixel, confirm_pixel

    def colors():
        ready_up_color = (247,255,25)
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

    def keyboard_click(key):
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)

    def log(progress):
        if progress == 1:
            print('Detected "Ready Up" button, entering game...')
        elif progress == 2:
            print('Detected "Health" color, pressing escape...')
        elif progress == 3:
            print('Detected "Exit" button, pressing button...')
        elif progress == 4:
            print('Detected "Return To Lobby" button, pressing button...')
        elif progress == 5:
            print('Detected "Confirm" button, pressing button...')
            print("Done!")

    def banner():
        print("   ____         ")
        print("  |_  /___ _ _  ")
        print("   / // -_) ' \ ")
        print("  /___\___|_||_|\n\n")

    def start():
        Zen.banner()
        os.system("color 06")

        positions = Zen.calculate()
        colors = Zen.colors()

        start_key = input("Enter a start key: ")
        exit_key = input("Enter a stop key: ")

        win32api.SetCursorPos((0, 0))
        while True:
            time.sleep(0.05)
            if keyboard.is_pressed(start_key):
                
                progress = 0
                while True:
                    if pyautogui.screenshot().getpixel((positions[0])) == colors[0] and progress == 0:
                        Zen.mouse_click(positions[0][0], positions[0][1]); win32api.SetCursorPos((0, 0))
                        progress += 1
                        Zen.log(progress)
                        
                    elif pyautogui.screenshot().getpixel((positions[1])) == colors[1] and progress == 1:
                        Zen.keyboard_click("escape")
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[2])) == colors[2] and progress == 2:
                        Zen.mouse_click(positions[2][0], positions[2][1]); win32api.SetCursorPos((0, 0))
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[3])) == colors[3] and progress == 3:
                        Zen.mouse_click(positions[3][0], positions[3][1]); win32api.SetCursorPos((0, 0))
                        progress += 1
                        Zen.log(progress)

                    elif pyautogui.screenshot().getpixel((positions[4])) == colors[4] and progress == 4:
                        Zen.mouse_click(positions[4][0], positions[4][1]); win32api.SetCursorPos((0, 0))
                        progress += 1
                        Zen.log(progress)
                        break
            
            elif keyboard.is_pressed(exit_key):
                break

Zen.start() # Main Function

# If you need to fix some values for whatever reason you can use these two functions below here, if you use them MAKE SURE to comment out the main function "Zen.start()" and
# use only one at a time.

# Zen.fix.get_mouse_position()
# Zen.fix.get_mouse_position_color()
