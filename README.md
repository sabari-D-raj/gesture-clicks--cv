# gesture-clicks--cv
# Hand Gesture Virtual Mouse

A Python-based virtual mouse that uses a webcam, MediaPipe hand tracking, and PyAutoGUI to control the mouse cursor using hand gestures. open application etc

## Features

* Real-time hand tracking with MediaPipe
* Mouse cursor control using index finger movement
* Single-click gesture detection
* Double-click functionality
* Smooth cursor movement
* Live hand landmark visualization

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/hand-gesture-virtual-mouse.git
cd hand-gesture-virtual-mouse
```

### Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui
```

## Usage

Run the script:

```bash
python virtual_mouse.py
```

## Controls

### Cursor Movement

Move your **index finger** to control the mouse cursor.

### Single Click

Bring your **thumb tip** and **index finger tip** close together to perform a click.

### Double Click

Perform the click gesture twice to trigger a double-click.

### Exit

Press:

```text
q
```

to quit the application.

## How It Works

1. Captures video from the webcam.
2. Detects and tracks a hand using MediaPipe.
3. Identifies key landmarks:

   * Thumb Tip (Landmark 4)
   * Index Finger Tip (Landmark 8)
4. Maps finger coordinates to screen coordinates.
5. Smooths cursor movement to reduce jitter.
6. Calculates the distance between thumb and index finger.
7. Executes click actions based on gesture detection.

## Project Structure

```text
Hand-Gesture-Virtual-Mouse/
│
├── virtual_mouse.py
├── README.md
└── requirements.txt
```

## Requirements

Create a `requirements.txt` file:

```txt
opencv-python
mediapipe
pyautogui
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Future Enhancements

* Right-click gesture
* Scroll gesture support
* Drag-and-drop functionality
* Multi-hand tracking
* Gesture customization
* Adjustable sensitivity settings

## Known Limitations

* Requires adequate lighting for accurate hand detection.
* Tracking performance depends on webcam quality.
* Fast hand movements may affect accuracy.
* Double-click detection may occasionally trigger unintentionally.

## License

This project is licensed under the MIT License.

## Author

Developed using Python, OpenCV, MediaPipe, and PyAutoGUI for gesture-based human-computer interaction.
