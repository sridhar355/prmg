pipeline {
    agent any

    stages {
        stage('build_docker') {
            agent{
                docker {
                    image: 'python:3'
                }
            }
            steps {
              sh """
                docker build -t dict .
              """
            }
        }
        stage('run') {
            steps {
                sh """
                  docker run --rm dict
                """
            }
        }
        stage('Build') {
            steps {
                sh 'echo "building.." > ArtFile.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    post
    {
        always
        {
            archiveArtifacts artifacts: 'ArtFile.txt', onlyIfSuccessful: true
        }
    }
}
