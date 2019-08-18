#!/bin/bash

docker run -d --rm \
--name movie_server \
-p 8090:80 \
-v /home/pi/docker/nginx/nginx.conf:/etc/nginx/nginx.conf \
-v /home/pi/docker/nginx/default.conf:/etc/nginx/conf.d/default.conf \
-v /STORAGE/incomming:/incomming:ro \
nginx:latest