import glob
from PIL import Image
image_list = []
for filename in glob.glob('img/*.png'):
       im=Image.open(filename)
       image_list.append(im)

a=0
c=[]
weight = 2224
area = (0, 46, 1668, 2174)
for i in range(0,len(image_list)):
       image_list[i] = image_list[i].crop(area)
       c.append(image_list[i])
       c[i].save('img' + str(i) + '.png')