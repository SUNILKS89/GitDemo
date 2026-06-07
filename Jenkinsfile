pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'chromedriver --version || true'
                sh 'google-chrome --version || true'
                sh 'which google-chrome || true'
                sh 'which chromedriver || true'
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                pip install playwright
                playwright install
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
            }
        }

        stage('Test') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pytest PlaywrightPython/Test.py -v -s'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
