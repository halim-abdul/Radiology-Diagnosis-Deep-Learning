"""Transparent, reproducible binary training loops."""
import torch

def run_epoch(model,loader,optimizer=None,device="cpu"):
    training=optimizer is not None
    model.train(training)
    loss_fn=torch.nn.BCEWithLogitsLoss()
    total=0.; n=0
    for images,labels in loader:
        images,labels=images.to(device),labels.float().to(device).view(-1,1)
        with torch.set_grad_enabled(training):
            logits=model(images)
            loss=loss_fn(logits,labels)
            if training:
                optimizer.zero_grad(set_to_none=True)
                loss.backward()
                optimizer.step()
        batch=labels.numel()
        total+=float(loss.detach())*batch; n+=batch
    if n==0: raise ValueError("Empty data loader")
    return {"loss":total/n}
