from PIL import Image

FILENAME = ("new_outroteste_pillow.png", "PNG")

pillow_obj = Image.open("outroteste_pillow.png")
pixel_set = pillow_obj.load()
width = pillow_obj.width
height = pillow_obj.height

for row in range(height // 2):
    for col in range(width // 2):
        r, g, b = pixel_set[col, row]
        pixel_set[col, row] = (b, g, r)
        pixel_set[rev_col, rev_row] = (b, g, r)

pillow_obj.save(*FILENAME)