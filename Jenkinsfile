pipeline {
    agent any
    stages {
        stage('python docker image') {
            steps {
                sh 'docker pull python:3'
            }
        }
        stage('build') {
            
            agent{
                  docker {
                        image 'python:3'
                        args '-v $WORKSPACE:/demo -u root'
                    }
                }
            steps {
                sh 'cd /demo'
                echo 'pwd'
                sh 'python sample.py'
                archiveArtifacts artifacts: '*.py'
            }
        }
        stage('building image') {
            steps {
                sh 'docker build -t sample .'
            }
        }
        stage('run docker') {
            steps {
                sh 'docker run sample'
            }
        }
    }
    post {
    always {
        cleanWs()
    }
    }
}
