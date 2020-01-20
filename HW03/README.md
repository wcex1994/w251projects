
Jetson Bash:


sudo docker network create --driver bridge hw03
sudo docker build -t facedetector -f Dockerfile.facedetector . 

# container needs to be run as privileged to get access to the devices.
sudo docker run -d --name facedetector --privileged --device=/dev/video1:/dev/video1 --network hw03 facedetector

sudo docker run --name facedetector --privileged --device=/dev/video1:/dev/video1 -ti --network hw03 facedetector sh

sudo docker build -t mosquittobroker -f Dockerfile.mosquittobroker . 
sudo docker run -d --name mosquittobroker --network hw03 -p 1883:1883 mosquittobroker
# Get the IP address of the broker 172.18.0.2
sudo docker inspect mosquittobroker

sudo docker build -t messageforwarder -f Dockerfile.messageforwarder . 

sudo docker run --name messageforwarder --network hw03 -ti messageforwarder sh

sudo docker rmi $(sudo docker images -f "dangling=true" -q)

sudo docker run --name mosquittobroker --network hw03 -p 1883:1883 mosquittobroker

