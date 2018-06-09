from setuptools import setup, find_packages

setup(
    name='stream_server',
    version='0.1',
    description='The stream server',
    license='MIT',
    home="src",
    packages=["stream_server"],
    package_dir={'stream_server': 'src/stream_server'},
    zip_safe=False
)
