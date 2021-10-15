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

def brighter(pixel: tuple, magnitude: int) -> tuple:
    """Increases the brightness of a pixel

    Args:
        pixel: a 3- tuple of (red, green, blue)
            subpixels
        magnitude: an int rom 0-255 that
            indicates how much it increases

    Returns:
        a 3-tuple representing a brighter pixel
    """
    # break down the pixel
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    MAX = 255
    # increase the value by some number
    if red + magnitude > MAX:
        red = MAX
    else:
        red += MAX
    if green + magnitude > MAX:
        green = MAX
    else:
        green += MAX
    if blue + magnitude > MAX:
        blue = MAX
    else:
        blue += MAX
    # return it
    return red, green, blue


# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0) top-left

print(a_pixel)

# Iterate over EVERY PIXEL
image_width = image.width
image_height = image.height

# Top to bottom
for y in range (image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        # print(f"\nPixel Location: {x}, {y}")
    # Print pixel values
    # print(f"red: {pixel[0]}")
    # print(f"green: {pixel[1]}")
    # print(f"blue: {pixel[2]}")


    brighterer_pixel = brighterer_pixel(0, 50)

    # put that in the new image
    output_image.putpixel((x, y), grey_pixel)

output_image.save('brighterer.jpg')
