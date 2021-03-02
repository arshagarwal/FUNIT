rm dataset.txt
python create_dataset.py --img_dir 'data/celeba_hq/val'
python train.py --config configs/train.yaml