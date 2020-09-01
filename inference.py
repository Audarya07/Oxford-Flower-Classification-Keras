print("Importing all required libraries...")
import os
import numpy as np
import scipy.io
import keras
from keras.utils import to_categorical
from keras.models import load_model
import cv2
from sklearn.model_selection import train_test_split
from scipy.io import loadmat
print("Importing libraries done...")

print("Loading image labels..")
img_labels = scipy.io.loadmat("imagelabels.mat")
img_labels = img_labels["labels"]
img_labels = img_labels[0]
for i in range(len(img_labels)):
	img_labels[i] = img_labels[i] - 1
	

print("Number of labels:",len(img_labels))


idmat = loadmat('setid.mat')
idmat.keys()
test_num = idmat['tstid']
test_num = test_num[0]
print("Number of images in the test set: {}".format(len(test_num)))


print("Accessing test images and converting them to arrays....Please wait..takes time!!")
test_x=[]
test_y = []
for i in range(len(test_num)):
  try:
    dir = 'jpg/image' + '_' + str(test_num[i]).zfill(5) + '.jpg'
    image = cv2.imread(dir)
    new_image = cv2.resize(image,(150,150))
    new_image = new_image.astype('float32')
    new_image /=255.0
    test_x.append(new_image)
  except Exception as e:
    print(str(e)) 
test_x = np.asarray(test_x, dtype=np.float32)   
print("Test data shape:",test_x.shape)

print("Getting test image labels...")
for i in range(len(test_num)):
  test_y.append(img_labels[test_num[i]-1])
test_y = np.asarray(test_y, dtype=np.float32)


print("Number of images:",len(test_x))
print("Number of labels:",len(test_y))

test_y = to_categorical(test_y)


#Load model
print("Loading model...")
model = load_model("model.h5")

print("Evaluating model on test data.....Please wait......")
score = model.evaluate(test_x, test_y,verbose=0) 

print('Test loss:', score[0]) 
print('Test accuracy:', score[1])

