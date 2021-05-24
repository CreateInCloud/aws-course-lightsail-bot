# Deploy commands

Install AWS cli version 2.x and lightsail plugin at 
https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software#install-lightsailctl-on-linux

Then create the `aws-day2`inside lightsail. Feel free to change the tag name to the docker image

Publish command

```shell
docker build -t aws-day2-lightsail-bot .
aws lightsail push-container-image --region eu-west-1 --profile luther --service-name aws-day2 --label aws-day2-lightsail-bot --image aws-day2-lightsail-bot:latest
```

Make sure to configure correctly the `TG_BOT_KEY` variable in Dockerfile

Once uploaded, then manually deploy on Lightsail.