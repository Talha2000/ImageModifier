from PIL import Image, ImageFilter

img.convert('L')


img = Image.open('astro.jpg')
img.thumbnail((400,400))
img.save('thumbnail.jpg')
img.show()

crooked = filtered_img.rotate(180)
crooked.save("grey.png", 'png')
crooked.show()
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')
region.show()

