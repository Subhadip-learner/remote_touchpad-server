# server.py
from flask import Flask, render_template
from flask_socketio import SocketIO
import pyautogui
import socket
import time
import threading

app = Flask(__name__)
# Allow all origins for SocketIO connections since we're running locally
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

def get_ip():
    """Get the local IP address of this machine to make it accessible on the network"""
    try:
        # Create a temporary connection to Google's DNS to find our own IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"Couldn't get IP address, using localhost: {e}")
        return "127.0.0.1"  # Fallback to localhost if there's an issue

@app.route('/')
def home():
    """Serve the main touchpad interface page"""
    return render_template('touchpad.html')

# Movement tracking variables
move_buffer = []  # Stores pending mouse movements
last_move = time.time()  # Time of last processed movement
move_lock = threading.Lock()  # Prevents race conditions with the buffer

def process_moves():
    """Process all accumulated mouse movements in one go for better performance"""
    global move_buffer, last_move
    with move_lock:
        if move_buffer:
            # Sum up all the pending movements
            total_x = sum(m['dx'] for m in move_buffer)
            total_y = sum(m['dy'] for m in move_buffer)
            move_buffer = []  # Clear the buffer
            
            try:
                # Execute the combined movement
                pyautogui.moveRel(total_x, total_y, _pause=False)
            except Exception as e:
                print(f"Mouse movement error: {e}")

@socketio.on('move_batch')
def handle_moves(data):
    """Handle incoming mouse movement data from the client"""
    global move_buffer, last_move
    now = time.time()
    
    # Add new movements to the buffer
    with move_lock:
        move_buffer.extend(data)
    
    # Process movements if enough time has passed (~120Hz)
    if (now - last_move) > 0.008:
        process_moves()
        last_move = now

@socketio.on('left_click')
def left_click():
    """Simulate a left mouse click"""
    try:
        pyautogui.mouseDown(button='left', _pause=False)
        time.sleep(0.02)  # Brief delay to make it register as a click
        pyautogui.mouseUp(button='left', _pause=False)
    except Exception as e:
        print(f"Left click didn't work: {e}")

@socketio.on('right_click')
def right_click():
    """Simulate a right mouse click"""
    try:
        pyautogui.mouseDown(button='right', _pause=False)
        time.sleep(0.02)
        pyautogui.mouseUp(button='right', _pause=False)
    except Exception as e:
        print(f"Right click failed: {e}")

@socketio.on('double_click')
def double_click():
    """Simulate a double click with appropriate timing"""
    try:
        for _ in range(2):
            pyautogui.mouseDown(button='left', _pause=False)
            time.sleep(0.02)
            pyautogui.mouseUp(button='left', _pause=False)
            time.sleep(0.08)  # Slightly longer delay between clicks
    except Exception as e:
        print(f"Double click didn't register: {e}")

@socketio.on('scroll')
def handle_scroll(data):
    """Handle scroll events from the touchpad"""
    try:
        amount = data.get('amount', 0)
        # Negative because touchpad scroll direction is opposite to mouse wheel
        pyautogui.scroll(-int(amount), _pause=False)
    except Exception as e:
        print(f"Scroll didn't work: {e}")

if __name__ == '__main__':
    # Configure pyautogui for fastest response
    pyautogui.FAILSAFE = False  # Disable the safety feature that stops the program
    pyautogui.PAUSE = 0  # Remove any artificial delays
    
    ip = get_ip()
    print(f"\nTouchpad server running at: http://{ip}:5000")
    print("Press Ctrl+C to stop the server\n")
    
    try:
        # Start the web server accessible from any device on the network
        socketio.run(app, host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Server encountered an error: {e}")