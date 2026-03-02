# OpenCV-with-YOLO-with-custom-dataset-

First of all go to this link:

https://colab.research.google.com/drive/12TpSVsA0wexmtaelXzVbU5rxhGLigMKi#scrollTo=KcUKbtO-byOE

"preferably you should watch this video to understand all the lines in this code: https://www.youtube.com/watch?v=mKAEGSxwOAY&list=PLKHYJbyeQ1a3tMm-Wm6YLRzfW1UmwdUIN 

and this videos: https://www.youtube.com/watch?v=10joRJt39Ns&list=PLKHYJbyeQ1a0oGzgRXy-QwAN1tSV4XZxg

https://www.youtube.com/watch?v=mKAEGSxwOAY&list=PLKHYJbyeQ1a3tMm-Wm6YLRzfW1UmwdUIN

Also you can subscribe him on github and download all files from there:

https://github.com/theAIGuysCode/YOLOv4-Cloud-Tutorial/tree/master/yolov4

=================================

U can see that i added some lines in google colab like these:

!apt-get update

!apt-get instadev libtiff-dev libpng-dev

!apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

!apt-get install -y libxvidcore-dev libx264-devll -y build-essential cmake git pkg-config

!apt-get install -y libjpeg-

!apt-get install -y libgtk-3-dev libatlas-base-dev gfortran

!apt-get install -y python3-dev python3-numpy

we use this lines to upgrade our OpenCV libraries!!!! IT'S IMPORTANT TO USE IT!!!!

==================================

!apt-get update

!apt-get install -y build-essential cmake git libopencv-dev

Then we just donwload all essentail libraries for OpenCV

=================================

!cp /content/darknet/cfg/yolov4-custom.cfg /mydrive/yolov4/yolov4-obj.cfg

IN THIS LINE WE HAVE TO PAY ATTENTION TO THIS: /content/darknet/cfg/yolov4-custom.cfg, we have to accessing the file **with absolute path, not by relative path!!!**

The same thing for this line:

!./darknet detector train data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights -dont_show

To train my model i was using Ybat BBOX Annotation Tool:

https://github.com/drainingsun/ybat

**When we send some files to Google disk compress your files like an AI Guy did!**

How to compress file:

1. Create a folder
   
2. Right click on folder
   
3. Choose: Send - Compressed (ZIP)
   
4. Send it to your google disk

**Important information that u should keep in mind while training model !**

1. When you did all things correctly and labeled all bboxes smothly(you don't have a lot of empty space of labled picture in bbox for example) and you have rewritten_bbox 0.000000% everytime - You did't do any mistakes (rewritten_bbox - could increase if your AI model just corrected your not good labeling while it is training )

2.If your loss at the beginning has this kind of numbers: 133.0000000
And after an hour or 30 minutes you have - 0.0000000001 
That can be okay if you have no more than approximately 100-500 images in your training dataset!

3. It's okay to use 100 images! (You don't have to have about 1000 images or more)

4. You have to wait until 1000 irrations will be reached
   
Just after the training you can change thresh in this line and compare the results:   

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights /content/gdrive/MyDrive/yolov4/images/shop.jpg -thresh 0.3
imShow('predictions.jpg')


When you have trained your model and did other things, pay attention to these lines!:

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights /content/gdrive/MyDrive/yolov4/images/**shop.jpg** -thresh 0.3
imShow('**shop.jpg**') - **Incorrect** **⨯**

!./darknet detector test data/obj.data cfg/yolov4-obj.cfg /mydrive/yolov4/backup/yolov4-obj_last.weights /content/gdrive/MyDrive/yolov4/images/**shop.jpg** -thresh 0.3
imShow('**predictions.jpg**') - **Correct**  **🗸**


After getting yolov4-obj_last.weights it's neccerary to use ESP32-AI CAM or another camera to test code on your own computer:

1. Use my .ino code for Esp32-ai cam to create a website where our video will be being streamed

2. Use another code for VISUAL STUDIO to start Yolo_model

3. Enjoy!
    
**Caution**: your camera on ESP-32 can be too slow to detect sth, cause the video is consiststed from a lot of photographs, so that's why it's a little bit difficult for him to be on live (create a website) and take a lot of photographs.


**IF YOU HAVE SOME PROBLEMS WITH DOWNLOADING, YOU CAN DOWNLOAD FROM THIS DOCUMANTATION!**

**What i have in my documantation: yolov4.conv.137, ybat-master.zip (Yolo Bbox Annotation Tool),obj.data, example obj.names, example yolov4-obj_last.weights , generate_test.py, generate_train.py, example test.zip, exapmple images**


