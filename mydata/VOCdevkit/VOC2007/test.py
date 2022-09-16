import os
import random

# 训练集和验证集的比例分配
trainval_percent = 0.1
train_percent = 0.9

# 标注文件的路径
xmlfilepath = 'C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/Annotations'

# 生成的txt文件存放路径
txtsavepath = 'C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('C:/Users/pei_m/Desktop/voc_yolo/mydata/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()