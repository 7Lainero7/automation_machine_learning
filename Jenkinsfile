pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-v /tmp:/tmp'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Pipeline') {
            steps {
                sh 'chmod +x pipeline.sh'
                sh './pipeline.sh'
            }
        }
    }
}