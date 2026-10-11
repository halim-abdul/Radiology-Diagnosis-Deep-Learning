import numpy as np
from radiology.geometry.affine import voxel_to_world,world_to_voxel
from radiology.geometry.overlap import dice_score

def test_affine_round_trip():
    a=np.array([[2,0,0,8],[0,3,0,-3],[0,0,4,2],[0,0,0,1]])
    p=np.array([[1.,2.,3.]])
    np.testing.assert_allclose(world_to_voxel(voxel_to_world(p,a),a),p)

def test_dice():
    assert dice_score([1,0,1],[1,0,1])==1.0
