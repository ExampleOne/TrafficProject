import os
import subprocess

#os.system('scp "output_old.avi" videoprocessor@VideoProcessingServer:Desktop/')

#ssh = paramiko.SSHClient()
#ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#ssh.connect("videoprocessor@VideoProcessingServer", username="videoprocessor", password="")

p = subprocess.Popen(["scp", "output.avi", "videoprocessor@192.168.1.139:videos/"]).wait()
# VideoProcessingServer:Desktop/"])


# To do this, you have to open port 22 on the target server.
# Use ufw sudo allow 22
# Also, make sure everything is up to date, especially the openssh-server, meaning
# ensure sudo apt-get update
# and sudo apt-get install openssh-server
# I found the "askubuntu why am I getting a port 22 connection refused error" quite useful
# Also have to set up host-key connection. using ssh-keygen is useful.
# Follow the guide on digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2
# This allows you to access the terminal of this mac from another computer... (opposite of what we want?)

print("done")

# Need to find a way to find ip addresses. Easiest to accomplish this using the ifconfig command on the target host.
# Why does device name not work?