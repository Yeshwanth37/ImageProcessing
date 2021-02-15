from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)  # Blurs the image
# filtered_img = img.filter(ImageFilter.SMOOTH)  # Smooth the image
# filtered_img = img.filter(ImageFilter.SHARPEN)  # Sharpens the image
# filtered_img = img.convert('L')   # converts the image into  Grey
# rotate = filtered_img.rotate(180)  # rotates the image in angles
# # resize = filtered_img.resize((300,300))  # This is to resize the image
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('rotate.png', 'png')   The above 3 code lines are used to resize the picture
img.thumbnail((400,400))
img.save('thumbnail.jpg')
