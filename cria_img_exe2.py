from PIL import Image
image = Image.open('IMG_2044.jpg')

image.show()
# The file format of the source file.
print(image.format) 
# Output: JPEG
# The pixel format used by the image. Typical values are "1", "L", "RGB", or "CMYK."
print(image.mode) 
# Output: RGB
# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) 
# Output: (1920, 1280)
# Colour palette table, if any.
print(image.palette) 
# Output: None
"""
#Changing Image Type
image = Image.open('teste_pillow.png')
image.save('teste_pillow.jpg')
"""
#Resizing Images
image     = Image.open('IMG_2044.jpg')
new_image = image.resize((400, 400))
new_image.save('teste_pillow2.png')

print(image.size)     # Output: (1920, 1280)
print(new_image.size) # Output: (400, 400)

image = Image.open('IMG_2044.jpg')
image.thumbnail((400, 400))
image.save('teste_pillow3.png')

print(image.size) # Output: (400, 267)