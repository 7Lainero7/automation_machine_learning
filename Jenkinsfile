pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Pipeline') {
            steps {
                sh 'chmod +x pipeline.sh'
                sh '. venv/bin/activate && ./pipeline.sh'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.pkl,*.csv,*.json', allowEmptyArchive: true
        }
    }
}