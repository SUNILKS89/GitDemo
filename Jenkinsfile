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

                sh '/var/lib/jenkins/workspace/Python Automation/venv/bin/python -m pytest SeleniumPython/test_HomePageTest.py --browser_name=chrome -v'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
