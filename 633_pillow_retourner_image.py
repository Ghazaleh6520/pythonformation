from PIL import Image

im = Image.open("img/image.jpg")

# rotation
im.rotate(45, expand=True).save("img/image_rotate.jpg")

# miroir horizontal
im.transpose(Image.FLIP_LEFT_RIGHT).save("img/image_flip.jpg")