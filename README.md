# Object Tracking using OpenCV

This repository contains code for real-time object tracking using OpenCV. The program tracks a specific colored object (in this case, red) using computer vision techniques and provides directions based on the position of the tracked object.

## Requirements

- Python 3.x
- OpenCV
- imutils

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install the required dependencies using pip:

   ```
   pip install opencv-python imutils
   ```

## Usage

1. Connect a USB-connected Android device with an active camera.
2. Obtain the IP address of the device and update the `address` variable in the code with the correct IP address.
3. Run the script:

   ```
   python object_tracking.py
   ```

4. A new window will open displaying the live camera feed with the tracked object highlighted.
5. The program will print directions based on the position of the tracked object:
   - If the object's radius is greater than 250, it will print "stop."
   - If the object's x-coordinate is less than 150, it will print "Left."
   - If the object's x-coordinate is greater than 450, it will print "Right."
   - If the object's radius is less than 250, it will print "Front."
   - Otherwise, it will print "Stop."

6. To quit the program, press the 'q' key.

## License

This project is licensed under the Apache License. 

## Acknowledgments

- The code is adapted from the work done by Pantech University
- Thanks to the creators of [imutils](https://github.com/jrosebr1/imutils) for providing useful image processing functions.