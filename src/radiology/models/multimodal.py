"""Late fusion of image embeddings and structured context vectors."""
import torch
from torch import nn

class LateFusion(nn.Module):
    def __init__(self,image_encoder,image_features,metadata_features,hidden=128):
        super().__init__()
        self.encoder=image_encoder
        self.metadata=nn.Sequential(nn.Linear(metadata_features,hidden),nn.ReLU())
        self.head=nn.Sequential(nn.Linear(image_features+hidden,hidden),nn.ReLU(),nn.Linear(hidden,1))
    def forward(self,image,metadata):
        embedding=self.encoder(image)
        if embedding.ndim>2:
            embedding=embedding.flatten(start_dim=1)
        return self.head(torch.cat([embedding,self.metadata(metadata)],dim=1))
