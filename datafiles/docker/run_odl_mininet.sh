#!/usr/bin/env bash

# Run OpenDaylight controller for accessing via web ui to view topology and flows
docker run --rm --name odl -p 8080:8080 opendaylight/base-edition
# Run mininet in privileged mode with linked OpenDaylight controller and start bash for running commands inside
docker run --privileged -it --rm --name mininet --hostname mininet --link odl:odl ciena/mininet /bin/bash
