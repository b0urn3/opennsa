#!/bin/bash

# Clean old stuff
docker-compose -p vtncoordinator stop
docker-compose -p vtncoordinator rm -f
docker rm -f $(docker ps -qa)
docker rmi -f $(docker images -qa)

# Make it run ;), docker build is done through docker compose
docker-compose -p vtncoordinator up

#HOST=`docker inspect opennsa_db_1 | grep "IPAddress\"" | cut -d "\"" -f4`
HOST=10.10.10.96
#DB="opennsa"
#USER="opennsa"

# Show that it is ok :)
docker-compose -p vtncoordinator ps

