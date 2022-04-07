import cv2

cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("../ImageProcessing/haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    if ret:
        faces = detector.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face

            cut = frame[y:y+h, x:x+w]
            fix_face = cv2.resize(cut, (300, 300))
            gray = cv2.cvtColor(fix_face, cv2.COLOR_BGR2GRAY)

        cv2.imshow("My Webcam", frame)
        cv2.imshow("My face", fix_face)
        cv2.imshow("My face grayscale", gray)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
