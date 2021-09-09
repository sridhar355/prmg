pipeline {
    agent any
    
    stages {
        stage('docker pull') {
            steps {
                sh 'docker pull maven:3.8.2-openjdk-11'
                sh 'docker pull openjdk:8-jdk-slim'
            }
        }
        stage('build') {
            
            agent{
                  docker {
                        image 'maven:3.8.2-openjdk-11'
                        args '-v $WORKSPACE:/shared-volume -u root'
                    }
                }
            steps {
                sh 'cd /shared-volume'
                sh 'mvn clean install'
                echo 'Creating Artifacts..'
                archiveArtifacts artifacts: 'target/*.jar'
            }
        }
        stage('building docker') {
            steps {
                sh 'docker build -t jar-executor .'
            }
        }
        stage('running docker') {
            steps {
                sh 'docker run jar-executor'
            }
        }
    }
    post {
        always{
            cleanWs()
         }
    }
}
