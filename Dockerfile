ARG REG=agrdocker
ARG DOCKER_PULL_TAG=build

FROM ${REG}/agr_java_software:${DOCKER_PULL_TAG}

WORKDIR /workdir/agr_java_software/schemas

ADD . .

CMD ["java", "-jar", "/workdir/agr_java_software/agr_schema_validation/target/agr_schema_validation-jar-with-dependencies.jar", "/workdir/agr_java_software/schemas"]
