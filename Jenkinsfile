pipeline {
    agent any
    stage('Setup Environment') {
        steps {
            sh 'python3 -m venv venv'
            sh '. venv/bin/activate && pip install --upgrade pip'
            sh '. venv/bin/activate && pip install -r requirements.txt'
        }
    }
    stages {
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
