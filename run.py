
import cv2
from server import StreamingSever


def run_server(img_dir):
    def gen_video():
        run = True
        cap = cv2.VideoCapture(img_dir)

        while run:
            ok, frame = cap.read()
            if ok:
                yield frame
            else:
                run = False
                cap.release()

    def gen_image():
        for img in img_dir:
            image = cv2.imread(img)
            yield image

    app = StreamingSever(gen_image)
    app.run()


if __name__ == "__main__":
    run_server(['end.png', 'img.png'])
