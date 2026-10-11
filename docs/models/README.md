# Models

CNN: ResNet18 binary logit baseline. ViT: torchvision ViT-B/16 with randomly initialized weights. Segmentation: lightweight U-Net for 2D masks. Multimodal: concatenate image and tabular embeddings; use only permitted, clinically appropriate metadata and control for shortcuts. No pretrained checkpoints are bundled. Compare against simple baselines with patient-wise held-out evaluation.
