FROM docker.io/postgres:latest

MAINTAINER Robert Zahradníček <robert.zahradnicek@b.cz>

ADD init.sql /docker-entrypoint-initdb.d/01_init.sql
ADD schema.sql /docker-entrypoint-initdb.d/02_schema.sql

ENV POSTGRES_USER="opennsa"

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]


