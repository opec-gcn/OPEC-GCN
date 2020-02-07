# OPEC-GCN
OPEC-GCN: Occluded Pose Estimation and Correction using Graph Convolutional Neural Networks  

## Module Pipeline
![Pipeline](show_img/pipeline.png)

## training
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

