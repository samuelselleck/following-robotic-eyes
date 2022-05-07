import serial
import time
import cv2
from mtcnn.mtcnn import MTCNN
debug_camera = True

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
video_capture = cv2.VideoCapture(0)

detector = MTCNN()

while True:
    # Capture frame-by-frame
    ret, img = video_capture.read()

    # Converting image to grayscale, detection model sees it as grayscale
    faces = detector.detect_faces(img)
    for face in faces:
        print(face)
    # Applying the face detection method on the grayscale image
    #faces_rect = haar_cascade.detectMultiScale(gray_img, 1.2, 9)
    # Iterating through rectangles of detected faces, displaying the rectangle
    #for (x, y, w, h) in faces_rect:
    #    if debug_camera:
    #        cv2.rectangle(img, (x, y), (x+w, y+h), (70, 0, 255), 2)
    #    eye_x, eye_y = x + w/2, y + h/2
    #    angle = round((eye_x/gray_img.shape[1] - 0.5)*-90 + 90)
    #    cmd = f'0 {angle}\n'
    #    ser.write(cmd.encode())


    # Display the resulting frame
    if debug_camera:
        cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

#for i in range(10):
#	angle = i*18
#	cmd = f'0 {angle}\n'
#	ser.write(cmd.encode())
#	print(cmd)
#	time.sleep(0.5)
