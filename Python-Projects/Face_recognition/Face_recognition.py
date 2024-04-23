#Implement a facial recognition system using the OpenCV and dlib libraries

"""Install Required Libraries
pip install opencv-python-headless
pip install dlib"""

#Import libraries
import cv2
import dlib
from imutils import face_utils
from scipy.spatial import distance as dist

#Load the pre-trained models for face detection and recognition
#Using OpenCV's pre-trained Haar cascade classifier and a face recognition model (face_recognizer) using the dlib library
face_detector = cv2.CascadeClassifier("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Face_recognition/haarcascade_frontalface_default.xml")
face_recognizer = dlib.face_recognition_model_v1("/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Face_recognition/dlib_face_recognition_resnet_model_v1.dat")

#Load sample images for testing the facial recognition system
img1 = cv2.imread('/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Face_recognition/face1.jpg')
img2 = cv2.imread('/Users/Zsuzsi/Documents/GitHub/Python-Projects/Python-Projects/Face_recognition/face2.jpg')

# Detect faces and get face encodings
def get_face_encodings(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convert the input image to grayscale (gray).
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) #Use the face detector to detect faces in the grayscale image (faces).

    face_encodings = []
    for (x, y, w, h) in faces: #Iterate over the detected face bounding boxes ((x, y, w, h)) and perform the following operations for each face:
        # Crop and resize face region
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, (150, 150))  # Resize to 150x150
        face_encoding = face_recognizer.compute_face_descriptor(face)
        face_encodings.append(face_encoding) #Append the computed face encoding to the list of face encodings 

    return face_encodings #Return the list of face encodings

#The code then calls get_face_encodings for both img1 and img2 to obtain their respective face encodings (encodings1 and encodings2).
encodings1 = get_face_encodings(img1)
encodings2 = get_face_encodings(img2)

# Compare face encodings using Euclidean distance
# Check if faces were detected
if not encodings1 or not encodings2:
    print("No faces detected in one or more images.")
else:
    # Compare face encodings and print distances
    for encoding1 in encodings1: 
        for encoding2 in encodings2: #It iterates over the face encodings from both images and calculates the Euclidean distance between each pair of face encodings using scipy.spatial.distance.euclidean.
            distance = dist.euclidean(encoding1, encoding2) #Calculates the Euclidean distance between each pair of face encodings using scipy.spatial.distance.euclidean.
            print('Distance between faces:', distance) #The distances between face encodings are printed as output, indicating the similarity or dissimilarity between the faces in the two images.

# Assume faces1 and faces2 are lists of tuples (x, y, w, h) representing detected faces
faces1 = [(100, 100, 50, 50), (200, 200, 60, 60)]  # Example bounding boxes for faces in img1
faces2 = [(50, 50, 70, 70)]  # Example bounding box for face in img2

# Display images with detected faces
for (x, y, w, h) in faces1:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 2)

for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('Image 1 with Faces', img1)
cv2.imshow('Image 2 with Faces', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
