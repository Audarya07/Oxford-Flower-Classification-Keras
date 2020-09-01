## Oxford Flower DataSet Classification using Keras API

### Preprocessing and preparing training & testing sets
* Preprocessing is performed on the flowers dataset so that it can be fed into the model.
* We extract the y_train, y_test and y_valid values from **setid.mat** file.
* The **imagelabels.mat** file provides the labels for our images.
* I have used 5240 images for the training set , 1311 for validation set and rest the 1638 imagesused for testing purposes.

### Making training, test and validation data
* Each of the images has been resized to 150 * 150 pixels format.
* All the images are fed into the convolutional layer in the form of an array.

### Making the model
1. Here we have first initialised the Sequential model.
2. Then we have used 1 convolutional layer having input shape 150 X 150 pixels for our model, activation function as ReLU and 64 feature detector of size 3 * 3.

3. Then we have used 2 convolutional layers having activation function as ReLU and 128 feature detector of size 3 * 3.
4. Then we have used 1 convolutional layer having activation function as ReLU and 256 feature detector of size 3 * 3.
5. Max pooling layers of size 2 * 2 units and Dropout of 0.5 units have been used.
4. Next the flattening operation is performed to convert the pooled features into a single vector.
5. This flattened vector is fed into a hidden with 512 neurons which applies layer the ReLU activation function.
6. In the end we get the output as one of the flowers from 102 categories. Since we have more than 2 categories, we are using __softmax__ activation function.

### Compiling and Fitting the model to the training set
* We compile the model using the **Adam** optimizer, loss function **categorical_crossentropy**  and metrics as **accuracy**.
* Lastly we fit our model to the classifier with **50 epochs**.

### Docker Files include:
* **jpg** - It is a directory which has flower images.
* **model.h5** - Model which gives accuracy of 50.30 on testing data.
* **Dockerfile** - File containing the dependencies for our images. Helps to copy files to our docker image and define the command to run our image. 
* **imagelabels.mat** && **setid.mat** - To get the id's and labels for our images.
* **inference.py** - This file contains the python program to inference our model.
* **requirements.txt** - It includes all the packages which are required for running our project.

__Note__ : Ubuntu 16.04 is used as the base image for our docker image.

**DockerHub repo link** : https://hub.docker.com/repository/docker/audaryauttarwar/keras-flower  
**Link to DataSet** : http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html
