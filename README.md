# 🎧 Cold’s Spotify Skipper 🎧  
A lightweight Python script to control **Spotify playback** with custom hotkeys — skip and rewind tracks from anywhere, even in-game.

---

### 🌟 Features

- **Bind your own hotkeys** for:
  - ⏭️  Next track  
  - ⏮️  Previous track
- ⚡ Super fast response (media key simulation)
- 🧠 Smart cooldown to prevent spam skipping
- 👆 Binds only after you press your own keys — no accidental defaults
- 🔒 Keeps running until you close it manually
- 👾 Custom Discord Presence

---

### ⚙ Requirements

Install dependencies:
```bash
pip install keyboard colorama pypresence

> 💡 This script only works on Windows (uses ctypes.windll.user32). > 🛠 If hotkeys don't respond, try running it as Administrator.

🚀 How to Use
1️⃣ Run the script:

bash
python "Cold's Spotify Skipper.py"
2️⃣ Press your first key → sets skip forward 3️⃣ Press your second key → sets previous track

4️⃣ The keys are now active in the background 🎵 Close the terminal when you’re done.

❗ Notes
Hotkeys are global — they work while gaming, browsing, or even when Spotify is minimized.

The script doesn’t interfere with media playback; it just sends native commands.

Customize the script easily if you want to add pause, volume, or play controls.
