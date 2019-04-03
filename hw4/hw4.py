from flask import Flask, render_template
from PIL import Image
from random import *
from image_info import image_info

app = Flask(__name__)

def no_repeat_image(array):
    num = randint(0, 9)
    while num in array:
        num = randint(0, 9)
    return num

@app.route('/')
def home():
    position = []
    for i in range(3):
        position.append(no_repeat_image(position))
    return render_template('home.html', first_pic = image_info[position[0]], second_pic = image_info[position[1]], third_pic = image_info[position[2]])

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

if __name__ == '__main__':
    app.run(debug = True)

