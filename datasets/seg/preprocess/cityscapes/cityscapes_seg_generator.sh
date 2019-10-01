#!/usr/bin/env bash
# -*- coding:utf-8 -*-
# Author: Donny You(youansheng@gmail.com)
# Generate train & val data.


ORI_ROOT_DIR='/n/pfister_lab2/Lab/xingyu/Dataset/Cityscapes2'
SAVE_DIR='/n/pfister_lab2/Lab/xingyu/Dataset/Cityscapes2'


python cityscapes_seg_generator.py --ori_root_dir $ORI_ROOT_DIR \
                                   --save_dir $SAVE_DIR
