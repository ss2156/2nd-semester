#!/bin/bash

##################################
# Install the Ryu SDN Controller #
##################################

# Update APT's repositories and get Ryu basically.
sudo apt-get update && apt-get install -y python3 python3-pip python3-ryu
