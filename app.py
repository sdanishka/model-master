from flask import Flask, render_template, request, jsonify, send_file
import cv2
import os
import traceback
import uuid
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            image_file = request.files['image']
            if image_file:
                image_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + image_file.filename)
                image_file.save(image_path)

                algorithm = request.form.get('algorithm')

                # Load the image
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                # Apply the selected algorithm
                if algorithm == 'canny':
                    low_threshold = int(request.form.get('low_threshold'))
                    high_threshold = int(request.form.get('high_threshold'))
                    edges = cv2.Canny(image, low_threshold, high_threshold)

                elif algorithm == 'hough':
                    edges = cv2.Canny(image, 50, 150, apertureSize=3)
                    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
                    if lines is not None:
                        for rho, theta in lines[:, 0, :]:
                            a = np.cos(theta)
                            b = np.sin(theta)
                            x0 = a * rho
                            y0 = b * rho
                            x1 = int(x0 + 1000 * (-b))
                            y1 = int(y0 + 1000 * (a))
                            x2 = int(x0 - 1000 * (-b))
                            y2 = int(y0 - 1000 * (a))

                            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

                # Save the processed image
                result_path = os.path.join(UPLOAD_FOLDER, algorithm, str(uuid.uuid4()) + 'result.jpg')
                os.makedirs(os.path.dirname(result_path), exist_ok=True)
                cv2.imwrite(result_path, edges)

                return jsonify({
                    'algorithm': algorithm,
                    'result_path': '/result/' + algorithm + '/' + os.path.basename(result_path)
                })

        except Exception as e:
            traceback.print_exc()

    return render_template('index.html')


@app.route('/result/<algorithm>/<filename>')
def get_result(algorithm, filename):
    return send_file(os.path.join(UPLOAD_FOLDER, algorithm, filename), mimetype='image/jpeg')


if __name__ == '__main__':
    app.debug = True
    app.run()
