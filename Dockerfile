FROM ghcr.io/volvo-cars/rdswf-python-3.8:0.1.0

WORKDIR tempo_poc/

# TODO: pip3 should be in rwswf-python-3.8
RUN apt-get update && apt-get install -y --no-install-recommends python3-pip

COPY requirements.txt . 
RUN pip3 install --no-cache-dir -r requirements.txt 

COPY . . 

ENTRYPOINT [ "/nonroot/tempo_poc/docker_entrypoint.sh" ]
CMD ["python3", "-u", "src/main.py"]

USER nonroot
