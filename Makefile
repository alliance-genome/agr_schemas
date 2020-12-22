REG := 100225593120.dkr.ecr.us-east-1.amazonaws.com

registry-docker-login:
ifneq ($(shell echo ${REG} | egrep "ecr\..+\.amazonaws\.com"),)
	@$(eval DOCKER_LOGIN_CMD=aws)
ifneq (${AWS_PROFILE},)
	@$(eval DOCKER_LOGIN_CMD=${DOCKER_LOGIN_CMD} --profile ${AWS_PROFILE})
endif
	@$(eval DOCKER_LOGIN_CMD=${DOCKER_LOGIN_CMD} ecr get-login-password | docker login -u AWS --password-stdin https://${REG})
	${DOCKER_LOGIN_CMD}
endif

.PHONY: run
run: build
	@docker run agrdocker/agr_schemas:latest

.PHONY: build
build: pull
	@docker build -t agrdocker/agr_schemas:latest --build-arg REG=${REG} .

.PHONEY: pull
pull: registry-docker-login
	@docker pull ${REG}/agr_java_software:build


