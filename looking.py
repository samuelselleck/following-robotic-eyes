import serial
import time
import cv2

debug = False

def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1, write_timeout = 0)
video_capture = cv2.VideoCapture(0)

# Loading the required haar-cascade xml classifier file, classifies face from non face
haar_cascade = cv2.CascadeClassifier('face_recognition.xml')
while True:
    # Capture frame-by-frame
    start_time = time.process_time()
    ret, img = video_capture.read()

    # Converting image to grayscale, detection model sees it as grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_time = time.process_time()
    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.2, 9)
    detect_time = time.process_time()
    # Iterating through rectangles of detected faces, displaying the rectangle
    if len(faces_rect) > 0:
        (x, y, w, h) = faces_rect[0]
        if debug:
            cv2.rectangle(img, (x, y), (x+w, y+h), (70, 0, 255), 2)
        eye_x, eye_y = x + w/2, y + h/2
        angle_x = clamp(round((eye_x/gray_img.shape[1] - 0.5)*2*-90*1.5 + 90), 0, 180)
        angle_y = clamp(round((eye_y/gray_img.shape[0] - 0.5)*2*90*1.5 + 90), 0, 180)
        if debug:
            print("-------")
            print("x-ang:", angle_x)
            print("y-ang:", angle_y)
        out = angle_x.to_bytes(1, "big") +  angle_y.to_bytes(1, "big")
        ser.write(out)

    signal_time = time.process_time()
    # Display the resulting frame
    if debug:
        cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    end_time = time.process_time()
    if debug:
        print("----------------------")
        print("img aquisition:", img_time - start_time)
        print("cascate detect time:", detect_time - img_time)
        print("send time:", signal_time - detect_time)
        print("end time:", end_time - signal_time)
    time.sleep(0.05)

video_capture.release()
cv2.destroyAllWindows()

