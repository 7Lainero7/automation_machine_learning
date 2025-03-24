pipeline {
    agent any

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    docker.image('python:3.9').inside('-v /tmp:/tmp') {
                        stage('Install dependencies') {
                            sh 'pip install -r requirements.txt'
                        }
                        stage('Data Generation') {
                            sh 'python data_generation.py'
                        }
                        stage('Data Preprocessing') {
                            sh 'python data_preprocessing.py'
                        }
                        stage('Model Training') {
                            sh 'python model_training.py'
                        }
                        stage('Model Testing') {
                            sh 'python model_testing.py'
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.pkl,*.csv', allowEmptyArchive: true
        }
    }
}