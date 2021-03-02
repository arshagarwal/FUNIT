import os
import argparse
import numpy as np

os.system('rm -r K-test')
parser = argparse.ArgumentParser()
parser.add_argument('--img_dir', default='data', help='path to parent folder')
parser.add_argument('--test_dir', default='test', help='path to test folder')
parser.add_argument('--k', type = int, default = 1, help = 'number of images')

config = parser.parse_args()
os.mkdir('K-test')

#creating folders containing k test images
for clas in os.listdir(config.img_dir):
  os.mkdir('K-test/' + clas)
  images = os.listdir(config.img_dir + '/' + clas)
  images = np.array(images)[:config.k]
  np.random.shuffle(images)
  for img in images:
    src = '{}/{}/{}'.format(config.img_dir,clas,img)
    dest = 'K-test/' + clas
    os.system('cp {} {}'.format(src,dest))

