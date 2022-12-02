FROM ghcr.io/volvo-cars/rdswf-python-3.8:0.1.0
WORKDIR tempo_poc/
COPY . . 
#Install pip 
RUN apt-get update && apt-get install -y \
    python3-pip
CMD pip3 install -r requirements.txt && python3 src/main.py 