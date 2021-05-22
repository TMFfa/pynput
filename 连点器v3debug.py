# 这里说明一下之前遇到的问题
"""
    在ms_click()， 我起初没用sys.exit()，便想保证按esc也能同时退出线程，便用了下面的语句：
        if event.key == keyboard.Key.backspace or Keyboard.Key.esc:
    这就有问题了，请注意！！！！
                    == 的优先级大于 or
    参见：http://c.biancheng.net/view/2190.html
    而Keyboard.Key.esc的bool是True，就导致线程结束了。
    此外，debug的时候发现，keyboard event的for循环其实是两次，按下，抬起，这两个动作的键都是同一个键，
所以按一个键等于开了两次线程。不过这影响不大。
    还有一点，我将问题语句改为：
        if event.key == (keyboard.Key.backspace or Keyboard.Key.esc):
    这时可以正常启动线程，但是关闭时，只能先按backspace关闭线程，
如果按esc，会导致整个程序无法退出，按backspace都不行了，具体原因没有再探索了，改用了sys.exit()，程序已完美。
"""

import time
import threading
from pynput import keyboard
from pynput.mouse import Button, Controller as Mouse_controller
import sys

mouse = Mouse_controller()


def ms_click():
    while True:
        time.sleep(0.1)
        mouse.click(Button.left)
        # 注意不能用or，会又bug，而且用的话注意==优先级大于or
        if event.key == keyboard.Key.backspace:
            break
        # elif event.key == keyboard.Key.esc:
        #     break


print('press enter to start,\nand press backspace to stop,\nand press esc to quit.')

# The event listener will be running in this block

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            sys.exit()
        elif event.key == keyboard.Key.enter:
            threading.Thread(target=ms_click).start()
        else:
            print('Received event {}'.format(event))
# 程序开始后，按回车开始连点，按删除键停止，按esc退出程序
# 注意只按一次啊，这是开的线程，按多了就是多个线程，自己等死吧
