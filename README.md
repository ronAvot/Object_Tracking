# Object_Tracking
Python Final Project
Object Tracking final project on Python and Computer vision course.
Libraries:
Opencv2
![alt text](https://firebasestorage.googleapis.com/v0/b/detectad-3314b.appspot.com/o/11.png?alt=media&token=714553b8-9e3d-4a24-819a-995d791df24d)


In this project I focused on “Multiple object track finding algorithms”.
In order to do so we need to use “Background Subtraction”, this will give us the ability to understand which object are on move and which are static.

There are three major types of background subtractions algorithms:
MOG 
Gaussian Mixture-based Background/Foreground Segmentation Algorithm
MOG2
Also a Gaussian Mixture-based Background/Foreground Segmentation Algorithm
GMG
Combines statistical background image estimation and per-pixel Bayesian segmentation
Each tracker algorithm has their own advantages and disadvantages


Code implementation:
1. Grab video file on project folder
2. Use GMO2 background subtractor
3. Apply background subtractor
4. Finding external contours with RETR_EXTERNAL and CHAIN_APPROX_SIMPLE
5. Looping for contours
6. Get bounding box from contour
7. Draw the bounding box 
8. At the end display the results
