FROM debian:buster-slim as build

RUN apt-get update -y; apt-get install build-essential -y
ADD shredder.c /tmp/shredder.c
ADD Makefile /tmp/Makefile
RUN cd /tmp/; make all

FROM debian:buster-slim

RUN apt-get update -y; apt-get install socat -y
COPY --from=build /tmp/shredder /pwn/shredder
COPY flag.txt /pwn/flag.txt
WORKDIR /pwn

EXPOSE 6000

ENTRYPOINT ["sh", "-c", "exec socat -s TCP-LISTEN:6000,reuseaddr,fork EXEC:/pwn/shredder,stderr"]
