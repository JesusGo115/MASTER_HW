'''
Filename: hw4.py
Name: Jesus "Chuy" Gomez
Partner: Jonathan Quintero
Date: 4/2/2019
Course: CST205 Multimedia Design and Programming
Description: The following code imports the array of key details about images and creates a website based on images that  you click on to be sent to another page and see the key details about each image.
'''

from flask import Flask, render_template
from PIL import Image
from random import *
from image_info import image_info

app = Flask(__name__)
#Initiates the flask program

def no_repeat_image(array):
    num = randint(0, 9)
    while num in array:
        num = randint(0, 9)
    return num
#This function assigns random values between 0 - 9 to the inserted array

@app.route('/')
def home():
    position = []
    for i in range(3):
        position.append(no_repeat_image(position))
    return render_template('home.html', first_pic = image_info[position[0]], second_pic = image_info[position[1]], third_pic = image_info[position[2]])
#This route is the main page of the website that first shows the first 3 randomized images. The for loop appends 
#the random values to the 'position' array and the 'render_template' function renders the 'home.html' file 
#and inserts the images to the html file.

@app.route('/pictures/<image_id>')
def image(image_id):
    spot = 0
    for position in range(len(image_info)):
        if image_id == image_info[position]['id']:
            spot = position
            break
    im = Image.open("static/" + image_info[spot]['id'] + ".jpg")
    w, h = im.size
    return render_template('image_1.html', image_id = image_info[spot]['id'], chosen_img = image_info[spot], width=w, height=h)
#This route creates the second page of the website that allows the user to see information about the image they
#clicked on. The for loop grabs the index value of the image the user chose and then uses that spot to render the
#width and the height of image, while also rendering the image and the image's id to the 'image_1.html' file.

if __name__ == '__main__':
    app.run(debug = True)
#This function runs and debugs this flask file
