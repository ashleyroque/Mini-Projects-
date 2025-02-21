import imageio.v3 as iio


filenames = ['aespa-pic1.jpg', 'aespa-pic2.jpg', 'aespa-pic3.jpg']


images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('aespa.gif', images, duration = 500, loop = 0)