pipeline {
    agent { docker { image 'maven:3.3.3' } }

    stages {
        stage{'log version info') {
            steps {
                git 'https://github.com/sridhar355/prmg.git'
                sh 'mvn --version'
                sh 'mvn clean install'
            }
        }
        stage
        ('Build') {
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
