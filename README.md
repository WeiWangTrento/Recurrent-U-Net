# Recurrent-U-Net
## Recurrent U-Net for Resource-Constrained Segmentation

![Coarse to Fine Hand Segmentation with Recurrent U-Net](./loop.pdf)

### Code
Please check the following URL for the code:
https://github.com/kcyu2014/recurrent-unet/blob/master/README.md

### Dataset
- *KBH.tar.gz* contains more than **12.5K** annoated hand segmentation images.
- *KBH2.tar.gz* is an extension which contains **3,054** annoated hand segmentation images.
- In total, there are **15,590** annotated hand segmentation images.

### Dataset Download Link
- *KBH.tar.gz* 
https://drive.google.com/file/d/1qEhfj7ezqzfzfJ_TbHC8PhJwzpg60bkN/view?usp=sharing
- *KBH2.tar.gz*
https://drive.google.com/file/d/1oc4N78LQqSkY0d3x4E5Q-qqD0z_hLZpI/view?usp=sharing
- *The two datasets need to be fused manually*
**If you used this dataset in your research, please consider citing:**

```
@inproceedings{wang2019recurrent,
  title={Recurrent U-Net for resource-constrained segmentation},
  author={Wang, wei and Yu, Kaicheng and Hugonot, Joachim and Fua, Pascal and Salzmann, Mathieu},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  pages={2142--2151},
  year={2019}
}
```

- Train Val Test Split
  - train_val_test_split folder saves the split used for the ICCV publication.
  - *split.py* shows how to get the train_val_test_split folder for KBH dataset.
  - *split2.py* shows how to get the train_val_test_split_ext folder for the extra images in KBH2.

- Command
  ``` 
  tar -xvzf KBH.tar.gz
  tar -xvzf KBH2.tar.gz
  python split.py
  python split2.py
  ```
  - txt fiels in *train_val_test_split* & *train_val_test_split_ext* folders need to be merged manually if you want to use all the images.

