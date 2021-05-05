# 这应该是可控版本了
import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller as Mouse_controller

mouse = Mouse_controller()


def ms_click():
    while True:
        time.sleep(0.1)
        mouse.click(Button.left)
        if event.key == keyboard.Key.backspace:
            break


print('press enter to start,\nand press backspace to stop,\nand press esc to quit.')

# The event listener will be running in this block

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            break
        elif event.key == keyboard.Key.enter:
            threading.Thread(target=ms_click).start()
        else:
            print('Received event {}'.format(event))
# 程序开始后，按回车开始连点，按删除键停止，按esc退出程序
# 注意只按一次啊，这是开的线程，按多了就是多个线程，自己等死吧
