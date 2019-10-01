#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Donny You(youansheng@gmail.com)


from model.backbones.vgg.vgg_backbone import VGGBackbone
from model.backbones.darknet.darknet_backbone import DarkNetBackbone
from model.backbones.resnet.resnet_backbone import ResNetBackbone
from model.backbones.mobilenet.mobilenet_backbone import MobileNetBackbone
from model.backbones.densenet.densenet_backbone import DenseNetBackbone
from model.backbones.squeezenet.squeezenet_backbone import SqueezeNetBackbone
from tools.util.logger import Logger as Log


class BackboneSelector(object):

    def __init__(self, configer):
        self.configer = configer

    def get_backbone(self, **params):
        backbone = self.configer.get('network', 'backbone')

        model = None
        if 'vgg' in backbone:
            model = VGGBackbone(self.configer)(**params)

        elif 'darknet' in backbone:
            model = DarkNetBackbone(self.configer)(**params)

        elif 'resnet' in backbone:
            model = ResNetBackbone(self.configer)(**params)

        elif 'mobilenet' in backbone:
            model = MobileNetBackbone(self.configer)(*params)

        elif 'densenet' in backbone:
            model = DenseNetBackbone(self.configer)(**params)

        elif 'squeezenet' in backbone:
            model = SqueezeNetBackbone(self.configer)(**params)

        else:
            Log.error('Backbone {} is invalid.'.format(backbone))
            exit(1)

        return model
