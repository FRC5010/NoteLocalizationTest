import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)

    upper_bound = np.array([0, 0, 0])
    lower_bound = np.array([255, 255, 255])

    def mouseRGB(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # checks mouse left button down condition
            colorsH = HSV_frame[y, x, 0]
            colorsS = HSV_frame[y, x, 1]
            colorsV = HSV_frame[y, x, 2]

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

    cv2.namedWindow("frame")
    cv2.setMouseCallback("frame", mouseRGB)

    while True:
        ret, frame = cap.read()

        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        GRAY_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        BLUR_frame = cv2.blur(GRAY_frame, (3, 3))

        lower_bound_orange = np.array([0, 50, 130])
        upper_bound_orange = np.array([179, 162, 255])

        mask = cv2.inRange(HSV_frame, lower_bound_orange, upper_bound_orange)
        edges = cv2.Canny(mask, 100, 200)

        if not ret:
            print("Unable to capture video")
            break

        if circles is not None:
            # Convert the circle parameters a, b and r to integers.
            circles = np.uint16(np.around(circles))

            for pt in circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circumference of the circle.
                cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

        cv2.imshow("frame", frame)
        cv2.imshow("RGB_frame", HSV_frame)
        cv2.imshow("mask", mask)
        cv2.imshow("edges", edges)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
