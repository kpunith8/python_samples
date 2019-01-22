from PIL import Image

img = Image.open("waterfall.jpg")

# To show the image in image viewer
# img.show()

# get the size of the image, filename and other details
print(img.size, img.filename, img.format_description)

# Cropping an image
top_left = img.crop((0, 0, 400, 600))  # .show()

# copy and paste the image
img.paste(im=top_left, box=(292, 0))

# resize((200,200))

# Transparency, RGB-A
img.putalpha(255)
# img.show()
