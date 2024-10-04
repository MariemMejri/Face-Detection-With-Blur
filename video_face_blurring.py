import os
import cv2
import mediapipe as mp





# open cap
cap = cv2.VideoCapture(0)


while True:
  ret, frame = cap.read()
  


  H ,W , _ = frame.shape
  
  # detect face 
  
  mp_face_detection = mp.solutions.face_detection
  
  with mp_face_detection.FaceDetection(model_selection=0,min_detection_confidence=0.5)as face_detection:
    img_rgb= cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
  
    if out.detections is not None:
      for detection in out.detections:
        location_data=detection.location_data
        bbox = location_data.relative_bounding_box
      
              # Convert the relative bounding box coordinates to pixel coordinates (for resized image)
        x1 = int(bbox.xmin * W)
        y1 = int(bbox.ymin * H)
        w = int(bbox.width * W)
        h = int(bbox.height * H)
        # Draw the bounding box on the resized image
        frame[y1:y1+h,x1:x1+w,:]=cv2.blur(frame[y1:y1+h,x1:x1+w,:],(50,50))
      # Display the resized image
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
      break
cap.release()

cv2.destroyAllWindows()

#image_path = 'input/asarra.jpg'
#img = cv2.imread(image_path)

