# vlc_macropad.py
# Maps four buttons to VLC media controls using media keys.
# Requires: pip install keyboard
# Run as administrator on Windows.

import keyboard
import time

# Button mappings (replace 'f13'–'f16' with your macropad keys if different)
SW1 = 'f13'  # Play / Pause
SW2 = 'f14'  # Volume Up
SW3 = 'f15'  # Volume Down
SW4 = 'f16'  # Mute

keyboard.add_hotkey(SW1, lambda: keyboard.send('play/pause media'))
keyboard.add_hotkey(SW2, lambda: keyboard.send('volume up'))
keyboard.add_hotkey(SW3, lambda: keyboard.send('volume down'))
keyboard.add_hotkey(SW4, lambda: keyboard.send('volume mute'))

while True:
    time.sleep(1)
