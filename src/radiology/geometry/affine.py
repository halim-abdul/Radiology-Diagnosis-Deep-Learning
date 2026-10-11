"""Voxel-to-world transformations. Coordinates follow the NIfTI affine convention."""
import numpy as np

def voxel_to_world(points,affine):
    p=np.asarray(points,dtype=float); a=np.asarray(affine,dtype=float)
    if p.shape[-1]!=3 or a.shape!=(4,4): raise ValueError("Expected Nx3 points and 4x4 affine")
    return (np.concatenate([p,np.ones((*p.shape[:-1],1))],axis=-1)@a.T)[...,:3]

def world_to_voxel(points,affine):
    return voxel_to_world(points,np.linalg.inv(np.asarray(affine,dtype=float)))
