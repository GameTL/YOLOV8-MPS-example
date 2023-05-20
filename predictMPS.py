# Importing Libraries
import cv2
from ultralytics import YOLO
import yaml
import time

# Setup



# Camera Config
[X_RESOLUTION, Y_RESOLUTION, VIDEO_FPS] = [1280, 720, 30]
cap = cv2.VideoCapture(0)
cap.set(3, X_RESOLUTION)
cap.set(4, Y_RESOLUTION)
cap.set(5, VIDEO_FPS)

# Load the dataset names
try:
    with open("ultralytics/yolo/data/datasets/coco8-seg.yaml", "r") as stream:
            datasets = yaml.safe_load(stream)
            datasets_names = datasets['names']
except:
        print("No file found")
        datasets_names = ""

# Load the model
model = YOLO('yolov8s.pt') # load an official model


# main loop
try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error")
            continue
        
        # Starts the timer for the fps counter
        start = time.time()

        #-----------------
        # results = model(source=image,device="cpu",conf=0.6)
        results = model(source=frame,device="mps",conf=0.6)
        #-----------------
        
        # Print FPS on the frame
        cv2.putText(frame, "fps: " + str(round(1 / (time.time() - start), 2)), (10, int(cap.get(4)) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Print FPS in Terminal
        result_image = results[0].plot()
        print("fps: " + str(round(1 / (time.time() - start), 2)))

        
        
        # show the results
        cv2.imshow("mps_test", result_image)

        # cv2.imshow("cpu_test", result_image)
        if cv2.waitKey(1) == ord("q"):
                cap.release()

except KeyboardInterrupt:
    cap.release()
except Exception as e:
    print(e)
    cap.release()

cv2.destroyAllWindows()