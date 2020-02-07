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
You can easily start to train CrowdPose dataset using following code.
```
CUDA_VISIBLE_DEVICES=0 python ./tools/train_alpha_pose_gcn.py --indir ../crowdpose/images/ --nEpochs 25 --trainBatch 20 --validBatch 60 --LR 1e-3 --dataset 'coco' --config ./configs/OPEC_GCN_CrowdPose_Test.py
```
## Result


Methods |mAP@50:95|AP50|AP75|AP80| AP90 
:--------------:|:--:|:--:|:--: |:--:  |:--:
AlphaPose| 67.9 |86.0 | 72.6| 66.8 | 45.7
A+OPEC-GCN| **69.6** | 86.1 | **74.9** | **69.3**  | **48.0** 
CrowdPose| 68.5 | 86.7 | 73.2| 66.9 |  45.9
CrowdPose+OPEC-GCN| **70.2** | **86.8**| **75.4** | **69.9**  | **48.4** 

 
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

