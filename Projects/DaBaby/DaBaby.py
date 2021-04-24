from playsound import playsound
from pynput import mouse
import sys
import os
if getattr(sys, 'frozen', False):
    Current_Path = os.path.dirname(sys.executable)
else:
    Current_Path = str(os.path.dirname(__file__))


def on_click(x, y, button, pressed):
    if pressed:
        playsound('YeahYeah.mp3', block=False)
    if not pressed:
        return False


while True:
    with mouse.Listener(on_click=on_click,) as listener:
        listener.join()
