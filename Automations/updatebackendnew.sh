#!/bin/bash

# Set the Instance ID and path to the .env file
INSTANCE_ID="i-02019f70d86a3d0b1"

# Retrieve the public IP address of the specified EC2 instance
ipv4_address=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID --query 'Reservations[0].Instances[0].PublicIpAddress' --output text)

# Path to the .env file
file_to_find="../.env"

# Check the current FRONTEND_URL in the .env file
current_url=$(sed -n "1p" $file_to_find)

# Update the .env file if the IP address has changed
if [[ "$current_url" != "ALLOWED_HOSTS=\"${ipv4_address}\"" ]]; then
    if [ -f $file_to_find ]; then
        sed -i -e "s|ALLOWED_HOSTS.*|ALLOWED_HOSTS=\"${ipv4_address}\"|g" $file_to_find
    else
        echo "ERROR: File not found."
    fi
fi
