## Instructions

### Prepare Credentials

Retrieve you temporary credentials from Learner's Lab.
Enter your configuration when prompted:
```
aws configure
```

And set your session token:
```
aws configure set aws_session_token <YOUR-TEMP-SESSION-TOKEBN>
```

### Apply Infrastructure
```
cd terraform
terraform init
terraform apply -auto-approve
```

### Send Requests
Make sure you are in terraform folder

Get public ip address
```
aws ec2 describe-network-interfaces \
--network-interface-ids $(
    aws ecs describe-tasks \
    --cluster $(terraform output -raw ecs_cluster_name) \
    --tasks $(
        aws ecs list-tasks \
        --cluster $(terraform output -raw ecs_cluster_name) \
        --service-name $(terraform output -raw ecs_service_name) \
        --query 'taskArns[0]' --output text
    ) \
    --query "tasks[0].attachments[0].details[?name=='networkInterfaceId'].value" \
    --output text
) \
--query 'NetworkInterfaces[0].Association.PublicIp' \
--output text
```

Send some requests:
```
Health Check:
curl http://<PUBLIC-IP-ADDRESS>:8080/products

GET:
# Shows all the products in the server
curl GET http://<PUBLIC-IP-ADDRESS>:8080/products

POST:
# Writes a new prodcut into the server
curl POST http://<PUBLIC-IP-ADDRESS>:8080/products
```

Successful Output:
```
To see succcessful healthcheck please navigate to src/Successful curl in after connecting via AWS.png

To see successful GET on the server, please navigate to src/Successful GET in AWS.png

To see successful POST on the server, please navigate to src/Successful post in AWS.png
```

Where to find:
```
To locate server code please navigate to src/product_api.py

To locate Docker File please naviagate to src/Dockerfile

To locate the infrastructure please navigate to the terraform folder
```

## Clean Up
```
terraform destroy -auto-approve
```
