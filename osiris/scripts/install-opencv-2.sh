#!/usr/bin/env bash

sudo apt-get install -y build-essential cmake

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):
sudo apt-get install -y qt5-default libvtk6-dev

# Media I/O:
sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev

# Video I/O:
sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev

# Parallelism and linear algebra libraries:
sudo apt-get install -y libtbb-dev libeigen3-dev

# Python:
sudo apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy

# Java:
sudo apt-get install -y ant default-jdk

# Documentation:
sudo apt-get install -y doxygen


sudo apt-get update -y && apt-get install -y \
            libgstreamer1.0-0 \
            gstreamer1.0-plugins-base \
            gstreamer1.0-plugins-good \
            gstreamer1.0-plugins-bad \
            gstreamer1.0-plugins-ugly \
            gstreamer1.0-libav \
            gstreamer1.0-doc \
            gstreamer1.0-tools \
            libgstreamer1.0-dev \
            libgstreamer-plugins-base1.0-dev
sudo apt-get update -y && apt-get install -y  pkg-config \
 zlib1g-dev  libwebp-dev \
 libtbb2 libtbb-dev  \
 libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
 cmake
sudo apt-get install -y \
  autoconf \
  autotools-dev \
  build-essential \
  gcc \
  git

git clone https://github.com/opencv/opencv.git /var/local/git/opencv
cd /var/local/git/opencv && \
  git checkout tags/3.4.5
mkdir -p /var/local/git/opencv/build && \
     cd /var/local/git/opencv/build && \
    cmake -D CMAKE_BUILD_TYPE=Release -D \
    BUILD_TIFF=OFF -D BUILD_TBB=OFF -D BUILD_JPEG=ON \
    -D BUILD_JASPER=OFF -D BUILD_ZLIB=ON -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_java=OFF -D BUILD_opencv_python2=ON \
    -D BUILD_opencv_python3=ON -D ENABLE_NEON=OFF -D WITH_OPENCL=OFF \
    -D WITH_OPENMP=OFF -D WITH_FFMPEG=ON -D WITH_GSTREAMER=ON -D WITH_GSTREAMER_0_10=OFF \
    -D WITH_GTK=ON \
    -D WITH_VTK=OFF -D WITH_TBB=ON -D WITH_1394=OFF -D WITH_OPENEXR=OFF \
    -D INSTALL_C_EXAMPLES=OFF -D INSTALL_TESTS=OFF ..
cd /var/local/git/opencv/build && \
      make install
