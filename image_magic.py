# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

def to_greyscale(pixel: tuple, algo= str) -> tuple:
    """Convert a pixel to greyscale
    Can also specify the greyscale algorithm
    Defaults to average

    Args:
        pixel: a 3-tuple of ints from
            0 - 225, e.a (140,120,255)
            represents (red, green, blue)
        algo: the greyscale conversion algorithm
        specified by the user
        valid values are "average", "luma"
        defaults to "average"

    Returns:
         a 3-tuple pixel (r, g, b) in
         greyscale
    """
    # grab r, g, b
    red, green, blue = pixel

    # calculate the grey pixel
    if algo.lower() == "luma":
        grey = int(red * 0.3 + green * 0,59 + blue * 0.11)
    else:
        grey = int((red + green + blue) / 3)

    return grey, grey, grey


def to_greyscale_luma(pixel: tuple) -> tuple:
    """Convert to using luma algorithm

     Args:
        pixel: a 3-tuple of ints from
            0 - 225, e.a (140,120,255)
            represents (red, green, blue)

    Returns:
         a 3-tuple pixel (r, g, b) in
         greyscale
    """
    red, green, blue = pixel
    grey = int(red * 0.3 + green * 0.59 + blue * 0.11)
    return grey, grey, grey

def brightness(pixel: tuple, magnitude: int) -> tuple:
    """Increases the brightness of a pixel

    Args:
        pixel: a 3- tuple of (red, green, blue)
            subpixels
        magnitude: an int rom -255 to +255 that
            indicates how much it increases

    Returns:
        a 3-tuple representing a brighter pixel
    """
    # break down the pixel
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    MAX = 255
    MIN = 0

    # add the magnitude to the r, g, b values
    if red + magnitude > MAX:
        red = MAX
    elif red + magnitude < MIN:
        red = MIN
    else:
        red += magnitude

    if green + magnitude > MAX:
        green = MAX
    elif green + magnitude < MIN:
        green = MIN
    else:
        green += magnitude

    if blue + magnitude > MAX:
        blue = MAX
    elif blue + magnitude < MIN:
        blue = MIN
    else:
        blue += magnitude

    # return it
    return red, green, blue


