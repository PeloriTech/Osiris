#!/usr/bin/env bash

echo "Downloading YoloV3 weights..."

mkdir cfg
sudo wget -O cfg/coco.data https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/coco.data
sudo wget -O cfg/yolov3.cfg https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg

echo "Modify config parameters to enable Testing mode"
sed -i '/batch=64/c\# batch=64' cfg/yolov3.cfg
sed -i '/subdivisions=16/c\# subdivisions=16' cfg/yolov3.cfg
sed -i '/# batch=1/c\batch=1' cfg/yolov3.cfg
sed -i '/# subdivisions=1/c\subdivisions=1' cfg/yolov3.cfg
sed -i '/names = data\/coco.names/c\names = data\/coco.names' cfg/coco.data
mkdir data
sudo wget -O data/coco.names https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

echo "Downloading yolov3 weights"
mkdir weights
sudo wget -O weights/yolov3.weights https://pjreddie.com/media/files/yolov3.weights


echo "Installing YoloV3 libraries...."

export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

sudo apt-get install -y virtualenv
virtualenv --system-site-packages --python=python3.6 venv
venv/bin/pip3.6 install -r requirements.txt