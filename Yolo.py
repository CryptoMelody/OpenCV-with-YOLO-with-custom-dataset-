import cv2
import numpy as np
import urllib.request
 
url = 'http://192.168.8.10/cam-hi.jpg'
 
# Use raw strings for Windows paths (prepend 'r' or use double backslashes)
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3

# Method 1: Raw strings (preferred for Windows paths)
classesfile = r"D:\obj.names"
modelConfig = r"D:\yolov4-obj.cfg"
modelWeights = r"D:\yolov4-obj_last.weights"

# Method 2: Double backslashes (also works)
# classesfile = "D:\\obj.names"
# modelConfig = "D:\\yolov4-obj.cfg"
# modelWeights = "D:\\yolov4-obj_last.weights"

classNames = []
with open(classesfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
 
net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObject(outputs, im):
    hT, wT, cT = im.shape
    bbox = []
    classIds = []
    confs = []
    found_cat = False
    found_bird = False
    
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
    
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    
    # Handle different return types of NMSBoxes
    if len(indices) > 0:
        # In newer OpenCV versions, indices is a tuple or array
        if isinstance(indices, tuple):
            indices = indices[0]
        
        for i in indices:
            # Handle whether i is a scalar or array
            if isinstance(i, (list, np.ndarray)):
                idx = i[0]
            else:
                idx = i
                
            box = bbox[idx]
            x, y, w, h = box[0], box[1], box[2], box[3]
            
            if classNames[classIds[idx]] == 'bird':
                found_bird = True
            elif classNames[classIds[idx]] == 'cat':
                found_cat = True
            
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(im, f'{classNames[classIds[idx]].upper()} {int(confs[idx] * 100)}%',
                       (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    
    return found_cat, found_bird

while True:
    try:
        # Use urllib to get image from URL
        img_resp = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        im = cv2.imdecode(imgnp, -1)
        
        # Alternative: Use VideoCapture if you prefer
        # cap = cv2.VideoCapture(url)
        # success, im = cap.read()
        # if not success:
        #     print("Failed to grab frame")
        #     continue
        
        # Create blob and perform detection
        blob = cv2.dnn.blobFromImage(im, 1/255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        
        # Get output layer names - FIXED VERSION
        layerNames = net.getLayerNames()
        
        # Handle different OpenCV versions
        unconnected_out_layers = net.getUnconnectedOutLayers()
        
        # Check the type of unconnected_out_layers
        if unconnected_out_layers.ndim == 1:
            # OpenCV 4.x: returns array of indices
            outputNames = [layerNames[i - 1] for i in unconnected_out_layers]
        else:
            # OpenCV 3.x: returns array of arrays
            outputNames = [layerNames[i[0] - 1] for i in unconnected_out_layers]
        
        outputs = net.forward(outputNames)
        
        # Find objects
        found_cat, found_bird = findObject(outputs, im)
        
        # Display result
        cv2.imshow('Image', im)
        
        # Check for quit key
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):  # ESC or 'q' to quit
            break
            
    except Exception as e:
        print(f"Error: {e}")
        # Wait a bit before retrying
        cv2.waitKey(1000)

cv2.destroyAllWindows()
