pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v /tmp:/tmp'
        }
    }
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Data Generation') {
            steps {
                sh 'python data_generation.py'
            }
        }
        stage('Data Preprocessing') {
            steps {
                sh 'python data_preprocessing.py'
            }
        }
        stage('Model Training') {
            steps {
                sh 'python model_training.py'
            }
        }
        stage('Model Testing') {
            steps {
                sh 'python model_testing.py'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.pkl,*.csv', allowEmptyArchive: true
        }
    }
}