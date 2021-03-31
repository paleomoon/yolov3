import os, sys
import shutil
import random
from tqdm import tqdm

ratio = 0.1

set_list=['train', 'val', 'test']

def pick_part(sets, src_path, dst_path):
    image_src_path = '%s/images/%s'%(src_path, sets)
    image_dst_path = '%s/images/%s'%(dst_path, sets)

    label_src_path = '%s/labels/%s'%(src_path, sets)
    label_dst_path = '%s/labels/%s'%(dst_path, sets)

    image_lists = os.listdir(image_src_path)
    random.shuffle(image_lists)
    n_total = len(image_lists)
    n_pick = int(n_total * ratio)
    for fname in image_lists[:n_pick]:
        image_full_src_path = os.path.join(image_src_path, fname)
        image_full_dst_path = os.path.join(image_dst_path, fname)
        shutil.copyfile(image_full_src_path, image_full_dst_path)
        print('copying %s to %s'%(image_full_src_path, image_full_dst_path))

        name = os.path.splitext(fname)[0]
        label_full_src_path = os.path.join(label_src_path, name + '.txt')
        label_full_dst_path = os.path.join(label_dst_path, name + '.txt')
        shutil.copyfile(label_full_src_path, label_full_dst_path)
        print('copying %s to %s'%(label_full_src_path, label_full_dst_path))


if __name__ == "__main__":
    for sets in set_list:
        src_path = './SHWD'
        dst_path = './SHWDs'

        pick_part(sets, src_path, dst_path)
