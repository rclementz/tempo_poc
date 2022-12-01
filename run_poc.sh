docker build -t tempo_doc . ""
docker run -v $pwd/.ssh:/home/user/.ssh:ro --env TEMPO_TOKEN tempo_poc
