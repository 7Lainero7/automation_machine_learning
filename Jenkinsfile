pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v /tmp:/tmp --user root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Pipeline') {
            steps {
                sh 'chmod +x pipeline.sh'
                sh './pipeline.sh'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.pkl,*.csv,*.json', allowEmptyArchive: true
        }
    }
}