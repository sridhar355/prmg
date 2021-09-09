pipeline {
    agent any
    stages {
        stage('python docker image') {
            steps {
                sh 'docker pull python:3.7-alpine'
            }
        }
        stage('build') {
            
            agent{
                  docker {
                        image 'python:3.7-alpine'
                        args '-v $WORKSPACE:/demo -u root'
                    }
                }
            steps {
                sh 'cd /demo'
                echo 'pwd'
                echo 'ls'
                sh 'python hello.py'
                archiveArtifacts artifacts: '*.py'
            }
        }
        stage('building image') {
            steps {
                echo "Creating image to run the py file"
                sh 'docker build -t runpy .'
            }
        }
        stage('run docker') {
            steps {
                echo "Running the container to see output of py file"
                sh 'docker run runpy'
            }
        }
    }
    post {
    always {
        cleanWs()
    }
    }
}
