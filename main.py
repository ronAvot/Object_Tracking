#Ron Avot 308245190

import cv2 as cv

# Capture the video on project folder
vid = cv.VideoCapture('SQUASH.mp4')

# creating MOG2 bg subtractor with 500 frames in cache and shadow detection
sub = cv.createBackgroundSubtractorMOG2(history=500, detectShadows=True)

# Check if everything is ok
while (vid.isOpened):

    # if ret is true than no error with cap.isOpened
    ret, frame = vid.read()

    if ret == True:

        # apply background subtractor and set it into the sub_mask
        sub_mask = sub.apply(frame)

        # finding external contours
        (im2, contours, hierarchy) = cv.findContours(sub_mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        # check for contours which greater than 500
        for contour in contours:
            if cv.contourArea(contour) < 500:
                continue

            # get bounding box from contour
            (x, y, w, h) = cv.boundingRect(contour)

            # draw bounding box
            cv.rectangle(frame, (x, y), (x + w - 1, y + h - 1), (0, 0, 255),2,1)

        #show the background subtraction - GMO2
        cv.imshow('background subtraction', sub_mask)

        #show the results frame with the bounding box
        cv.imshow('Frame', frame)

        # Exit if ESC pressed
        k = cv.waitKey(1) & 0xff
        if k == 27: break

    #Video finished
    else:
        break


# realese video and cv
vid.release()
cv.destroyAllWindows()

