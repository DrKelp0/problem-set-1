# Image Magic
# Load an image and manipulate the pixels

from PIL import Image

# Load the image (pumpkin)
image = Image.open('./halloween-unsplash.jpg')

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

        print(f"\nPixel Location: {x}, {y}")
    # Print pixel values
    print(f"red: {pixel[0]}")
    print(f"green: {pixel[1]}")
    print(f"blue: {pixel[2]}")



