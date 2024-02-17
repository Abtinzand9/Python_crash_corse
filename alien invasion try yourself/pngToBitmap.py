from PIL import Image

# convert png to bitmap
img = Image.open('images/photo_2024-02-17_11-59-20.png')
img = img.resize((50,50))
img = img.rotate(90)
img.save('images/alien.bmp')