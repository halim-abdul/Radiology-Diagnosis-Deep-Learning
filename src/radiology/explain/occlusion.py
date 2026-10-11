"""Simple perturbation-based attribution for toy 2D experiments."""
import torch

@torch.no_grad()
def occlusion_map(model,image,patch=16):
    if image.ndim!=4 or image.shape[0]!=1: raise ValueError("Expected [1,C,H,W]")
    model.eval()
    base=model(image).flatten()[0]
    _,_,h,w=image.shape
    output=torch.zeros((h,w),device=image.device)
    for y in range(0,h,patch):
        for x in range(0,w,patch):
            changed=image.clone()
            changed[:,:,y:y+patch,x:x+patch]=0
            output[y:y+patch,x:x+patch]=base-model(changed).flatten()[0]
    return output
