pipeline {
    agent {
        docker { image 'python' }
    }

    stages {
        stage('build_docker') {
            steps {
              sh """
                docker build -t dict .
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
