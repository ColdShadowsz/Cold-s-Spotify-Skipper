import keyboard
import ctypes
import time
from colorama import init, Fore
from pypresence import Presence

# ────────── Setup ──────────
init(autoreset=True)
blue = Fore.CYAN

# Discord Rich Presence
CLIENT_ID = "1394495994221039677"
rpc = Presence(CLIENT_ID)
rpc.connect()
rpc.update(
    state="Selecting Hotkeys",
    details="Cold's Spotify Skipper",
    large_image="skipper",
    large_text="Cold's Spotify Skipper"
)

# ────────── Banner ──────────
print(r"""
   ___     _    _      ___          _   _  __        ___ _   _                   
  / __|___| |__| |___ / __|_ __ ___| |_(_)/ _|_  _  / __| |_(_)_ __ _ __ ___ _ _ 
 | (__/ _ | / _` (_-< \__ | '_ / _ |  _| |  _| || | \__ | / | | '_ | '_ / -_| '_|
  \___\___|_\__,_/__/ |___| .__\___/\__|_|_|  \_, | |___|_\_|_| .__| .__\___|_|  
                          |_|                 |__/            |_|  |_|           
""")

# ────────── State ──────────
bind_stage = 0
skip_key = None
prev_key = None
last_skip = 0
last_prev = 0

# ────────── Action Functions ──────────
def skip_track():
    global last_skip
    now = time.time()
    if now - last_skip > 0.5:
        ctypes.windll.user32.keybd_event(0xB0, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0xB0, 0, 2, 0)
        print(blue + "⏭️  Skipped track")

        rpc.update(
            state=f"Hotkeys set: {skip_key} + {prev_key}",
            details="⏭️ Skipping...",
            large_image="skipper",
            large_text="Cold's Spotify Skipper"
        )
        time.sleep(2)

        rpc.update(
            state=f"Hotkeys set: {skip_key} + {prev_key}",
            details="Idle",
            large_image="skipper",
            large_text="Cold's Spotify Skipper"
        )

        last_skip = now

def previous_track():
    global last_prev
    now = time.time()
    if now - last_prev > 0.5:
        ctypes.windll.user32.keybd_event(0xB1, 0, 0, 0)
        ctypes.windll.user32.keybd_event(0xB1, 0, 2, 0)
        print(blue + "⏮️  Previous track")

        rpc.update(
            state=f"Hotkeys set: {skip_key} + {prev_key}",
            details="⏮️ Rewinding...",
            large_image="skipper",
            large_text="Cold's Spotify Skipper"
        )
        time.sleep(2)

        rpc.update(
            state=f"Hotkeys set: {skip_key} + {prev_key}",
            details="Idle",
            large_image="skipper",
            large_text="Cold's Spotify Skipper"
        )

        last_prev = now

# ────────── Key Capture ──────────
def capture_key(e):
    global bind_stage, skip_key, prev_key

    print(blue + f"🔍 Captured: key='{e.name}', scan_code={e.scan_code}")
    key = e.name

    if key in ['ctrl', 'alt', 'shift', 'windows', 'enter']:
        return

    if key == 'backspace':
        print(blue + "⚠️  Backspace is blocked from being bound. Try a different key.")
        return

    if bind_stage == 0:
        skip_key = key
        print(blue + f"✅ Skip bound to: {skip_key}")
        bind_stage = 1
    elif bind_stage == 1:
        prev_key = key
        print(blue + f"✅ Previous bound to: {prev_key}")
        keyboard.unhook(capture_hook)
        keyboard.add_hotkey(skip_key, skip_track)
        keyboard.add_hotkey(prev_key, previous_track)

        rpc.update(
            state=f"Hotkeys set: {skip_key} + {prev_key}",
            details="Idle",
            large_image="skipper",
            large_text="Cold's Spotify Skipper"
        )
        print(blue + "🎵 Hotkeys active! Close the window to stop the script.")
        bind_stage = 2

# ────────── Start Binding ──────────
print(blue + "🎧 Press a key for SKIP, then another for PREVIOUS (e.g. '\\' and ']').")
capture_hook = keyboard.on_press(capture_key)
keyboard.wait()
