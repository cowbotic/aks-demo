FROM jazzdd/alpine-flask:python3

RUN cd /app
ENV GREET hola
RUN git clone https://github.com/cowbotic/test.git .
