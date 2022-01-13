import PIL.Image
from PIL.ImageFilter import (
     BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN
)
import sys
import os

class Image:       
    def __init__(self):
        print("Welcome to my ImageModifier Program!")
        print(40*'=')
        self.userDirectory = input("Enter the name of the image file you wish to modify\n")
        img = PIL.Image.open(self.userDirectory)
        img.thumbnail((400,400))
        img.save('thumbnail.jpg')
        img.show()

        self.ModOptions = str(['RESIZE', 'BLUR', 'CONTOUR', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SHARPEN']).lower()
        print(self.ModOptions)
        self.Options()
    
    # def Options(self):
    #     print("The modification options are as follows:\n " + self.ModOptions)
    #     # while True:
    #     #     try:
    #     #         self.selectOpt= input("What kind of modification would you like?\n").lower()
    #     #         if self.selectOpt == 'blur':
        
    # def OptBlur(self):

Image()



# from PIL import Image, ImageFilter

# img.convert('L')


# img = Image.open('astro.jpg')
# img.thumbnail((400,400))
# img.save('thumbnail.jpg')
# img.show()

# crooked = filtered_img.rotate(180)
# crooked.save("grey.png", 'png')
# crooked.show()
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("grey.png", 'png')
# region.show()

