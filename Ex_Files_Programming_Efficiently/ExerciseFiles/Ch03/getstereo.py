import io
import base64

import requests
import bs4
import PIL.Image
import PIL.ImageOps
import PIL.ImageEnhance

def getstereo(date):
    # get SDO index for date, find all 512x512 171-angstrom images 
    indexreq = requests.get(f'https://sdo.gsfc.nasa.gov/assets/img/browse/{date}')
    soup = bs4.BeautifulSoup(indexreq.content, 'lxml')
    filenames = [link.string for link in soup.pre.find_all('a')
                             if link.string.endswith('512_0171.jpg')]
    
    # get two images across the day
    images = []
    # note integer division in case there's an odd number
    for filename in [filenames[0], filenames[len(filenames)//2]]:
        imagereq = requests.get(f'https://sdo.gsfc.nasa.gov/assets/img/browse/{date}/{filename}')
        images.append(PIL.Image.open(io.BytesIO(imagereq.content)))
    
    # grayscale + colorize the two images
    red  = PIL.ImageOps.colorize(images[0].convert('L'), (0,0,0), (255,0,0))
    cyan = PIL.ImageOps.colorize(images[1].convert('L'), (0,0,0), (0,255,255))

    # blend and adjust brightness
    blend = PIL.Image.blend(red, cyan, 0.5)
    final = PIL.ImageEnhance.Brightness(blend).enhance(2.5)
    
    return final

def makebase64(img):
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')

    b64image = base64.b64encode(buffer.getvalue()).decode('ascii')

    return f'<img src="data:image/png;base64,{b64image}"/>'

def getcached(date):
    soup = bs4.BeautifulSoup(open('cached/index_20160509.html'), 'lxml')
    filenames = [link.string for link in soup.pre.find_all('a')
                             if link.string.endswith('512_0171.jpg')]
    
    images = []
    for filename in [filenames[0], filenames[len(filenames)//2]]:
        images.append(PIL.Image.open(f'cached/{filename}'))

    red  = PIL.ImageOps.colorize(images[0].convert('L'), (0,0,0), (255,0,0))
    cyan = PIL.ImageOps.colorize(images[1].convert('L'), (0,0,0), (0,255,255))

    blend = PIL.Image.blend(red, cyan, 0.5)
    final = PIL.ImageEnhance.Brightness(blend).enhance(2.5)
    
    return final
