import glob
import os
from tqdm import tqdm

def regroup_reds_dataset(train_path, val_path):
    """Regroup original REDS datasets.

    We merge train and validation data into one folder, and separate the
    validation clips in reds_dataset.py.
    There are 240 training clips (starting from 0 to 239),
    so we name the validation clip index starting from 240 to 269 (total 30
    validation clips).

    Args:
        train_path (str): Path to the train folder.
        val_path (str): Path to the validation folder.
    """
    # move the validation data to the train folder
    val_folders = glob.glob(os.path.join(val_path, '*'))
    for folder in tqdm(val_folders):
        new_folder_idx = int(folder.split('/')[-1]) + 240
        os.system(f'cp -r {folder} {os.path.join(train_path, str(new_folder_idx))}')


if __name__ == '__main__':
    # train_sharp
    train_path = 'trainsets/REDS/train_sharp'
    val_path = 'trainsets/REDS/val_sharp'
    print("Regrouping REDS GT dataset...")
    regroup_reds_dataset(train_path, val_path)

    # train_sharp_bicubic
    train_path = 'trainsets/REDS/train_sharp_bicubic/X4'
    val_path = 'trainsets/REDS/val_sharp_bicubic/X4'
    print("Regrouping REDS bicubic dataset...")
    regroup_reds_dataset(train_path, val_path)

    # train_blur (for video deblurring)
    # train_path = 'trainsets/REDS/train_blur'
    # val_path = 'trainsets/REDS/val_blur'
    # regroup_reds_dataset(train_path, val_path)

