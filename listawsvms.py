# by cb, 2020-02
## simple example printing information about running and stopped VMs in AWS using AWS-CLI 
# Usage:
## aws cli must be installed
### apt-get install -y python python-pip
### pip install awscli
## aws configure --profile profileName
### to generate multiple credentials-pairs within the credentials config


import os

# change to your locations
path = "/home/usr/.aws/credentials"
logpath ="/var/log/awsvms.txt"

if os.path.isfile(logpath):
	os.remove(logpath)

if os.path.isfile(path):
	with open(path, 'r') as file:
		line = "1"
		while line:
			line = file.readline()
			if line.find("]") > 0: # All profile names are in [ ]
				profile = line.split("[")[1].split("]")[0]
				os.system("echo '_______ Profile: " + profile + " ______' >> " + logpath)
				os.system ("echo '### running VMs ###' >> "+ logpath)
				os.system("aws --profile "+ profile + " ec2 describe-instances --filters \"Name=instance-state-name,Values=running\" --output table --query 'Reservations[*].Instances[*].[Tags[?Key==`Name`].Value, NetworkInterfaces[*].Association.PublicDnsName, InstanceType, LaunchTime]' >> " + logpath + "")
				os.system("echo '### stopped VMs ###' >> " + logpath)
				os.system("aws --profile "+ profile + " ec2 describe-instances --filters \"Name=instance-state-name,Values=stopped\" --output table --query 'Reservations[*].Instances[*].Tags' >> " + logpath + "")

