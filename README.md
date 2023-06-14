# Model Master Project

Model Master is a web application that allows users to visualize two OpenCV algorithms: Canny Edge Detection and Hough Transform. The application provides a user-friendly interface built using HTML, CSS, and JavaScript as the front-end, and Python Flask as the back-end.

### Prerequisites

To run the Model Master project, ensure that you have the following installed:

* Python 3.7 or latter 
* Flask
* OpenCV
* HTML, CSS, and JavaScript compatible web browser

### Getting Started

1. Clone the repository or download the project files.
2. Install the required Python dependencies by running the following command in the project's root directory: `pip install -r requirements.txt`
3. Run the Flask development server by executing the following command: `python app.py`
4. Open your web browser and access the application using the following URL: http://localhost:5000

### Usage

1. Upon accessing the application, you will see two algorithm buttons: "Canny Edge Detection" and "Hough Transform."
2. Click on the desired algorithm button to select it.
3. Once an algorithm is selected, an image upload form will appear below the algorithm buttons.
4. Click the "Choose File" button to upload an image for processing.
5. Adjust the "Low Threshold" and "High Threshold" values if you selected the Canny Edge Detection algorithm. These values determine the sensitivity of the edge detection.
6. Click the "Submit" button to process the uploaded image using the selected algorithm.
7. The processed image will be displayed below the upload form.
8. You can switch between algorithms by clicking on the respective algorithm button and repeating the upload process.

### File Structure

The project files are structured as follows:

* #### app.py:
The main Python script that implements the Flask server and handles the image processing.
* #### templates/index.html:
The HTML template that defines the web application's user interface.


### Technologies Used

* Python
* Flask
* OpenCV
* HTML
* CSS
* JavaScript

### Acknowledgments

The Model Master project is based on the Flask framework and utilizes the OpenCV library for image processing. The project structure and code are inspired by various online tutorials and examples.

### Troubleshooting

If you encounter any issues while running the application, ensure that you have installed the required dependencies and that there are no errors in the console.
If you experience any difficulties with image processing or algorithm results, refer to the OpenCV documentation for detailed explanations of the Canny Edge Detection and Hough Transform algorithms.