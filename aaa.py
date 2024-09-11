import pyautogui, time, threading, keyboard, tkinter as tk

def autoclick(interval):
    while is_running: pyautogui.click(); time.sleep(interval)

def toggle(interval):
    global is_running
    is_running = not is_running
    status.config(text=f"Autoclicker {'running' if is_running else 'stopped'} (F6)")
    if is_running: threading.Thread(target=autoclick, args=(interval,)).start()

root, is_running = tk.Tk(), False
tk.Label(root, text="Click interval (seconds)").pack()
entry, status = tk.Entry(root), tk.Label(root, text="Press F6 to start")
entry.pack(), status.pack()

keyboard.add_hotkey('F6', lambda: toggle(float(entry.get()) if entry.get() else 0.1))
root.mainloop()
keyboard.wait('esc')
