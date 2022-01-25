from multiprocessing.shared_memory import ShareableList
from xml.etree.ElementTree import PI
import PIL.Image
from PIL.ImageFilter import (
     BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
     EMBOSS, FIND_EDGES, SHARPEN, SMOOTH
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
            elif self.selectOpt == 'detail':
                self.Optdetail()
            elif self.selectOpt == 'edge_enhance':
                self.OptEdge1()
            elif self.selectOpt == 'edge_enhance_more':
                self.OptEdge2()
            elif self.selectOpt == 'emboss':
                self.OptEmboss()
            elif self.selectOpt== 'find_edges':
                self.Opt_FindEdges()
            elif self.selectOpt == 'sharpen':
                self.OptSharp()

    def OptResize(self):
        imgSizeA, imgSizeB = [int(x) for x in input("Enter the size you would like to resize to. For Example, '100,100'").split(',')]
        img = PIL.Image.open(self.userDirectory)
        img.thumbnail((imgSizeA, imgSizeB))
        img.save('test.jpg')
        img.show()

    def OptBlur(self):
        # imgSizeA, imgSizeB = [int(x) for x in input("Enter the size you would like to resize to. For Example, '100,100'").split(',')]
        # img = PIL.Image.open(self.userDirectory)
        # img.thumbnail((imgSizeA, imgSizeB))
        # img.save('test.jpg')
        # img.show()
        # print("Blur")
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(BLUR)
        newImg.save('testBlur.jpg')
        newImg.show()

    def OptContour(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(CONTOUR)
        newImg.save('contourTest.jpg')
        newImg.show()

    def Optdetail(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(DETAIL)
        newImg.save('detailTest.jpg')
        newImg.show()

    def OptEdge1(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(EDGE_ENHANCE)
        newImg.save('edge1_Test.jpg')
        newImg.show()

    def OptEdge2(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(EDGE_ENHANCE_MORE)
        newImg.save('edge2_Test.jpg')
        newImg.show()

    def OptEmboss(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(EMBOSS)
        newImg.save('embossTest.jpg')
        newImg.show()

    def Opt_FindEdges(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(FIND_EDGES)
        newImg.save('FindEdges_Test.jpg')
        newImg.show()

    def OptSharp(self):
        img = PIL.Image.open(self.userDirectory)
        newImg = img.filter(SHARPEN)
        newImg.save('SharpTest.jpg')
        newImg.show()


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

