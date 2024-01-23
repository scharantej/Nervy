## Flask Application Design

### HTML Files

- **index.html**:
  - This is the landing page of our application.
  - It will contain instructions and explanations of the app's functionality and usage.
  - It will display a form for uploading images and a button to trigger the training process.


- **result.html**:
  - This page will display the results of the training.
  - It will include visualizations and metrics to evaluate the model's performance.


### Routes

- **"/upload"**:
  - This route will handle the upload of images from the user's computer.
  - It will save the uploaded images in a designated folder on the server.


- **"/train"**:
  - This route will be responsible for initiating the training process.
  - It will execute the necessary commands to train the neural network using the uploaded images.


- **"/status"**:
  - This route will provide information about the current status of the training process.
  - It will return messages indicating the progress, completion, or any errors encountered during training.


- **"/result"**:
  - This route will display the results of the training.
  - It will render the "result.html" page with the appropriate visualizations and metrics.