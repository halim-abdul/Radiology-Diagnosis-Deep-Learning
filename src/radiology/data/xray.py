"""Image dataset for PNG/JPEG exports of de-identified radiographs."""
from pathlib import Path
import numpy as np
from PIL import Image
import torch
from torch.utils.data import Dataset

class XrayDataset(Dataset):
    def __init__(self, frame, size=224, transform=None):
        self.frame = frame.reset_index(drop=True)
        self.size = size
        self.transform = transform

    def __len__(self):
        return len(self.frame)

    def __getitem__(self, index):
        row = self.frame.iloc[index]
        with Image.open(Path(row.image_path)) as image:
            image = image.convert("RGB").resize((self.size, self.size))
            tensor = torch.from_numpy(np.array(image, dtype=np.float32).transpose(2, 0, 1).copy()) / 255.
        if self.transform:
            tensor = self.transform(tensor)
        return tensor, torch.tensor(float(row.label), dtype=torch.float32)
