## Docker
docker_build:
	docker build -t suzano-challenge-448218 .

docker_run:
	docker run -p 8000:8000 suzano-challenge-448218