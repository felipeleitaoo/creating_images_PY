from PIL import Image

pillow_obj = Image.new(mode = "RGB", size = (200, 200),color = (153, 153, 255))
pillow_obj.show()
pillow_obj.save("teste_pillow.png", "PNG")