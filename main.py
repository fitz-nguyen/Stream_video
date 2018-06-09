from server import StreamingSever
from input import gen_image


if __name__ == "__main__":
    app = StreamingSever(gen_image)
    app.run()
