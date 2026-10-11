import torch
from radiology.models.unet import UNet2D
from radiology.training.metrics import binary_metrics

def test_unet_shape():
    x=torch.randn(2,1,64,64)
    assert UNet2D()(x).shape==(2,1,64,64)

def test_metrics():
    metrics=binary_metrics([0,1],[0.1,0.9])
    assert metrics["auroc"]==1.0
