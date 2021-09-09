FROM openjdk:8-jdk-slim

COPY target/*.jar /temp/app.jar

WORKDIR /temp

CMD ["java", "-jar", "app.jar"]
