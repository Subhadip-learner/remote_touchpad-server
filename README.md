📱🖥️ Mobile Touchpad Controller
Turn your smartphone into a wireless touchpad for your computer!
A Flask-SocketIO server that converts mobile touch gestures into mouse movements, clicks, and scroll events on your desktop.

🌟 Features
```
Multi-touch support (1-2 fingers)
Low latency (~15ms movement delay)
Cross-platform (Windows/macOS/Linux)
No apps required (Works in mobile browsers)
Battery efficient (WebSocket connection)
```
🛠️ How It Works

<img width="2196" height="1449" alt="image1" src="https://github.com/user-attachments/assets/52f6fc4d-16af-4660-83e1-7c5eed820f18" />

🚀 Installation
Prerequisites
Python 3.7+

Mobile device and computer on same network
```
# 1. Clone repository  
git clone https://github.com/yourusername/mobile-touchpad.git  
cd mobile-touchpad  

# 2. Install dependencies  
pip install flask flask-socketio pyautogui  

# 3. Run the server  
python server.py  

# 4. Open mobile browser to:  
# http://[your-computer-ip]:5000  
```
🖐️ Gesture Controls
```
#👆 Single tap	Left click	🖱️→📱
#✌️ Two-finger tap	Right click	🖐️✌️→📱
#👆➡️ Drag	Mouse move	👆→➡️
#✌️⬇️ Scroll	Vertical scroll	🖐️🖐️↓↑
```
⚙️ Configuration
Edit server.py to customize:
```
# Sensitivity settings  
MOVE_SENSITIVITY = 1.5  # Higher = faster cursor  
SCROLL_SENSITIVITY = 2.0  

# Server port  
PORT = 5000  
```
📊 Performance Metrics
```
Metric	Value
Movement sampling rate	120Hz
Click recognition delay	<50ms
WebSocket packet size	~50-100KB/min
```
🤝 Contributing
```
1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit changes (git commit -m 'Add amazing feature')
4. Push (git push origin feature/AmazingFeature)
5. Open a Pull Request
```

🤖 Feature	Tech Stack Development Guide(How to Contribute) :
Gesture Learning	
Voice Shortcuts
Gaze Tracking	
Palm Rejection	


📜 License
MIT ©Subhadip Medya

✉️ Contact
Mail : subhadipmedya2512@gmail.com   



Linkedin : 
                    
![linkedin qr](https://github.com/user-attachments/assets/75ddc88d-20d4-4bb7-9abd-531b4b2dfaa4)












