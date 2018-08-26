from PIL import Image

def load_img(filename):
    image = Image.open(filename)
    return image

def show_img(image):
    image.show()

def save_img(image, filename):
    image.save(filename, "jpeg")
    show_img(image)

def sumtuple(tuple):
    total = 0
    for term in tuple:
        total += term
    return total

def obamicon(image):
    lista = image.getdata(band=None)
    listb =[]
    for x in range (0, len(lista)):
        if sumtuple(lista[x])<182:
            listb.append((0,51,76))
        elif sumtuple(lista[x])<364 and sumtuple(lista[x])>=182:
            listb.append((217,26,33))
        elif sumtuple(lista[x])<546 and sumtuple(lista[x])>=364:
            listb.append((112,150,158))
        elif sumtuple(lista[x])>= 546:
            listb.append((252,227,166))
    imagenew = Image.new("RGB",image.size)
    imagenew.putdata(listb)
    return imagenew

def invrainbowfilter(image):
    lista = image.getdata(band=None)
    listb =[]
    for x in range (0, len(lista)):
        if sumtuple(lista[x])<100 and sumtuple(lista[x])>=0:
            listb.append((207, 150, 255))
        elif sumtuple(lista[x])<200 and sumtuple(lista[x])>=100:
            listb.append((60, 139, 242))
        elif sumtuple(lista[x])<300 and sumtuple(lista[x])>=200:
            listb.append((38, 186, 1))
        elif sumtuple(lista[x])<430 and sumtuple(lista[x])>=300:
            listb.append((219, 184, 8))
        elif sumtuple(lista[x])<546 and sumtuple(lista[x])>=430:
            listb.append((188, 104, 1))
        elif sumtuple(lista[x])>= 546:
            listb.append((112, 7, 0))
    imagenew = Image.new("RGB",image.size)
    imagenew.putdata(listb)
    return imagenew

def rainbowfilter(image):
    lista = image.getdata(band=None)
    listb =[]
    for x in range (0, len(lista)):
        if sumtuple(lista[x])<100 and sumtuple(lista[x])>=0:
            listb.append((112, 7, 0))
        elif sumtuple(lista[x])<200 and sumtuple(lista[x])>=100:
            listb.append((188, 104, 1))
        elif sumtuple(lista[x])<300 and sumtuple(lista[x])>=200:
            listb.append((219, 184, 8))
        elif sumtuple(lista[x])<430 and sumtuple(lista[x])>=300:
            listb.append((38, 186, 1))
        elif sumtuple(lista[x])<500 and sumtuple(lista[x])>=430:
            listb.append((1, 94, 17))
        elif sumtuple(lista[x])<600 and sumtuple(lista[x])>=500:
            listb.append((60, 139, 242))
        elif sumtuple(lista[x])>= 600:
            listb.append((207, 150, 255))
    imagenew = Image.new("RGB",image.size)
    imagenew.putdata(listb)
    return imagenew
