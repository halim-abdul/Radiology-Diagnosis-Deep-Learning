"""Torchvision ResNet binary baseline; weights are not downloaded automatically."""
import torch.nn as nn
from torchvision.models import resnet18

def make_resnet(pretrained=False):
    if pretrained:
        raise ValueError("Download and validate pretrained weights explicitly before use")
    model=resnet18(weights=None)
    model.fc=nn.Linear(model.fc.in_features,1)
    return model
