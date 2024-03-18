# FlaskColorWorks

FlaskColorWorks is a dynamic web application powered by Flask, designed to showcase the integration of advanced computer vision techniques directly within a user-friendly web interface. This application utilizes deep learning models for object detection and segmentation, enabling users to selectively apply color transformations to objects within uploaded images. The core functionality revolves around preserving the texture and details of the objects while altering their color, demonstrating the practical application of computer vision and machine learning in media manipulation.

## Key Features

- **User-Friendly Interface**: Simple and intuitive web interface for easy navigation and interaction.
- **Dynamic Object Colorization**: Apply different colors to specific objects within images without losing texture or detail.
- **Real-Time Processing**: Quick and responsive image processing, allowing for immediate visual feedback.
- **Advanced Computer Vision**: Leverages the Mask R-CNN model for accurate object detection and segmentation.

## Getting Started

### Prerequisites

Ensure you have Python 3.6+ installed on your system. FlaskColorWorks relies on several Python libraries, including Flask, PyTorch, torchvision, and OpenCV, among others.

### Installation

Follow these steps to get FlaskColorWorks running on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/raihan-js/FlaskColorWorks.git
Navigate to the project directory:

cd FlaskColorWorks

#### Install dependencies:

pip install -r requirements.txt
Run the application:

flask run

or

python app.py
Open your web browser and go to http://127.0.0.1:5000/ to start using FlaskColorWorks.

### Usage
From the homepage, select an image file you wish to upload and colorize.
Input the target object's label ID that you wish to colorize within the image.
Specify the desired RGB color values (e.g., 255,0,0 for red).
Submit the form to process the image.
The application will display the original image alongside the colorized version for comparison.

### Contributing
We welcome contributions to FlaskColorWorks! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

### License
FlaskColorWorks is open-sourced under the MIT License. See the LICENSE file for more details.

### Requirements.txt

Your `requirements.txt` file should list all Python libraries that your project depends on. You can generate this file by activating your project's virtual environment, running your application to verify that all dependencies are installed, and then using `pip freeze`. Here’s a basic example:


Flask==2.0.1
Werkzeug==2.0.1
torch==1.8.1
torchvision==0.9.1
opencv-python-headless==4.5.2.52
Pillow==8.2.0
numpy==1.20.3


Adjust the versions based on the current versions you're using. Note that opencv-python-headless is used instead of opencv-python to reduce the number of unnecessary GUI dependencies for server deployments.