import random
import os
import numpy as np
import shutil
from shutil import copyfile
# from tqdm import tqdm


def split_data(directory, random_generator, person_ID, lists):
    print("Split Train/Validation/Test Set ...")
    id_orders = random_generator.permutation(51)+1
    n_train, n_val, n_test = 30, 10, 11
    id_train, id_val, id_test = id_orders[0:n_train], id_orders[n_train:(n_train+n_val)], id_orders[(n_train+n_val):51]

    train_list, validation_list, test_list = [], [], []
    train_vid_num, val_vid_num, test_vid_num = 0, 0, 0

    for id in id_train:
        itemindex = np.where(person_ID == id)
        for i in itemindex[0]:
            train_list += lists[i]
            train_vid_num += 1

    for id in id_val:
        itemindex = np.where(person_ID == id)
        for i in itemindex[0]:
            validation_list += lists[i]
            val_vid_num += 1

    for id in id_test:
        itemindex = np.where(person_ID == id)
        for i in itemindex[0]:
            test_list += lists[i]
            test_vid_num += 1

    print('train/val/test video nums are: ', train_vid_num, val_vid_num, test_vid_num)
    print('train/val/test image nums are: ', len(train_list), len(validation_list), len(test_list))

    # for i in tqdm(range(n_train), desc='loading traning samples ... '):
    #     train_list.append(samples[i])
    #
    # for i in tqdm(range(n_val), desc='loading validation samples ... '):
    #     validation_list.append(samples[i])
    #
    # for i in tqdm(range(n_test), desc='loading testing samples ... '):
    #     test_list.append(samples[i])
    folder = 'train_val_test_split'
    img_list_2_txt(folder, 'train.txt', train_list)
    img_list_2_txt(folder, 'val.txt', validation_list)
    img_list_2_txt(folder, 'trainval.txt', train_list+validation_list)
    img_list_2_txt(folder, 'test.txt', test_list)

    copy_data(directory, 'train/img', train_list, '_halfres.jpg')
    copy_data(directory, 'train/gt', train_list, '_mask.png')
    copy_data(directory, 'val/img', validation_list, '_halfres.jpg')
    copy_data(directory, 'val/gt', validation_list, '_mask.png')
    copy_data(directory, 'test/img', test_list, '_halfres.jpg')
    copy_data(directory, 'test/gt', test_list, '_mask.png')


def copy_data(source_directory, target_directory, img_list, extension):
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)
    os.makedirs(target_directory)
    for i, img in enumerate(img_list):
        imgname = img + extension
        source = os.path.join(source_directory, imgname)
        target = os.path.join(target_directory,imgname)
        [target_sub_dir, file] = os.path.split(target)
        if not os.path.exists(target_sub_dir):
            os.makedirs(target_sub_dir)
        copyfile(source, target)


def img_list_2_txt(folder, filename, split_list):
    if not os.path.exists(folder):
        os.makedirs(folder)
    text_file = open(os.path.join(folder, filename), "w")
    for i, file in enumerate(split_list):
        text_file.write(file+'\n')
    text_file.close()


if __name__ == '__main__':
    root = './data_split_by_seq'
    videos = [dI for dI in os.listdir(root) if os.path.isdir(os.path.join(root,dI))]
    lists = [[] for i in range(len(videos))]
    person_ID = np.zeros(len(videos))

    for i, video in enumerate(videos):
        ids = video.split('_')
        # print(ids)
        person_ID[i] = int(ids[0])
        sub_dir = os.path.join(root, video)
        for file in os.listdir(sub_dir):
            if file.endswith("_mask.png"):
                original_rgb_path = os.path.join(sub_dir, file[:-9] + '.jpg')
                half_resolution_rgb_path = os.path.join(sub_dir, file[:-9] + '_halfres.jpg')
                segmentation_mask_path = os.path.join(sub_dir, file)
                corners_path = os.path.join(sub_dir, file[:-9] + '.json')
                if os.path.exists(original_rgb_path) & os.path.exists(half_resolution_rgb_path) & os.path.exists(segmentation_mask_path) & os.path.exists(corners_path):
                    lists[i].append(os.path.join(video, file[:-9]))

    vid_counter = 0
    frame_counter = 0
    for list_video in lists:
        vid_counter += 1
        frame_counter += len(list_video)

    print('video frame nums: ', frame_counter)
    print('video nums: ', vid_counter)

    random_generator = np.random.RandomState(23455)
    split_data(root, random_generator, person_ID, lists)


