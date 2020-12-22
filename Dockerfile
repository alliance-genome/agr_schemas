ARG ALLIANCE_RELEASE=build
ARG REG=agrdocker

FROM ${REG}/agr_java_software:${ALLIANCE_RELEASE}

WORKDIR /workdir/agr_java_software/schemas

ADD . .

CMD ["java", "-jar", "/workdir/agr_java_software/agr_schema_validation/target/agr_schema_validation-jar-with-dependencies.jar", "/workdir/agr_java_software/schemas"]
