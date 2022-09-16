# <center> 一、自制VOC数据集</center>

## 首先，按照VOC2007的数据集格式要求，分别创建文件夹`VOCdevkit`、`VOC2007`、`Annotations`、`ImageSets`、`Main`和`JPEGImages`，它们的层级结构如下所示：

``` └─VOCdevkit
    └─VOC2007
        ├─Annotations
        ├─ImageSets
        │  └─Main
        └─JPEGImages
```

## 其中，`Annotations`用来存放`xml`标注文件，`JPEGImages`用来存放图片文件，而`ImageSets/Main`存放几个`txt`文本文件，文件的内容是训练集、验证集和测试集中图片的名称(去掉扩展名)，这几个文本文件是需要我们自己生成的。

## 接下来新建一个脚本，把它放在`VOCdevkit/VOC2007`文件夹下，命名为`test.py`，层级结构如下所示：

```─VOCdevkit
    └─VOC2007
        │  test.py
        │
        ├─Annotations
        ├─ImageSets
        │  └─Main
        └─JPEGImages
```

## 然后，进入到目录`VOCdevkit/VOC2007`，执行这个脚本，结束后，在`ImageSets/Main`下生成了4个`txt`文件，层级结构如下：

```─VOCdevkit
    └─VOC2007
        │  test.py
        │
        ├─Annotations
        ├─ImageSets
        │  └─Main
        │       test.txt
        │       train.txt
        │       trainval.txt
        │       val.txt
        └─JPEGImages
```

## 这4个文件的格式都是一样的，文件的内容是对应图片名称去掉扩展名。

## 最后，在`VOCdevkit`同级目录下创建脚本`VOC_labels.py`文件，并执行，就会生成`2007_train.txt`、`2007_val.txt`、`2007_test.txt`以及`yolo数据集`对应的`txt`文件，其层级结构如下：

```─VOCdevkit
   │ └─VOC2007
   │   │    test.py
   │   │
   │   ├─Annotations
   │   ├─ImageSets
   │   │  └─Main
   │   │        test.txt
   │   │        train.txt
   │   │        trainval.txt
   │   │        val.txt
   │   ├─JPEGImages 
   │   └─labels
   │           00001.txt     
   VOC_labels.py
   2007_train.txt       
   2007_val.txt
   2007_test.txt
```

## 至此，VOC数据集制作完成，且训练、测试、验证集都已划分。
