#!/bin/bash

set -x

image=xl_python_web_demo
tag=0.0.1
registry=registry.xuelangyun.com/shuzhi-amd64
repo=${registry}/${image}:${tag}

docker build -t ${repo} .
docker push ${repo}
