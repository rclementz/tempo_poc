export TEMPO_TOKEN=$(cat ../tempo_token)
docker build -t tempo_poc . 
docker run -it -v "$PWD/.ssh:/home/nonroot/.ssh:ro" --env TEMPO_TOKEN tempo_poc
