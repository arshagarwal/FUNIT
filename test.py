import os
import argparse
import numpy as np

os.system('rm -r K-test')
os.system('rm -r test_output')

parser = argparse.ArgumentParser()
parser.add_argument('--img_dir', default='data', help='path to parent folder')
parser.add_argument('--test_dir', default='test', help='path to test folder')
parser.add_argument('--k', type = int, default = 1, help = 'number of images')
parser.add_argument('--g_ckpt', default = '1.pt', help = 'path to generator checkpoint')

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

#creating output folders
os.mkdir('test_output')
for clas in os.listdir(config.img_dir):
  os.mkdir('test_output/' + clas)

#testing each image

for clas in os.listdir('K-test'):
  for img in os.listdir(config.test_dir):
    os.system('python test_k_shot.py --config configs/train.yaml\
    --ckpt {} --input {}\
    --class_image_folder {} --output {}'.format(
      config.g_ckpt,
      config.test_dir+'/'+img,
      'K-test' + '/' + clas,
      'test_output/' +  clas+ '/'  + img
    ))











