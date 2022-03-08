#!/bin/sh
docker run -d --network=host -p 8055:8055  -v /home/ubuntu/:/home/ubuntu/ -e py_ms_demo:latest
