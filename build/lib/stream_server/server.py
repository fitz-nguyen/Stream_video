#!/usr/bin/env python
from flask import Flask, Response, url_for
import cv2


def bootstrap(app):
    @app.route('/')
    def index():
        template = """
        <html>
          <head>
            <title>Video Streaming Demonstration</title>
          </head>
          <body>
            <h1>Video Streaming Demonstration</h1>
            <img id="bg" src="{}">
          </body>
        </html>"""
        return template.format(url_for('video_feed'))

    def gen(source):
        gen = source()
        while True:
            frame = next(gen)
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    @app.route('/video_feed')
    def video_feed():
        return Response(gen(app.source_frame),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


class StreamingSever(Flask):
    def __init__(self, input):
        super(StreamingSever, self).__init__(__name__)
        self.source_frame = input
        bootstrap(self)
