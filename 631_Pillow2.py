from PIL import Image
im = Image.open("img/image.jpg")
im.save("img/imagePNG.png")
im = Image.open("img/imagePNG.png")
im.save("img/image2.jpg") # erreur RGBA possible
im.convert("RGB").save("img/image3.jpg")