## Docker
docker_build:
	docker build -t suzano-challenge-448218 .

docker_run:
	docker run -p 4444:4444 suzano-challenge-448218