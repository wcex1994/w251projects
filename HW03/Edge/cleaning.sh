sudo docker stop facedetector
sudo docker stop messageforwarder
sudo docker stop mosquittobroker
sudo docker rm facedetector
sudo docker rm messageforwarder
sudo docker rm mosquittobroker
sudo docker build -t facedetector -f Dockerfile.facedetector .
sudo docker build -t mosquittobroker -f Dockerfile.mosquittobroker .
sudo docker build -t messageforwarder -f Dockerfile.messageforwarder .
sudo docker rmi $(sudo docker images -f "dangling=true" -q)
sudo docker ps -a
