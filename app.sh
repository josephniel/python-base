#!/usr/bin/env bash

function app_start {
    docker-compose up \
        --build \
        --abort-on-container-exit \
        --remove-orphans
}

function app_stop {
    docker-compose down \
        --rmi all \
        --remove-orphans
}

case $1 in
    "start")
        app_start;;
    "stop")
        app_stop;;
esac
