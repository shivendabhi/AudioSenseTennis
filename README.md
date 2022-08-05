# Tennis Ball Detector
This is a program that will detect a tennis ball that is in the frame of the camera and highlight it using the DetectNet Object Detection model, making it easier to see. The real world application of this would be using it at real tennis matches, to track and highlight the ball traveling at 60-120 mph across the tennis court. This would it tremendously easier for people with certain visual impairments to have a better viewing experience of tennis in a whole. This is also a very cost effective solution as it will work on already existing cameras at tennis venues, it just needs to be processed in real time and broadcasted on a special channel for the viewers to use. 
![Placeholder](https://img.icons8.com/ios-glyphs/120/1FB141/icons8-new-logo.png)
## The Algorithm
The program utilizes DetectNet, which is a object detection model which is a covolutional neural network. They are especially good at capturing and recognizing patterns in photos. A convolutional neural network is made up of multiple convolutional layers. Each layer is composed of multiple filters that classify one pixel at a time. When on top of one another, they can split the scene into multiple sections of different patterns. By doing so, it is able to localize and pick out specific objects from the scene. The more layers a network has, the more compleicated and specialized objects are able to be detected.

---
## Running the project
1. Make sure git and cmake is installed:
```
sudo apt install git all
sudo apt install cmake
```
2. Clone the "jetson-inference" project into your home folder:
 ```
git clone https://github.com/dusty-nv/jetson-inference
cd jetson-inference
```
3. 
---
#### Video Explanation
[Tennis Ball Detector Program Explanation(placeholder)](youtube.com)
