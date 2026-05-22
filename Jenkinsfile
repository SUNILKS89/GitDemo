pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'chromedriver --version || true'
                sh 'google-chrome --version || true'
                sh 'which google-chrome || true'
                sh 'which chromedriver || true'
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
