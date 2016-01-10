FROM ubuntu:latest

MAINTAINER Robert Zahradníček <robert.zahradnicek@b.cz>

# Remove the cache information. This helps eliminate "hash sum" errors when doing an update
# which may be caused when mirrors and caches are out of sync.
RUN rm -fR /var/lib/apt/lists/*
RUN mkdir /var/lib/apt/lists/partial

# Install OpenJDK 7 in headless mode and Maven
RUN apt-get clean && \
    apt-get update && \
    apt-get -y install pkg-config gcc make unzip wget ant g++ git libboost-dev libcurl4-openssl-dev \
    libjson0-dev libssl-dev openjdk-7-jre-headless openjdk-7-jdk unixodbc-dev xmlstarlet git \
    postgresql-9.3 postgresql-client-9.3 postgresql-client-common postgresql-contrib-9.3 odbc-postgresql && \
    apt-get clean

RUN apt-get -y install python-software-properties software-properties-common
RUN add-apt-repository ppa:andrei-pozolotin/maven3 && apt-get update && apt-get -y install maven3

# Shortcut command for grabbing settings.xml from OpenDaylight
# RUN cp -n ~/.m2/settings.xml ~/.m2/settings.xml.orig
RUN mkdir ~/.m2; \
    wget -q -O - https://raw.githubusercontent.com/opendaylight/odlparent/master/settings.xml > ~/.m2/settings.xml

# Download OpenDaylight and install VTN Coordinator
RUN git clone https://git.opendaylight.org/gerrit/p/vtn.git /usr/local/vtn
RUN cd /usr/local/vtn && \
    git checkout stable/lithium && \
    cd coordinator && \
    mvn -f dist/pom.xml install
RUN tar -C/ -jxvf /usr/local/vtn/coordinator/dist/target/distribution.vtn-coordinator-6.1.4-SNAPSHOT-bin.tar.bz2

EXPOSE 8083

#CMD /usr/local/vtn/sbin/db_setup && /usr/local/vtn/bin/vtn_start
#ENTRYPOINT /bin/bash


