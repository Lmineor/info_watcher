#!/usr/bin/env sh

docker build -t info_watcher:0.0.1 .

docker-compose -f docker-compose.yaml down
docker-compose -f docker-compose.yaml up -d