from playsound import playsound
from pynput import keyboard

hasReleased = True


def on_press(key):
    global hasReleased
    if hasReleased:
        try:
            playsound('YeahYeah.mp3', block=False)
            hasReleased = False
        except AttributeError:
            playsound('YeahYeah.mp3', block=False)
            hasReleased = False


def on_release(key):
    global hasReleased
    hasReleased = True
    if key == keyboard.Key.esc:
        # Stop listener
        return False


while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
