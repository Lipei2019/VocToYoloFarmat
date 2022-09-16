import os
import shutil
import random

# 训练集、验证集和测试集的比例分配
test_percent = 0.0
valid_percent = 0.2
train_percent = 1

# 标注文件的路径
image_path = 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/images'
label_path = 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/labels'

images_files_list = os.listdir(image_path)
labels_files_list = os.listdir(label_path)
print('images files: {}'.format(images_files_list))
print('labels files: {}'.format(labels_files_list))
total_num = len(images_files_list)
print('total_num: {}'.format(total_num))

test_num = int(total_num * test_percent)
valid_num = int(total_num * valid_percent)
train_num = int(total_num * train_percent)

# 对应文件的索引
test_image_index = random.sample(range(total_num), test_num)
valid_image_index = random.sample(range(total_num), valid_num) 
train_image_index = random.sample(range(total_num), train_num)

for i in range(total_num):
    print('src image: {}, i={}'.format(images_files_list[i], i))
    if i in test_image_index:
        # 将图片和标签文件拷贝到对应文件夹下
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/images/{}'.format(images_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/test/images/{}'.format(images_files_list[i]))
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/labels/{}'.format(labels_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/test/labels/{}'.format(labels_files_list[i]))
    elif i in valid_image_index:
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/images/{}'.format(images_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/valid/images/{}'.format(images_files_list[i]))
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/labels/{}'.format(labels_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/valid/labels/{}'.format(labels_files_list[i]))
    else:
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/images/{}'.format(images_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/train/images/{}'.format(images_files_list[i]))
        shutil.copyfile('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/labels/{}'.format(labels_files_list[i]), 'C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/train/labels/{}'.format(labels_files_list[i]))