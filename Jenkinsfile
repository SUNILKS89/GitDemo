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
                . venv/bin/activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
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
                sh '. venv/bin/activate'
                sh 'pytest SeleniumPython/test_HomePageTest.py --browser_name=chrome -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
