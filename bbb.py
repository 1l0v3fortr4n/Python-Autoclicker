import pyautogui, time, threading, keyboard

is_running = False

def autoclick(interval):
    while is_running: pyautogui.click(); time.sleep(interval)

def toggle(interval):
    global is_running
    is_running = not is_running
    if is_running: threading.Thread(target=autoclick, args=(interval,)).start()

interval = float(input("Enter click interval in seconds: "))  # CLI input for interval

keyboard.add_hotkey('F6', lambda: toggle(interval))

print("Press F6 to start/stop autoclicker, ESC to exit.")
keyboard.wait('esc')  # Program runs until ESC is pressed
