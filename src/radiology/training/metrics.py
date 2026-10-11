"""Metrics and operating-point utilities."""
import numpy as np
from sklearn.metrics import roc_auc_score,average_precision_score,confusion_matrix

def binary_metrics(labels,probabilities,threshold=0.5):
    y=np.asarray(labels,dtype=int)
    p=np.asarray(probabilities,dtype=float)
    if y.shape!=p.shape: raise ValueError("Shapes must match")
    predictions=(p>=threshold).astype(int)
    tn,fp,fn,tp=confusion_matrix(y,predictions,labels=[0,1]).ravel()
    return {"auroc":float(roc_auc_score(y,p)) if len(set(y))>1 else None,
            "average_precision":float(average_precision_score(y,p)) if y.sum()>0 else None,
            "sensitivity":float(tp/(tp+fn)) if tp+fn else None,
            "specificity":float(tn/(tn+fp)) if tn+fp else None,
            "tp":int(tp),"tn":int(tn),"fp":int(fp),"fn":int(fn)}
