import PIL.Image
from PIL.ImageFilter import (
     BLUR, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN
)
import sys
import os

class Image:       
    def __init__(self):
        os.system('cls')
        print("Welcome to my ImageModifier Program!")
        print(40*'=')
        self.userDirectory = input("Enter the name of the image file you wish to modify\n")
        self.ModOptions = str(['RESIZE', 'BLUR', 'CONTOUR', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SHARPEN']).lower()
        self.Options()
    
    def Options(self):
        os.system('cls')
        print("The modification options are as follows:\n " + self.ModOptions + "\n\n")
        while True:
            self.selectOpt = input("Choose an Option to apply to the image:\n ")

            if self.selectOpt == "x":
                break
            if self.selectOpt == 'resize':
                self.OptResize()
            elif self.selectOpt == 'blur':
                self.OptBlur()
            elif self.selectOpt == 'contour':
                self.OptContour()
            elif self.selectOpt == 'Edge_enhance':
                self.OptEdge1()
            elif self.selectOpt == 'Edge_enhance_more':
                self.OptEdge2()
            elif self.selectOpt == 'emboss':
                self.OptEmboss()
            elif self.selectOpt== 'find_edges':
                self.OptEdge()
            elif self.selectOpt == 'Sharpen':
                self.OptSharp()

    def OptResize(self):
        img = PIL.Image.open(self.userDirectory)
        img.thumbnail((100,100))
        img.save('test.jpg')
        return img.show()

    def OptBlur(self):
        pass

    def OptContour(self):
        pass

    def OptEdge1(self):
        pass

    def OptEdge2(self):
        pass

    def OptEmboss(self):
        pass

    def OptBlur(self):
        pass

    def OptEdge(self):
        pass

    def OptSharp(self):
        pass


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

