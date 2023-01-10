build:
	docker build . -t django-project-template -f docker/Dockerfile

run:
	docker run -p 8001:8001 -ti --rm django-project-template
