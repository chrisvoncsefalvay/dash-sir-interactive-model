# Dash SIR distancing model

[! https://img.shields.io/github/license/chrisvoncsefalvay/dash-sir-distancing-model] [! https://img.shields.io/badge/Made%20at-Starschema-red]
A Dash illustration of a SIR epidemic model with social distancing.


## Running locally

To run a development instance locally, create a virtualenv, install the 
requirements from `requirements.txt` and launch `app.py` using the 
Python executable from the virtualenv.

## Deploying on ECS

Use `make image` to create a Docker image. Then, follow [these 
instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/) 
to deploy the image on ECS.