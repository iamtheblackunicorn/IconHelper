# ICON HELPER :hammer:

*A tool to help you generate all the different icon sets you need for a Flutter application. :hammer:*

## About :books:

I always hated generating different app icons of different sizes for different platforms manually using Photoshop. So, I decided to automate that process.
This tool, written in Python, my native language, lets you do just that. Currently supported platforms for generation of icon sets are:

- Mac OSX
- Android
- Windows

## Usage :pick:

Make sure you have the following installed:

- Python 3+
- Pillow for Python 3+
- Git

1.) Download the tool from [here]().
2.) Take an icon you have created for your Flutter app. (Should be square and a `*.png` image.)
3.) Place the tool and your base image in the same directory.
4.) Run one of these commands according to what you want to do:
  - Generate icons for a Mac OSX application:
  ```bash
  $ python iconhelper.py --source mypng.png --platform MacOS
  ```
  - Generate icons for an Android application:
  ```bash
  $ python iconhelper.py --source mypng.png --platform Android
  ```
  - Generate icons for a Windows application:
  ```bash
  $ python iconhelper.py --source mypng.png --platform Windows
  ```
5.) Place the generated directory's icons in the place where they should be for the correct platform. The result directory's name will be of the format `dist<Platform>`.
6.) Enjoy! :)

## Contributing :book:

If you want to contribute, you are more than welcome to. Just a file a Pull Request and I will review it.
