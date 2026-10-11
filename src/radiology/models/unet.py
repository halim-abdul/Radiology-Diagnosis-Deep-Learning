"""Small, fully convolutional U-Net for 2-D segmentation."""
import torch
from torch import nn

def block(a,b):
    return nn.Sequential(nn.Conv2d(a,b,3,padding=1),nn.ReLU(inplace=True),
                         nn.Conv2d(b,b,3,padding=1),nn.ReLU(inplace=True))

class UNet2D(nn.Module):
    def __init__(self,in_channels=1,out_channels=1,base=16):
        super().__init__()
        self.a=block(in_channels,base)
        self.b=block(base,base*2)
        self.c=block(base*2,base*4)
        self.pool=nn.MaxPool2d(2)
        self.up_b=block(base*6,base*2)
        self.up_a=block(base*3,base)
        self.head=nn.Conv2d(base,out_channels,1)
    def forward(self,x):
        a=self.a(x); b=self.b(self.pool(a)); c=self.c(self.pool(b))
        d=self.up_b(torch.cat([b,nn.functional.interpolate(c,size=b.shape[2:],mode="bilinear",align_corners=False)],dim=1))
        e=self.up_a(torch.cat([a,nn.functional.interpolate(d,size=a.shape[2:],mode="bilinear",align_corners=False)],dim=1))
        return self.head(e)
