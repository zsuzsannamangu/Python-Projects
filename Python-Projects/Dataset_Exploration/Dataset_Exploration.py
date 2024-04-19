#Dataset Exploration and Preprocessing Assignment

#Install any needed libraries
#pip install scikit-learn (scikit-learn is a machine learning library)
#pip install numpy (NumPy is a library for numerical computing in Python)
#pip install matplotlib (Matplotlib is a plotting library in Python that allows creation of various visualizations)

#Download the CIFAR-10 dataset and save it in your chosen directory (use this directory to save upcoming code): cifar-10-python.tar.gz 
#Note: “CIFAR-10” stands for “Canadian Institute for Advanced Research (CIFAR) 10-class classification dataset.” 
#It is a widely used dataset in computer vision and machine learning research. The dataset consists of 60,000 32x32 color images in 10
#different classes, with 6,000 images per class. The classes include common objects such as airplanes, automobiles, birds, cats, dogs, etc.

#Import required libraries by writing this code:
import pickle #“pickle” is a Python module that provides a way to serialize (convert data into a suitable storage or transmission format) and deserialize Python objects, allowing them to be saved or transferred between processes.
import numpy as np
from sklearn.model_selection import train_test_split
import tarfile #“tarfile” is a module in Python that provides support for reading and manipulating tar archive files, which are commonly used for file compression and storage.
import matplotlib.pyplot as plt

#Extract the dataset using the tarfile module by writing this code:
tar = tarfile.open(r"/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Dataset_Exploration/cifar-10-python.tar.gz")
tar.extractall()
tar.close() #This line closes the tar file after extraction.

#Define a function to load the batch file (script or text file containing commands that can be executed by a computer in sequence)
def unpickle(file): #The function “unpickle” is used to load and deserialize data from a file.
    with open(file, 'rb') as fo: #This line opens the specified file (file) in binary read mode ('rb'), assigning it to the variable fo.
        data = pickle.load(fo, encoding='bytes') #The pickle module loads data from the opened file (fo) and deserialize it. The data should be loaded as bytes.
        return data

#Load dataset batch files:
data_batch_1 = unpickle('cifar-10-batches-py/data_batch_1')
data_batch_2 = unpickle('cifar-10-batches-py/data_batch_2')
data_batch_3 = unpickle('cifar-10-batches-py/data_batch_3')
data_batch_4 = unpickle('cifar-10-batches-py/data_batch_4')
data_batch_5 = unpickle('cifar-10-batches-py/data_batch_5')

#Concatenate the data from all batch files into a single dataset
X_train = np.concatenate([ #X_train represents the input features (data)
    data_batch_1[b'data'],
    data_batch_2[b'data'],
    data_batch_3[b'data'],
    data_batch_4[b'data'],
    data_batch_5[b'data'],
])

y_train = np.concatenate([ #y_train represents the corresponding target labels, used for training a ML model
    data_batch_1[b'labels'],
    data_batch_2[b'labels'],
    data_batch_3[b'labels'],
    data_batch_4[b'labels'],
    data_batch_5[b'labels'],
])

label_names = { #Name of category labels
    0: "Aircraft",
    1: "Automobile",
    2: "Bird",
    3: "Cat",
    5: "Dog",
    6: "Frog",
    7: "Horse",
    8: "Ship"
}

#Load the test batch:
test_batch = unpickle('cifar-10-batches-py/test_batch')
X_test = test_batch[b'data']
y_test = np.array(test_batch[b'labels'])

#Reshape the data: (Changing the dimension or structure of data while preserving its content. In this case, the images will be reshaped to display correctly)
X_train = X_train.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)
X_test = X_test.reshape(-1, 3, 32, 32).transpose(0, 2, 3, 1)

#Split the dataset into training and validation sets: 
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42) #use the train_test_split function for splitting with a test size of 20%.

#Display that the dataset extraction was successful:
print("Dataset extracted successfully.")

#Print the shapes of the datasets:
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_val shape:", X_val.shape)
print("y_val shape:", y_val.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

#Display image visualization:
fig, axes = plt.subplots(3, 5, figsize=(12, 6)) #This line creates a figure with a grid of subplots (3 rows, 5 columns) for visualizing images.
                                                #figsize=(12, 6): This specifies the size of the figure in inches. The width of the figure will be 12 inches, and the height will be 6 inches. 
for i, ax in enumerate(axes.flat): # this loop is used to display images and set titles for each subplot in a grid layout. "Flat" flattens the 2D array of axes (axes) into a 1D iterable
    ax.imshow(X_train[i]) #This line displays an image from the training data (X_train) on each subplot (ax) of the figure.
    ax.set_title(f"Label: {y_train[i]}\n{label_names[y_train[i]]}") #This line sets the title of each subplot to display the corresponding label and category name from y_train.
    ax.axis("off") #Turn off the axis labels,leaving only the image to focus solely on the visual content without distraction from the axis markings
plt.tight_layout() #This line adjusts the layout of the subplots to prevent overlapping.
plt.show() #This line displays the visualized images.

#Verify the class labels:
unique_labels = np.unique(y_train) #This line finds and stores the unique class labels present in the training data (y_train).
print("Unique class labels:", unique_labels)

#Explanation of output:

#X_train has a shape of (40000, 32, 32, 3), which means it contains 40,000 images for training. Each image has a size of 32x32 pixels with 3 color channels (RGB).
#y_train has a shape of (40000,), which corresponds to the labels for the 40,000 training images. Each label represents the class/category of the corresponding image in X_train.
#X_val has a shape of (10000, 32, 32, 3), indicating it contains 10,000 images used for validation. The dimensions of each image are the same as in X_train.
#y_val has a shape of (10000,) and contains the corresponding labels for the validation images in X_val.
#X_test has a shape of (10000, 32, 32, 3), representing 10,000 images that are part of the test set. Similar to X_train and X_val, each image in X_test has dimensions of 32x32 pixels with 3 color channels.
#y_test has a shape of (10000,) and provides the labels for the test images in X_test.
#Unique class labels: [0 1 2 3 4 5 6 7 8 9]: As a reminder, in the CIFAR-10 dataset, there are a total of 10 different classes or categories, represented by the numbers 0 to 9.

#This code performs several tasks in the following sequence to handle the CIFAR-10 dataset:

#Extracts the dataset from a compressed file.
#Loads and combines the individual batch files (individual subsets of data within a dataset) into a single dataset for training. The test batch is loaded separately.
#Reshapes the data into the desired format to prepare it for further processing.
#Splits the dataset into training and validation sets.
#Confirms the successful extraction and verifies the shapes of the datasets.
#Visualizations are created to display a subset of the training images along with their labels and category names using matplotlib.
#Prints the unique class labels present in the training dataset