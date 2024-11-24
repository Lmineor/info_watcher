#!/usr/bin/env sh

docker build -t info_watcher:0.0.1 .

docker run -e BARK_KEY=  -e BARK_PORT=  -v /var/log/info_watcher:/var/log/info_watcher info_watcher:0.0.1