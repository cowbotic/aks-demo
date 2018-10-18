FROM jazzdd/alpine-flask:python3

RUN cd /app
RUN pip install requests
RUN git clone https://github.com/cowbotic/aks-demo.git .
