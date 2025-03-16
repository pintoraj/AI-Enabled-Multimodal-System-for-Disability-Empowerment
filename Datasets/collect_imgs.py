import os  # Module for file and directory operations
import cv2  # OpenCV for computer vision tasks

# Define the directory where data will be stored
DATA_DIR = '../data'

# Check if the folder 'data' exists. If not, create it.
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Number of classes (e.g., 30 different hand gestures or objects)
number_of_classes = 30

# Number of images to capture for each class
dataset_size = 100

# Initialize the webcam (0 refers to the default camera)
cap = cv2.VideoCapture(0)

# Iterate through each class (0 to 29)
for j in range(number_of_classes):
    # Create a folder for each class if it doesn't already exist
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    # Display 'Ready?' message to indicate the user should prepare
    done = False  # Control flag for the loop
    while True:
        ret, frame = cap.read()  # Capture the current frame from the webcam

        # Display text overlay prompting the user to press 'Q' to start
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        cv2.imshow('frame', frame)  # Display the current video frame

        # Wait for user input; exit the loop if 'Q' is pressed
        if cv2.waitKey(25) == ord('q'):
            break

    # Image collection loop for the current class
    counter = 0  # Counter to track number of images captured
    while counter < dataset_size:
        ret, frame = cap.read()  # Capture frame by frame
        cv2.imshow('frame', frame)  # Display the current frame
        cv2.waitKey(25)  # Delay for smooth capturing

        # Save the captured frame as an image file in the respective class folder
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1  # Increment the counter for each saved image

# Release the webcam resource and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()