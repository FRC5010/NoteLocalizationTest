import cv2
import numpy as np



def main():
    cap = cv2.VideoCapture(0)
    
    upper_bound = np.array([0,0,0])
    lower_bound = np.array([255,255,255])

    def mouseRGB(event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
            colorsH = HSV_frame[y,x,0]
            colorsS = HSV_frame[y,x,1]
            colorsV = HSV_frame[y,x,2]

            if colorsH > upper_bound[0]:
                upper_bound[0] = colorsH

            if colorsH < lower_bound[0]:
                lower_bound[0] = colorsH

            if colorsS > upper_bound[1]:
                upper_bound[1] = colorsS

            if colorsS < lower_bound[1]:
                lower_bound[1] = colorsS

            if colorsV > upper_bound[2]:
                upper_bound[2] = colorsV

            if colorsV < lower_bound[2]:
                lower_bound[2] = colorsV

            

            


            print("Lower Bound: ", lower_bound)
            print("Upper Bound: ", upper_bound)

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouseRGB)

    while True:
        ret, frame = cap.read()

        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_bound_orange = np.array([0, 66, 141])
        upper_bound_orange = np.array([54, 255, 255])






        mask = cv2.inRange(HSV_frame, lower_bound_orange, upper_bound_orange)
        contour = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if not ret:
            print("Unable to capture video")
            break

        cv2.drawContours(frame, contour[0], -1, (0, 255, 0), 3)

        cv2.imshow('frame', frame)
        cv2.imshow('RGB_frame', HSV_frame)
        cv2.imshow('mask', mask)
        


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    


if __name__ == '__main__':
    main()