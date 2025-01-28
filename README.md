# 🚨 Adult Video Detection 📹

## Overview

**"Adult Video Detection"** is a machine learning-based web application designed to automatically detect adult content in videos. It uses advanced computer vision techniques to analyze video frames and classify content as either safe or explicit. The project is built with **Python**, utilizing libraries such as **TensorFlow** for model training, **OpenCV** for video processing, and **Flask** for serving the application. The goal is to ensure safer online environments by detecting and flagging adult content in video platforms.

## Features

- **Adult Content Detection**: Automatically detect explicit content in videos based on frames analysis.
- **Real-Time Classification**: Analyze videos in real-time to classify them as safe or explicit.
- **Machine Learning Model**: Trained on a large dataset of labeled videos to recognize adult content with high accuracy.
- **User-Friendly Interface**: Upload videos and receive immediate classification results via a web interface.
- **Video Processing**: Extract video frames for analysis, ensuring efficient detection of explicit content in videos.

## Tech Stack

- **Back-End**: Flask (Python)
- **Front-End**: HTML, CSS (for simple web interface)
- **Machine Learning**: TensorFlow, Keras
- **Computer Vision**: OpenCV, NumPy
- **Deployment**: Localhost (for local deployment)

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/veer-debug/Instagram_adult_contant_dection.git
   cd Instagram_adult_contant_dection
2. **Create a Virtual Environment**
   ```bash
    python3 -m venv venv
    source venv/bin/activate  
    # On Windows, use 
    venv\Scripts\activate
3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
4. **Run the Application**

    ```bash
    python app.py
- Open your browser and navigate to http://127.0.0.1:5000/ to access the application.

## Usage
- Upload Video: Click on the "Upload Video" button to select a video file from your local machine.
- Real-Time Detection: After uploading, the video is processed and analyzed frame by frame to detect adult content.
- Results: The system will return a classification of "Safe" or "Explicit" based on the content in the video.
## Machine Learning Integration
### Adult Content Detection
- Model Used: Convolutional Neural Networks (CNN) and pre-trained models.
- Description: The model is trained on a large dataset of labeled videos, enabling it to analyze each frame and classify it as either safe or explicit. It leverages TensorFlow and Keras for deep learning and pattern recognition.
## Real-Time Video Processing
- Techniques Used: OpenCV is used to capture and process video frames for analysis. Each frame is passed through the trained model for classification.
- Description: The app processes the uploaded video, analyzing -individual frames, and classifying them based on patterns learned during training. The real-time processing ensures rapid feedback to users.
## Example of AI in Action
- Training: The model is trained on a diverse set of labeled video frames that include both explicit and non-explicit content. This training allows the model to recognize adult content based on visual cues such as nudity, explicit gestures, and inappropriate scenes.
- Frame Analysis: As the video is uploaded, it is split into individual frames. These frames are passed through the model, which makes predictions based on the content of each frame.
- Classification: After analyzing all frames, the system provides a final classification of the entire video as either "Safe" or "Explicit."
## Contributing
- Contributions are welcome! If you have suggestions, improvements, or fixes, please follow these guidelines:

### Fork the repository.
- Create a new branch for your changes.
- Commit your changes with descriptive messages.
- Push your changes to your forked repository.
- Create a pull request from your branch to the main repository.
## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- TensorFlow/Keras: A deep learning framework used for building and training the neural network model.
- OpenCV: A computer vision library used for processing video frames.
- Flask: A lightweight framework for serving the application and handling user requests.
- NumPy: A fundamental package for scientific computing with Python, used for handling arrays during frame analysis.
