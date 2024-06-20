UNAME_P := $(shell uname -p)
ARC = 'x86_64'
DOCKER_FILE = 'Dockerfile'
ifneq ($(filter arm%,$(UNAME_P)),)
	ARC = 'ARM'
	DOCKER_FILE = 'Dockerfile.arm64v8'
endif


build:
	docker-compose build

up:
	docker-compose up