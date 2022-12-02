export TEMPO_TOKEN=$(cat ../tempo_token)
docker build -t tempo_poc . 
docker run -it -v $pwd/.ssh:/home/user/.ssh:ro --env TEMPO_TOKEN tempo_poc
