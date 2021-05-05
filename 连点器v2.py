import time
from pynput import mouse
from pynput.mouse import Button, Controller as Mouse_controller

ms = Mouse_controller()
# 可以直接用click代替press+release，方便一点
# mouse.click(Button.right)

# 这里暂时没用
# def listen():
#     def on_move(x, y):
#         print('Pointer moved to {0}'.format(
#             (x, y)))
#
#     def on_click(x, y, button, pressed):
#         print('{0} at {1}'.format(
#             'Pressed' if pressed else 'Released',
#             (x, y)))
#         if not pressed:
#             # Stop listener
#             return False
#
#     def on_scroll(x, y, dx, dy):
#         print('Scrolled {0} at {1}'.format(
#             'down' if dy < 0 else 'up',
#             (x, y)))
#
#     # Collect events until released
#     with mouse.Listener(
#             on_move=on_move,
#             on_click=on_click,
#             on_scroll=on_scroll) as listener:
#         listener.join()
#
#     # ...or, in a non-blocking fashion:
#     listener = mouse.Listener(
#         on_move=on_move,
#         on_click=on_click,
#         on_scroll=on_scroll)
#     listener.start()


def detect():
    try:
        with mouse.Events() as events:
            for event in events:
                if event.button == Button.right:
                    break
                else:
                    if not event.pressed:
                        time.sleep(0.1)
                        ms.click(Button.left)
                        print('released')
                    else:
                        print('pressed')
    except Exception as e:
        print(e)
        detect()


# 这。。。做出了个莫名其妙的简陋版。
# 首先这个event只对鼠标的点击有效，移动会报错，所以我用try实现了循环，
# 然后他本身for循环一直运行，每次按压和释放都会记录，右键结束。
# 这个函数在你点击一次左键之后（要松开左键），就会一直循环点击，移动可以打断（通过报错打断，轻微移动都会打断），但程序还在运行，右键才结束。
detect()
# 啊这，这程序容易崩溃，也不知为啥，我傻了
