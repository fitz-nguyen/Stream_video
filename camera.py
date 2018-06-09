import cv2


class VideoCamera(object):
    def __init__(self, input):
        print("Camera")
        self.video = cv2.VideoCapture('video.mov')
        self.input = input
        self.gen = input()
        self.temp = cv2.imread('img.png')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = next(self.gen)
        if image is not None:
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()

        ret, jpeg = cv2.imencode('.jpg', self.temp)
        return jpeg.tobytes()
