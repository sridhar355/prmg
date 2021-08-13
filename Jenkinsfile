pipeline {
    agent any

    stages {
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
