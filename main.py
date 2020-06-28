import cv2

frame = cv2.imread('/Users/wangzhongxuan/Desktop/xBQqP.jpg')
print(frame)
# cap = cv2.VideoCapture(0)
# while (True):
# Capture frame-by-frame
# ret, frame = cap.read()
h = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)[:,:,0]
ret, thresh = cv2.threshold(h, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25, 25))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Get the countour points
contours, hierarchy = cv2.findContours(cv2.bitwise_not(opening), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

print('The extreme points are leftmost: {}, rightmost: {}, topmost: {} and bottommost: {}'.format(leftmost, rightmost, topmost, bottommost))
img2 = frame.copy()
cv2.circle(img2, leftmost, 5, (0, 255, 255), -1)    #-- leftmost
cv2.circle(img2, rightmost, 5, (0, 255, 255), -1)    #-- rightmost
cv2.circle(img2, topmost, 5, (0, 255, 255), -1)    #-- topmost
cv2.circle(img2, bottommost, 5, (0, 255, 255), -1)    #-- bottommost

    # p1 =
    # p2 =

    # matrix = cv2.getPerspectiveTransform()
    # # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
# cv2.imwrite('frame.jpg', img2)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# if __name__ == '__main__':
#     pass
