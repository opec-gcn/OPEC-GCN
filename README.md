# OPEC-GCN
OPEC-GCN: Occluded Pose Estimation and Correction using Graph Convolutional Neural Networks  

## Module Pipeline
![Pipeline](show_img/pipeline.png)

## Datasets
In our work, we mainly use three dataset to evaluate our considerablely results.   
you can download the dataset from below link.  
[CrowdPose](https://github.com/Jeff-sjtu/CrowdPose)  
[OCHuman](https://cg.cs.tsinghua.edu.cn/dataset/form.html?dataset=ochuman)  
[MSCOCO](http://images.cocodataset.org/zips/train2017.zip)  

## Initialize
### Folder Structure
Firstly you should download the dataset, and then your project folder looks like follow structure. All of img_dir you can modify in [config](configs/OPEC_GCN_CrowdPose_Test.py)  

--Crowdpose/images/...  
--train2017/...  
--OPEC-GCN/...  
### Download weights
At the same time, you need download the weights of sppe and yolov3 because our OPEC-GCN depends on Alphapose as base module.  
So download the models manually: **duc_se.pth** (2018/08/30) ([Google Drive]( https://drive.google.com/open?id=1OPORTWB2cwd5YTVBX-NE8fsauZJWsrtW) | [Baidu pan](https://pan.baidu.com/s/15jbRNKuslzm5wRSgUVytrA)), **yolov3-spp.weights**([Google Drive](https://drive.google.com/open?id=1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC) | [Baidu pan](https://pan.baidu.com/s/1Zb2REEIk8tcahDa8KacPNA)). Place them into `./weights/sppe` and `./weights/yolo` respectively.

### Process Data
Considering convenience, I already processed datasets for you so that you can easily train your opec-gcn model.
download the json file manually: [train_process_datasets]( https://drive.google.com/open?id=1OPORTWB2cwd5YTVBX-NE8fsauZJWsrtW), [test_process_datasets](https://drive.google.com/open?id=1D47msNOOiJKvPOXlnpyzdKA3k6E97NTC). Place them into `./train_process_datasets` and `./test_process_datasets` respectively.



## Train
```bash
bash train.sh  

Better Para:  
   --epochs 120  
   --batch_size 8  
   --model_def ./config/yolo-nano_person.cfg  
   --lr 2.5e-4  
   --fix_up True  
   --lr_policy cosine
```
## Testing
```bash
python test.py --data_config ./config/coco_person.data --model_def ./config/yolo-nano_person.cfg --weights_path [checkpoint path]
```
## Result
In this engineer we only train our model using coco-train person class  
we compare with yolov-3，yolo-tiny. We got competitive results.  

Methods |mAP@50|mAP|weights|FPS| Model 
:--------------:|:--:|:--:|:--: |:--:  |:--:
 yolov3(paper)      | 74.4 |40.3 | 204.8M| 28.6FPS  |[Google Disk](https://pjreddie.com/media/files/yolov3.weights)
 yolov3-tiny(paper) | 38.8 |15.6 | 35.4M | 45FPS |[Google Disk](https://pjreddie.com/media/files/yolov3-tiny.weights)
 yolo-nano          | 55.6 |27.7 | 22.0M | 40FPS |[Baidu WebDisk](https://pan.baidu.com/s/1Rp0is2LqA91XwjRc41mGaw)  
 
Baidu WebDisk Key: p2j3
## Ablation Result
 Augmentation| fixup | mAP 
:--------------:|:--:|:--:
No|No|54.3
Yes|No|53.9
No|YES|55.6
YES|YES|54.8   
## Inference Result
![Pipeline](assets/show.jpg)

