[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/dashboard?id=FrancescoDiSalesGithub_DirtyOps)
# DirtyOps 

This application let you download from my repository **Kubernetes-component-templates**, some kubernetes yaml file templates, such as:

* Deployment template yaml file
* Config template yaml file
* Secret template yaml file
* Service template yaml file

## Requirements

* Python3 environment
* Any Linux/Unix distribution

## Installation

If you want a permanent installation of DirtyOps on your system then ran the following commands:

* `chmod +x install.sh`
* `sudo ./install.sh`

## Getting started

With DirtyOps you have to specify two arguments:
* type of yaml file to download
* directory where the yaml file has to be downloaded

Example:
`dirtyops deployment /home/user/mykubernet-project`

the possible types of yaml file are:
* deployment
* configmap
* service
* secret

