# Dash SIR distancing model

An interactive Dash illustration of a SIR epidemic model with social distancing.

![Sample output SIR plot](https://raw.githubusercontent.com/chrisvoncsefalvay/dash-sir-interactive-model/master/Screenshot%202020-07-24%20at%201.15.05%20PM.png?token=AAUL4FHX7J5QYEAXKZ7DX7K7DMMBG)

## Running locally

To run a development instance locally, create a virtualenv, install the 
requirements from `requirements.txt` and launch `app.py` using the 
Python executable from the virtualenv.

## Deploying on ECS

Use `make image` to create a Docker image. Then, follow [these 
instructions](https://www.chrisvoncsefalvay.com/2019/08/28/deploying-dash-on-amazon-ecs/) 
to deploy the image on ECS.
