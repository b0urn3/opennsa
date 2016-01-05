#!/bin/bash

# Clean old stuff
docker-compose -p opennsa stop
docker-compose -p opennsa rm -f
docker rmi -f opennsa_db
#docker rmi -f $(docker images -qa)

# Make it run ;), docker build is done through docker compose
docker-compose -p opennsa up -d

#HOST=`docker inspect opennsa_db_1 | grep "IPAddress\"" | cut -d "\"" -f4`
HOST=10.10.10.96
DB="opennsa"
USER="opennsa"

# Show that it is ok :)
docker-compose -p opennsa ps

