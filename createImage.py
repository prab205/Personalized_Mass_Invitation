import os
from PIL import Image, ImageDraw, ImageFont

def createInvitationCard(srcImg, text, destImg=None, cordinates=(None, None), color=(0,0,0), fontPath=None, fontSize=50, display=False):
    try:
        img = Image.open(srcImg)
    except:
        print("Image couldnot be loaded successfully.\nPlease check the provided path and name.\nInclude file extension as well")
        return

    if destImg:
        imgName = f'./images/{destImg}'
    else:
        imgName = './images/interimage.png'

    if not os.path.isdir('images'):
        os.mkdir('images')

    if os.path.exists(imgName):
        print(f"{imgName} already exists. Exiting without proceeding further.")
        exit(-1)

    editableImage = ImageDraw.Draw(img)
    imgName = imgName

    if fontPath:
        #loads the font as well as the fontsize if font is provided by user
        fontVar = ImageFont.truetype(fontPath, fontSize)

        #if any one cordinate is missing, then centers text at that cordinate.
        if cordinates[0] and cordinates[1]:
            editableImage.text((cordinates[0], cordinates[1]), text,  fill=color, font=fontVar)
            img.save(imgName)
        elif cordinates[1]:
            W,_ = img.size
            w,_ = fontVar.getsize(text)
            editableImage.text(((W-w)/2, cordinates[1]), text,  fill=color, font=fontVar)
            img.save(imgName)
        elif cordinates[0]:
            _,H = img.size
            _,h = fontVar.getsize(text)
            editableImage.text((cordinates[0], (H-h)/2), text,  fill=color, font=fontVar)
            img.save(imgName)
        else:
            editableImage.text((0,0), text,  fill=color, font=fontVar)
            img.save(imgName)

    else:
        if cordinates[0] and cordinates[1]:
            editableImage.text((cordinates[0], cordinates[1]), text,  fill=color)
            img.save(imgName)
        elif cordinates[1]:
            W,_ = img.size
            w,_ = editableImage.textsize(text)
            editableImage.text(((W-w)/2, cordinates[1]), text,  fill=color)
            img.save(imgName)
        elif cordinates[0]:
            _,H = img.size
            _,h = editableImage.textsize(text)
            editableImage.text((cordinates[0], (H-h)/2), text,  fill=color)
            img.save(imgName)
        else:
            editableImage.text((0,0), text,  fill=color)
            img.save(imgName)

    if display:
        img.show()
    
    return imgName
