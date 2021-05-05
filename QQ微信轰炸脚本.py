from pynput.mouse import Button, Controller as Mouse_controller
from pynput.keyboard import Key, Controller as Key_controller
import time

mouse = Mouse_controller()
keyboard = Key_controller()
time.sleep(3)
mouse.press(Button.left)
mouse.release(Button.left)
for i in range(30):
    time.sleep(0.1)
    keyboard.type('待输入内容')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
