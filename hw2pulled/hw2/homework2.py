"""

Creared by Jonathan J. Quintero Ramos & Jesus 'Chui' Gomez
created 2/23/2019
The following code: will use an image dictionary to then interpret multiple images
and remove the obstructinos, like in this case the motorcylce

"""

#The following modules are required for the code to work
from PIL import Image
import math
import glob

#This is where the images are opened and stored at

image = glob.glob("Images/*.png")
imageDict = []
for i in image:
    imageDict.append(Image.open(i))

"""
imageDict={
        1:Image.open("Images/1.png"),
        2:Image.open("Images/2.png"),
        3:Image.open("/3.png"),
        4:Image.open("forCst/4.png"),
        5:Image.open("forCst/5.png"),
        6:Image.open("forCst/6.png"),
        7:Image.open("forCst/7.png"),
        8:Image.open("forCst/8.png"),
        9:Image.open("forCst/9.png"),
        10:Image.open("forCst/10.png"),
        11:Image.open("forCst/11.png")
}
"""

#Because the same camera was used, the dimensions would be the same
#This is then for convenience
width = imageDict[1].width
height = imageDict[1].height

#The following image is created to then place pixels upon
im = Image.new("RGB",(width, height),"white")

#The following code determines the pixel difference from those given, returns pixel difference 
#The math module is required for this function
def pixelEvaluator(a,b):
    red = math.pow((a[0] - b[0]),2)
    green = math.pow((a[1] - b[1]),2)
    blue = math.pow((a[2] - b[2]),2)
    return math.sqrt(red+green+blue)

#The following function takes in two image files from the dictionary
#it then inputs the pixels whose color distance is less than 30 calling
#the pixelEvaluator function. 
#The image is then saved at "LastImage.png"
def replacer(a,b):
    for x in range(width):
        for y in range(height):
            pixelVal1 = imageDict[a].getpixel((x,y))
            pixelVal2 = imageDict[b].getpixel((x,y))
            if(pixelEvaluator(pixelVal1,pixelVal2) <1):
                im.putpixel((x,y),pixelVal1)

            
    im.save("LastImage.png")


#The following function takes in the images dictionary, it then calls the function
#replacer and inputs two files, making sure that if the function is at a last image 
#file, then the first is called to evaluate with the first and then stops.
def multipleImages():
    for x in range(len(imageDict)):
        #print(x)
        x = int(x)
        y = int(x)
        y+=1
        if(y==len(imageDict)):
            y=0
        replacer(x,y)
        
        
#function called
multipleImages()
#placeholder variable to call and open the image.
mi = Image.open("LastImage.png")
mi.show()

