# remote_touchpad-server

# 📱 Mobile Touchpad – Turn Your Phone into a Wireless Mouse!

Transform your smartphone or tablet into a **wireless touchpad** for your computer using just a browser. Perfect for presentations, watching movies, or lazy couch computing. 🛋️📱

---

## ✨ Features

- 🖱️ **Multi-touch gestures**
  - Single tap → Left click
  - Two-finger tap → Right click
  - Drag → Cursor movement
  - Two-finger drag → Scrolling
- 🌐 **Cross-platform** – Works on any device with a browser
- ⚡ **Low latency** – Smooth and responsive controls
- 🚫 **No app installation** – Just a browser is enough
- 🧠 **Simple Python-based backend**

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6+
- A smartphone or tablet with a modern browser

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/remote_touchpad-server.git
cd remote_touchpad-server

```

# Install dependencies:

```
pip install flask flask-socketio pyautogui
```
### Requirements.txt

# Python 3.13.5 compatible
```
Flask==3.1.1
Flask-SocketIO==5.5.1
PyAutoGUI==0.9.54
```
# Transitive dependencies
```
python-engineio==4.9.0
python-socketio==5.11.2
```
### ✌️ Repository Structure Recommendation
```
remote_touchpad-server/
├── server.py               # Main server code
├── requirements.txt        # Dependency file (you're creating this)
├── static/
│   └── touchpad.html       # HTML interface 
├── README.md               # Project documentation
└── .gitignore              # Ignore Python cache files

```
▶️ Usage
Run the server:

bash
Copy
Edit
```
python server.py
```
Check the terminal for your local IP (e.g., http://192.**8.*.**0:5000)

Open the address on your mobile device browser

Use touch gestures to control your PC!

✋ Supported Gestures
Gesture	Action
Single tap	Left click
Two-finger tap	Right click
Drag	Move cursor
Two-finger drag	Scroll
🔜 Pinch-to-zoom	(Coming soon)

🌐 Network Setup Tips
Connect both PC and phone to the same WiFi network

If access fails:

Check firewall settings on PC
Ensure port 5000 is allowed
Remote access over the internet requires port forwarding (advanced)

🤝 Contributing
Contributions are welcome and appreciated!

Fork this repository

Create a feature branch:  
``` 
git checkout -b feature/YourFeatureName
```
Commit your changes: 

```
git commit -m "Add: Your feature"
```
Push to the branch: 
```
git push origin feature/YourFeatureName
```
Open a Pull Request



📧 Contact
Your Name
📬 subhadipmedya2512@gmail.com
🔗 GitHub: https://github.com/Subhadip-learner/remote_touchpad-server

☕ Acknowledgments
Inspired by every time I lost my mouse under the couch 🛋️

- Built with love using Flask, Socket.IO, and pyautogui

- Fueled by ☕ and late-night coding
