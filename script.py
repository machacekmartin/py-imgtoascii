from PIL import Image
import sys

def convert_image():
    SHADES = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    COLOR_MAX = 255

    with Image.open(sys.argv[1]).convert('L') as image:
        image.thumbnail((500,500))
        pixels = image.load()

    with open('output.txt', 'w') as output:
        for row in range(image.height):
            for col in range(image.width):
                norm = COLOR_MAX / len(SHADES)
                index = pixels[col, row] / norm
                output.write(SHADES[int(index) - 1])
                
            output.write('\n')

convert_image()