# Object Storage Result
![S3 Results](https://github.com/wcex1994/w251projects/blob/master/HW03/cloud/S3%20Screenshot.png)


# On Jetson Bash
```
sudo docker network create --driver bridge hw03

sudo docker build -t facedetector -f Dockerfile.facedetector . 
sudo docker build -t mosquittobroker -f Dockerfile.mosquittobroker . 
sudo docker build -t messageforwarder -f Dockerfile.messageforwarder . 

# To Get the IP address of the broker 172.18.0.2
sudo docker inspect mosquittobroker

# Container needs to be run as privileged to get access to the devices.
sudo docker run -d --name mosquittobroker --network hw03 -p 1883:1883 mosquittobroker
sudo docker run -d --name messageforwarder --network hw03 messageforwarder
sudo docker run -d --name facedetector --privileged --device=/dev/video1:/dev/video1 --network hw03 facedetector

# For debug purpose:
sudo docker run --name messageforwarder --network hw03 -ti messageforwarder sh
sudo docker run --name facedetector --privileged --device=/dev/video1:/dev/video1 -ti --network hw03 facedetector sh
```

# On IBM VM Bash
```
docker network create --driver bridge hw03

docker build -t mosquittobroker -f Dockerfile.mosquittobroker . 
docker build -t saveface -f Dockerfile.saveface .
docker run -d --name mosquittobroker -p 1883:1883 --network hw03 mosquittobroker
docker run -d --name saveface --network hw03 saveface

# For debug purpose:
docker run -d --name mosquittobroker -p 1883:1883 --network hw03 mosquittobroker
docker run --name saveface --network hw03 -ti saveface sh
```
# Topics
* Local topic is `hw03new`
* Cloud topic is `hw03cloud`

# QoS
* I didn't set specific QoS, so the system used its default.
