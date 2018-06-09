#!/usr/bin/env python
from flask import Flask, render_template, Response
from camera import VideoCamera


def bootstrap(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    def gen(camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    @app.route('/video_feed')
    def video_feed():
        video = VideoCamera(app.input)
        return Response(gen(video),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


class StreamingSever(Flask):
    def __init__(self, input):
        super(StreamingSever, self).__init__(__name__)
        self.input = input
        bootstrap(self)
