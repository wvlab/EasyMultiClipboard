import pyperclip as clip
import keyboard

global data
data = {i: None for i in range(10)}

def change(key):
    global data
    if data[key] is not None:
        clip.copy(data[key])
    return

def insert(key):
    global data
    data[key] = clip.paste()
    return

for i in range(10):
    keyboard.add_hotkey(f'Ctrl+Space+{i}', change, args=[i])
    keyboard.add_hotkey(f'Ctrl+Alt+{i}', insert, args=[i])

keyboard.wait()
