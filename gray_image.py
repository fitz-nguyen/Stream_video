import cv2
from server import StreamingSever


def gen_gray_image():
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret:
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            yield gray
        else:
            break

    cap.release()


app = StreamingSever(gen_gray_image)
app.run(host="0.0.0.0", port = "8000", debug=True)
