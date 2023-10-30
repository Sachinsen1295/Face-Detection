# Face Detection with OpenCV

This project demonstrates how to perform face detection using OpenCV and provides a streamlined setup process through a single command that automates multiple tasks, including creating a virtual environment.

## Prerequisites

Before you get started, ensure you have the following prerequisites installed on your system:

- Python (version 3.7 or higher)
- Virtualenv (recommended for creating a virtual environment)
- Git (to clone this repository)

## Setup

To simplify the setup process, you can use the following one-liner to create a virtual environment, install the required dependencies, and run the face detection script:

```bash
git clone https://github.com/Sachinsen1295/Face-Detection.git && cd face-detection && sh init_setup.sh

github link to download models - https://github.com/spmallick/mallick_cascades/tree/master/haarcascades

to install cv2 from command line - pip3 install opencv-python

```

##  One command 

### To create  environment , run file , install requirements

```
bash init_setup.sh
```
## Manual Setup (Optional)
#### If you prefer manual setup, follow these steps:

### Clone the Repository:

bash
```
git clone https://github.com/yourusername/face-detection.git
cd face-detection

```

### Create a Virtual Environment (Optional but recommended):
```
conda create -p env python=3.8 -y
```

### Install Dependencies:

```
pip install -r requirements.txt
```

### Run the Face Detection Script:

```
python face_detection.py
```



Press Q to exit the application.

Customization
You can customize the face detection by modifying the face_detection.py script and adjusting parameters to suit your needs.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenCV for providing a powerful computer vision library.
Your Favorite Python Community for the Python programming language.
Enjoy exploring and experimenting with face detection using OpenCV!

Feel free to contribute to this project by submitting pull requests or reporting issues.



