import asyncio
import datetime
import random
import websockets
import pyperclip
import json
import sys
import psutil
import os
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.withdraw()

sys.stdout = open('log.log', 'w')
occurences = []
for item in list(psutil.process_iter()):
    try:
        if item.name() == "clipboard_serve.exe":
            occurences += [item]
            print(item)
    except psutil.AccessDenied:
        pass
print(len(occurences))
if len(occurences) >= 2:
    tkinter.messagebox.showinfo(title="Clipboard serve", message="Terminating clipboard serve")
    for item in occurences:
        if int(item.pid) == int(os.getpid()):
            continue
        item.terminate()
    os._exit(1)
else:
    tkinter.messagebox.showinfo(title="Clipboard serve", message="Launching clipboard serve.")

global config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

async def time(websocket, path):
    first = True
    last_content = ""
    while True:
        if first:
            first = False
            last_content = pyperclip.paste()
            await websocket.send(last_content)
            
        else:
            current_content = pyperclip.paste()
            if not(last_content == current_content):
                last_content = current_content
                await websocket.send(last_content)
        await asyncio.sleep(config["wait_time"])

start_server = websockets.serve(time, config["ip"], config["port"])

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
