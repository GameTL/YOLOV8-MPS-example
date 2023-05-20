# Overview
Only how I got my machine to use MPS for Yolo will be documented here. Your mileage may vary.
Thank you to Ultralytics and the Open Source communities for their work on Yolo and especially the modifications to make it work with MPS.

MPS is Apple own API for interfacing with the GPU and is used by Metal. It's kinda like CUDA eqv. but for Mac.

# Performace
On my Macbook Pro 16" 2023 M2 Pro with 12-core CPU & 19-core of GPU.
inference change from 14fps to 43fps with yolov8s.pt

However, the GPU is not fully utilized. Only about 70% of the GPU is utilised.

<img src="misc/Screenshot 2023-05-21 at 00.38.24.png" alt="Image of YOLO with CPU" width="33%">
<img src="misc/Screenshot 2023-05-21 at 00.38.13.png" alt="Image of YOLO with GPU" width="35%">
<img src="misc/Screenshot 2023-05-21 at 00.34.16.png" alt="Image of GPU ultilisation for M2 Pro" width="25%">


# Setup
Install the lastest version of YOLO 
```
pip install ultralytics
```

Using anaconda, install the lastest version of pytorch-nightly for MPS support.
```
conda install pytorch torchvision torchaudio -c pytorch-nightly
```


