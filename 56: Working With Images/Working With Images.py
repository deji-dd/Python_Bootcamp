from PIL import Image

mac = Image.open('example.jpg')
pencils = Image.open('pencils.jpg')
x = 0
y = 1100
w = 1950/3
h = 1300
pencils.crop((x, y, w, h))
halfway = 1993/2
x1 = halfway - 200
w1 = halfway + 200
y1 = 800
h1 = 1257
computer = mac.crop((x1, y1, w1, h1))
mac.paste(im=computer, box=(0, 0))  # to paste an image onto another image
mac = mac.resize((3000, 500))
mac = mac.rotate(180)
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
red.putalpha(128)
