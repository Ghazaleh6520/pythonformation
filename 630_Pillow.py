from PIL import Image
im = Image.new("RGBA", (1920,180), "#614fc5")
im.show() # image temporaire
im2 = Image.open("img/image.jpg")
im2.show() # image temporaire