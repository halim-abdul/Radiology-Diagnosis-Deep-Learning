"""Input-gradient saliency; explanatory maps are not lesion segmentations."""
import torch

def input_gradient(model,image,target_index=0):
    model.eval()
    x=image.detach().clone().requires_grad_(True)
    logits=model(x)
    value=logits[:,target_index].sum()
    gradient=torch.autograd.grad(value,x)[0]
    return gradient.detach().abs().amax(dim=1)

def normalized_heatmap(values,eps=1e-8):
    values=values.detach()
    minimum=values.amin(dim=(-2,-1),keepdim=True)
    peak=values.amax(dim=(-2,-1),keepdim=True)
    return (values-minimum)/(peak-minimum+eps)
