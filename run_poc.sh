docker build -t tempo_poc . 

export TEMPO_TOKEN=$(cat ../tempo_token)
export SSH_KEY=$(cat ~/.ssh/testing)
docker run --rm -it -e TEMPO_TOKEN -e SSH_KEY -e SSH_KEY_TYPE=rsa tempo_poc
