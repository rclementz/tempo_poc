FROM ghcr.io/volvo-cars/rdswf-ubuntu-22.04:latest AS builder
WORKDIR tempo_poc/
COPY . . 
ADD  ../.ssh /home/user/.ssh
RUN apt-get update && apt-get install -y \
    python3-pip

FROM ghcr.io/volvo-cars/rdswf-python-3.8:0.1.1
WORKDIR tempo_poc/
COPY . . 
CMD pip3 install -r requirements.txt && python3 src/main.py 