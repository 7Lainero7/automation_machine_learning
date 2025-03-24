pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '--user root -v /tmp:/tmp'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python -m ensurepip --upgrade
                python -m pip install --upgrade pip
                pip install virtualenv
                python -m virtualenv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pipeline') {
            steps {
                sh '''
                chmod +x pipeline.sh
                . venv/bin/activate
                ./pipeline.sh
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.pkl,*.csv,*.json', allowEmptyArchive: true
        }
    }
}