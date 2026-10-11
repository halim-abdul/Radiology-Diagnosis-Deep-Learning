"""Binary mask overlap metrics."""
import numpy as np

def dice_score(pred,target,eps=1e-8):
    p=np.asarray(pred,dtype=bool);t=np.asarray(target,dtype=bool)
    if p.shape!=t.shape:raise ValueError("Mask shapes differ")
    return float((2*np.logical_and(p,t).sum()+eps)/(p.sum()+t.sum()+eps))

def iou_score(pred,target,eps=1e-8):
    p=np.asarray(pred,dtype=bool);t=np.asarray(target,dtype=bool)
    if p.shape!=t.shape:raise ValueError("Mask shapes differ")
    return float((np.logical_and(p,t).sum()+eps)/(np.logical_or(p,t).sum()+eps))
