# FROM nvidia/cuda:8.0-cudnn5-devel   
# start with the nvidia container for cuda 8 with cudnn 5

# 

FROM ubuntu:16.04
# start with simple base

# forked from https://github.com/mjsobrep/DockerFiles-public
# forked from https://github.com/garyfeng/docker-openpose

LABEL maintainer "Alex Warren <exrhizo@gmail.com>"

# needed for garyfeng style
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget unzip lsof apt-utils lsb-core -y
RUN apt-get install libatlas-base-dev -y
RUN apt-get install libopencv-dev python-opencv python-pip -y

# Additional for cmake build
# from install_cmake.sh
RUN apt-get install build-essential
# General dependencies
RUN apt-get --assume-yes install libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler
RUN apt-get --assume-yes install --no-install-recommends libboost-all-dev
# Remaining dependencies, 14.04
RUN apt-get --assume-yes install libgflags-dev libgoogle-glog-dev liblmdb-dev
# Python libs
RUN pip install --upgrade numpy protobuf
# cmake
RUN apt-get install cmake

RUN wget https://github.com/CMU-Perceptual-Computing-Lab/openpose/archive/master.zip; \
    unzip master.zip; rm master.zip

RUN mkdir /openpose-master/build

WORKDIR openpose-master/build

RUN cmake -DGPU_MODE=CPU_ONLY ..
RUN make -j$(grep processor /proc/cpuinfo | wc -l) install

WORKDIR /
RUN git clone https://github.com/exrhizo/expressome.git
WORKDIR /expressome

# RUN sed -i 's/\<sudo chmod +x $1\>//g' ubuntu/install_caffe_and_openpose_if_cuda8.sh; \
#     sed -i 's/\<sudo chmod +x $1\>//g' ubuntu/install_openpose_if_cuda8.sh; \
#     sed -i 's/\<sudo -H\>//g' 3rdparty/caffe/install_caffe_if_cuda8.sh; \
#     sed -i 's/\<sudo\>//g' 3rdparty/caffe/install_caffe_if_cuda8.sh; \
#     sync; sleep 1; ./ubuntu/install_caffe_and_openpose_if_cuda8.sh