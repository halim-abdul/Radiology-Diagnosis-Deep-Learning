"""Vision Transformer research baseline with torchvision."""
import torch.nn as nn
from torchvision.models import vit_b_16

def make_vit(image_size=224):
    if image_size != 224:
        raise ValueError("This baseline expects 224x224 input")
    model=vit_b_16(weights=None)
    model.heads=nn.Linear(model.hidden_dim,1)
    return model
