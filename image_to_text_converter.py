from PIL import Image


# Source
IMG = 'pika.jpg'
WIDTH = 105
HEIGHT = 75
OUTPUT = 'pikachu.txt'
# characters used for text construction
ascii_char = list("$a@c%8&j#*/\|()M{}[]r?-_q+~<>!;:,i\"^l`'k.")


def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (255.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    with open(OUTPUT,'w') as f:
        f.write(txt)