reply to kys
reply to kms

# Advice
1. phone use panratha niruthu

# DEPLOYMENT
## RUNNING LOCALLY
1. just run main.py duh :dontcry:

## SIMPLE EC2
1. uses systemd to run bot as service
2. uses github workflow to push to ec2

### SETUP
1. [Follow this](https://www.caronteconsulting.com/en/news/run-script-python-service/)
2.  sudo systemctl enable /home/ubuntu/amma-bot/ec2-deployment/amma.service
3.  sudo systemctl daemon-reload
4.  sudo service amma start
5.  https://gist.github.com/comhad/de830d6d1b7ae1f165b925492e79eac8
6.  once ec2 instance has been initialized with the service, further deployments are automated

#### CONS
1. requires an infra (ec2-instance) to be pre setup with service, can be addressed by terraform


## DOCKER IMAGE
build image ```docker build -t my-python-app -f docker\Dockerfile .```

run image


## COMPLEX
