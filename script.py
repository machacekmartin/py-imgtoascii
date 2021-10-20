import sys, cv2, os

SHADES = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
COLOR_MAX = 255
OUTPUT_FOLDER = 'output'
        
def clear_output():
    for file in os.listdir(OUTPUT_FOLDER):
        os.remove(os.path.join(OUTPUT_FOLDER, file))

def resize_image(image, dimensions):
    return cv2.resize(image, dimensions)

def add_text_to_output(text, output_file):
    with open('{}/{}'.format(OUTPUT_FOLDER, output_file), 'w') as file:
        file.write(text)

def convert_image_to_ascii(image):
    ascii = ''
    rows, cols = image.shape

    for row in range(rows):
        for col in range(cols):
            norm = COLOR_MAX / len(SHADES)
            index = image[row][col] / norm
            ascii += SHADES[int(index) - 1] + ' '

        ascii += '\n'
    return ascii

def run():
    clear_output()

    if not os.path.isfile(sys.argv[1]):
        print("This script accepts only one parameter 'input file', which can be either .jpg or an .mp4 file")
    
    file = sys.argv[1]
    filename, extension = os.path.splitext(file)

    if extension == '.jpg':

        image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        resized_image = resize_image(image, (150, 150))

        ascii = convert_image_to_ascii(resized_image)
        add_text_to_output(ascii, 'output')

    if extension == '.mp4':

        video = cv2.VideoCapture(file)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        i = 0
        success, frame = video.read()
        
        while success:
            print('Converting frames.. [', i+1 ,'/' , frame_count ,']')
            grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_image = resize_image(grayscaled, (150, 150))
            ascii = convert_image_to_ascii(resized_image)
            add_text_to_output(ascii, i)

            i += 1
            success, frame = video.read()

run()


