sudo mkdir /var/lib/osiris
sudo mkdir /var/lib/osiris/tensorflow-serve
sudo mkdir /var/lib/osiris/tensorflow-serve/resnet
sudo mkdir /tmp/resnet
sudo curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C /tmp/resnet -xvz
sudo mv /tmp/resnet/* /var/lib/osiris/tensorflow-serve/resnet