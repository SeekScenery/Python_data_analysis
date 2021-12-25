# -*- coding = utf-8 -*-
# @Time : 2021/12/25 20:46
# @Author : qiu
# @File : data_divide.py
# @Software : PyCharm
import os
import shutil
import random


img_path = "./All_data/images/"
label_path = "./All_data/labels/"
list_img = os.listdir(img_path)
random.shuffle(list_img)


def data_divide(data_list, train_ratio, valid_ratio):
    """
    用来切分数据集
    :param data_list: 样本文件路径
    :param train_ratio:训练集比率
    :param valid_ratio:验证集比例
    :return:无
    """
    list_train = ['train', 'valid', 'test']
    data_len = len(data_list)
    # 设置train、valid、test 的比例
    train_len = int(train_ratio * data_len)
    valid_len = int(valid_ratio * data_len)
    test_len = data_len - train_len - valid_len
    for folder in list_train:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.mkdir(folder)
        os.mkdir('./' + folder + '/images')
        os.mkdir('./' + folder + '/labels')

    for count, file in enumerate(data_list):
        file_img_path = img_path + file
        file_label_path = label_path + file[:-4] + '.txt'
        if count < train_len:
            shutil.copy(file_img_path, 'train/images')
            shutil.copy(file_label_path, 'train/labels')
        elif count < train_len + valid_len:
            shutil.copy(file_img_path, 'valid/images')
            shutil.copy(file_label_path, 'valid/labels')
        else:
            shutil.copy(file_img_path, 'test/images')
            shutil.copy(file_label_path, 'test/labels')
    print(f"train data number: {train_len}")
    print(f"valid data number: {valid_len}")
    print(f"test data number: {test_len}")


data_divide(list_img, 0.6, 0.2)
