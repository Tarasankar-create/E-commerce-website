#! /bin/bash

set -e

# Update package
apt-get update -y

# install docker
apt-get install docker.io -y

systemctl start docker
systemctl enable docker

# Allow user
usermod -aG docker ubuntu

# install openjdk
apt-get install fontconfig openjdk-21-jre -y

# install jenkins
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2026.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins -y

systemctl enable jenkins
systemctl start jenkins