.PHONY: run
run: build
	@docker run agrdocker/agr_schemas:latest

.PHONY: build
build: pull
	@docker build -t agrdocker/agr_schemas:latest .

.PHONEY: pull
pull:
	@docker pull agrdocker/agr_java_software:build


