import PIL
import os
import shutil
import colorama
import argparse
from os import makedirs
from os import chdir
from os import rmdir
from PIL import Image
from shutil import move
from argparse import ArgumentParser

def mainException():
    print('Invalid arguments supplied!')

def androidSizes():
    return {
      'hdpi':'72',
      'mdpi':'48',
      'xhdpi':'96',
      'xxhdpi':'144',
      'xxxhdpi':'192'
    }
def macOSSizes():
    return {
      '1':'16',
      '2':'32',
      '3':'64',
      '4':'128',
      '5':'256',
      '6':'512',
      '7':'1024',
    }
def windowsSizes():
    return {
      '1':'256'
    }

def executeCompile(sourceImage, platform):
    try:
        targetDir = 'dist' + platform
        makedirs(targetDir)
        chdir(targetDir)
        if platform == 'MacOS':
            src = '../' + sourceImage
            myImage = Image.open(src)
            prefix = 'app_icon_'
            for key in macOSSizes():
                size = int(macOSSizes()[key])
                new_image = myImage.resize((size, size))
                newString = prefix + macOSSizes()[key] + '.png'
                new_image.save(newString)
        elif platform == 'Android':
            src = '../' + sourceImage
            myImage = Image.open(src)
            imageName = 'ic_launcher.png'
            for key in androidSizes():
                dir = 'mipmap-' + key
                makedirs(dir)
                os.chdir(dir)
                size = int(androidSizes()[key])
                new_image = myImage.resize((size, size))
                new_image.save(imageName)
                chdir('..')
        elif platform == 'Windows':
            src = '../' + sourceImage
            myImage = Image.open(src)
            for key in windowsSizes():
                size = int(windowsSizes()[key])
                new_image = myImage.resize((size, size))
                newString = 'app_icon.ico'
                new_image.save(newString)
        else:
            pass
        chdir('..')
    except Exception as error:
        print(str(error))

def executeCleanUp():
    dirList = [
      'dist',
      'distAndroid',
      'distMacOS',
      'distWindows',
    ]
    for item in dirList:
        try:
            rmdir(item)
        except Exception as error:
            print(str(error))

def version():
    name = 'Flutter Helper'
    version = '1.0.0'
    author = 'Alexander Abraham'
    license = 'MIT'
    print(name + 'v.' + version)
    print('by ' + author)
    print('Licensed under the ' + license + 'license!')

def cli():
    parser = ArgumentParser()
    parser.add_argument('--version', help='displays version info', action='store_true')
    parser.add_argument('--source', help='the image for which to generate images')
    parser.add_argument('--platform', help='which platform to target')
    parser.add_argument('--clean', help='cleans up the current directory')
    args = parser.parse_args()
    if args.version:
        version()
    elif args.source and args.platform:
        executeCompile(args.source, args.platform)
    elif args.clean:
        executeCleanUp()
    elif args.source:
        try:
            executeCompile(args.source, 'Android')
            executeCompile(args.source, 'MacOS')
            executeCompile(args.source, 'Windows')
            makedirs('dist')
            move('distAndroid', 'dist')
            move('distMacOS', 'dist')
            move('distWindows', 'dist')
        except Exception as error:
            print(str(error))
    else:
        mainException()
def main():
    cli()
if __name__ == '__main__':
    main()
