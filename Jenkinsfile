pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
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