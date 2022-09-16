import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# 根据自己情况修改
classes = ["FWUAV", "UAV"]


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):

    if not os.path.exists('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/Annotations/%s.xml' % (image_id)):
        return

    in_file = open('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/Annotations/%s.xml' % (image_id))

    out_file = open('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

for image in os.listdir('C:/Users/pei_m/Desktop/voc_yolo/Yolo5DataSets/images'):
    # 这里需要根据你的图片情况进行对应修改。比如图片名称是123.456.jpg，这里就会出错了。
    # 一般来讲，如果图片格式固定，如全都是jpg，那就image_id=image[:-4]处理就好了。
    # 总之，情况比较多，自己看着办，哈哈！
    image_id = image.split('.')[0]
    convert_annotation(image_id)