from PIL import Image

# convert png to bitmap
img = Image.open('images/Goodstuff-No-Nonsense-Free-Space-Space-shuttle.512.png')
img = img.resize((50,50))
img = img.rotate(90)
img.save('images/ship.bmp')