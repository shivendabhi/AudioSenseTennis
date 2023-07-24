# AudioSenseTennis
This is a program that will detect a tennis ball that is in the frame of the camera and highlight it using the DetectNet Object Detection model, making it easier to see. The real world application of this would be using it at real tennis matches, to track and highlight the ball traveling at 60-120 mph across the tennis court. This would it tremendously easier for people with certain visual impairments to have a better viewing experience of tennis in a whole. This is also a very cost effective solution as it will work on already existing cameras at tennis event venues, it just needs to be processed in real time and broadcasted on a special channel for the viewers to use. This is currently a work in progress, but in the future, the goal is to have this connected to a generative text model to generate AI commentary on matches as they are going on live.

![tennis-photo](https://user-images.githubusercontent.com/88247327/186822410-5089b3b0-6831-42f0-a353-a062aced1814.png)

## The Algorithm
The program utilizes DetectNet, which is a object detection model which is a convolutional neural network. They are especially good at capturing and recognizing patterns in photos. A convolutional neural network is made up of multiple convolutional layers. Each layer is composed of multiple filters that classify one pixel at a time. When on top of one another, they can split the scene into multiple sections of different patterns. By doing so, it is able to localize and pick out specific objects from the scene. The more layers a network has, the more compleicated and specialized objects are able to be detected.

---
## Running the project
1. Make sure git and cmake is installed:
```
sudo apt install git all
sudo apt install cmake
```
2. Make sure you have Docker installed on your computer
3. Clone the "jetson-inference" project into your home folder:
 ```
git clone https://github.com/dusty-nv/jetson-inference
cd jetson-inference
```
4. Clone this project into the "jetson-inference" folder
```
git clone https://github.com/shivendabhi/tennis-ball-detector
```
5. Run the Docker container and mount the "tennis-ball-detector" folder(If you encounter a runtime error when launching the container, refer to this document to resolve the issue: [Link to Document](https://app.box.com/s/e0dy6dr651h6nxyel4nw81gf5v8a1f3r)
```
docker/run.sh --volume ~/jetson-inference/tennis-ball-detector:/jetson-inference/tennis-ball-detector
```
6. Navigate into the "tennis-ball-detector" folder and run the "tennis-ball_detection.py" script. Make sure that your USB camera is installed under /dev/video0
```
cd tennis-ball-detector
python3 tennis-ball_detection.py
```
At this point, the script will load the model included in the repository that was trained on numerous images of tennis balls(in limited environments). The initial setup for the model may take anywhere from 5-10 minutes, depending on how capable your hardware is. By default, a window will open on the desktop and show a live preview of the camera with the object detection. 

After waiting 10-15 minutes after the script had been run and there is still no camera feed, as well as the desktop being frozen, refer to this document to resolve this issue: [Link to Document](https://app.box.com/s/3n6bezbn6ieadmd8rur0hgsp7eai4no6)

---
### Video Explanation
[Tennis Ball Detector Explanation and Walkthrough](https://youtu.be/OToqQ7yxvfQ)
