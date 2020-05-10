from PIL import Image
import math


def divider(a, b):
    s = []
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            s.append(i)
    s.append(a)
    for j in range(2, int(math.sqrt(b) + 1)):
        if b % j == 0 and (j in s):
            return j


for image in 'filename':
    im = Image.open(image)
    x, y = im.size
    k = divider(x, y)
    x1 = x // k
    y1 = y // k
    f = x1 * y1
    for i in range(x1):
        for j in range(y1):
            if i != x1 and j != y1:
                im.crop(box=(x / x1 * i, y / y1 * j, x / x1 * (i + 1) - 1, y / y1 * (j + 1) - 1)). \
                    save('im{}{}.jpeg'.format(str(i + 1), str(j + 1)))
for i in 'filename':
    im = Image.open(i)
    im2 = im.resize((150, 150))
    im2.save(str(i) + 'resize')

