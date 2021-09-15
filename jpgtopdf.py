from PIL import Image

imagecover = Image.open(r'/Users/cihat.s.ersoz/Documents/WEB/A1/1.COVER.jpeg')

imglist = []

for x in range(10):
    x += 12
    imglist.append ("image" + str(x) + " = " + "Image.open(r'/Users/cihat.s.ersoz/Documents/WEB/A1/" + str(x) +".jpg')")
    #("image" + str(x) + " = " + "Image.open(r'/Users/cihat.s.ersoz/Documents/WEB/A1/" + str(x) +".jpg')")

imagecover.save(r'/Users/cihat.s.ersoz/Documents/WEB/A1/a1deneme.pdf',save_all=True, append_images=imglist)