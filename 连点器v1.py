from pynput import mouse
from pynput.mouse import Button, Controller
import time


def listen():
    def on_move(x, y):
        print('Pointer moved to {0}'.format(
            (x, y)))

    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    def on_scroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    # Collect events until released
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll)
    listener.start()


def main(times):  # input click times
    listen()
    time.sleep(2)
    mouse_c = Controller()
    for i in range(times):
        time.sleep(0.1)  # 一定要加，不然点太快直接没了
        mouse_c.click(Button.left)
    print('clicked {} times'.format(times))


if __name__ == '__main__':
    # 运行后先监听，单击左键后，等2秒开始连点
    main(50)
