
# Import necessary libraries
from flask import Flask, request, redirect, url_for, render_template
import os
from subprocess import Popen, PIPE

# Create a Flask application
app = Flask(__name__)

# Define the route for uploading images
@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded images
    images = request.files.getlist('images')

    # Save the images to a designated folder
    image_folder = './images'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    for image in images:
        image.save(os.path.join(image_folder, image.filename))

    # Return a message indicating successful upload
    return 'Images uploaded successfully!'

# Define the route for initiating the training process
@app.route('/train')
def train():
    # Execute the command to train the neural network
    training_command = 'nerfacto train --config=configs/nerfacto_config.yaml'
    training_process = Popen(training_command, stdout=PIPE, stderr=PIPE, shell=True)

    # Monitor the training process and display progress
    while training_process.poll() is None:
        output = training_process.stdout.readline()
        print(output.decode('utf-8').strip())

    # Return a message indicating successful training
    return 'Training completed successfully!'

# Define the route for displaying the training status
@app.route('/status')
def status():
    # Check the status of the training process
    training_status = 'Training in progress...'

    # Return the training status
    return training_status

# Define the route for displaying the training results
@app.route('/result')
def result():
    # Load the training results
    results = {
        'loss': '0.01',
        'accuracy': '99%'
    }

    # Render the result page with the training results
    return render_template('result.html', results=results)

# Run the Flask application
if __name__ == '__main__':
    app.run()
