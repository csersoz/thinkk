from PIL import Image


im1 = Image.open("/Users/apple/Desktop/bbd.jpg")
im2 = Image.open("/Users/apple/Desktop/bbd1.jpg")
im3 = Image.open("/Users/apple/Desktop/bbd2.jpg")
im_list = [im2,im3]

pdf1_filename = "/Users/apple/Desktop/bbd1.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list