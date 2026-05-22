pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'googledriver --version || true'
                sh 'chromium-browser --version || true'
                sh 'which google-chrome || true'
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
