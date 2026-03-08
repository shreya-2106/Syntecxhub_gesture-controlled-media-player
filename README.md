## Syntecxhub_gesture controlled media player
A Python project that allows you to control your media player (music or video) using hand gestures via your webcam. No keyboard or mouse is required. 
This project uses MediaPipe for hand tracking, OpenCV for webcam video feed, and PyAutoGUI to simulate media key presses.


## Features
- Play / Pause: Fist (✊) gesture   
- Volume Up: One finger (☝️) gesture  
- Volume Down: Two fingers (✌️) gesture  
- Pause / Space: Open palm (✋) gesture  
- Real-time hand skeleton tracking  
- Works on Windows with Python 3.10  
- Gesture cooldown to avoid repeated triggers  

##  How it Works
The webcam captures real-time video, and MediaPipe tracks hand landmarks to detect finger positions. Based on the number of fingers raised, PyAutoGUI simulates media key presses to control play, pause, or volume. OpenCV displays the hand skeleton and current gesture on screen.

## Technology Used
-Python 3.10 
-MediaPipe 
-OpenCV 
-PyAutoGUI 

## How to Run
1.Clone the repository:
git clone https://github.com/<your-username>/gesture-controlled-media-player.git 
cd gesture-controlled-media-player

2.Create a virtual environment:
python -m venv venv

3.Activate the virtual environment:
Windows:
.\venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

4.Install dependencies:
pip install -r requirements.txt

5.Run the main script:
python main.py

