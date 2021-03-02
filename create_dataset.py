import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--img_dir', default='data', help='path to parent folder')
config = parser.parse_args()

classes = os.listdir(config.img_dir)
f = open("dataset.txt", "w")

for clas in classes:
  for image in os.listdir(config.img_dir + '/' + clas):
    f.write('{}/{}'.format(clas,image))
    f.write('\n')