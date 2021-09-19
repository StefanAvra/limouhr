from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# config
filename = 'footer.png'
FONT_SIZE = 62
IMAGE_SIZE = (916, 48)
RESIZE_X = 0.5
RESIZE_Y = 15


def get_weird_timestamp():
    print(datetime.now())
    fnt = ImageFont.truetype('./OCRB Regular.ttf', FONT_SIZE)

    image = Image.new(mode="1", size=IMAGE_SIZE, color="white")
    draw = ImageDraw.Draw(image)
    text = f'({datetime.now().strftime("%d.%m.%Y/%H:%M:%S")})'
    draw.text((-12, -4), text, font=fnt, fill=(0))
    image = image.resize(
        (round(image.size[0]*RESIZE_X), round(image.size[1]*RESIZE_Y)))
    return image


# get_weird_timestamp().save(filename)
