from PIL import Image

im = Image.open("img/image.jpg")
im = im.convert("RGB")

green = Image.new("RGB", im.size, "#2ea93f")

Image.blend(im, green, 0.7).save("img/image_green.jpg")