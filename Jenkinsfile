pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Install Chrome dependencies') {
            steps {
                sh '''
                apt-get update
                apt-get install -y \
                    libnss3 \
                    libgconf-2-4 \
                    libatk-bridge2.0-0 \
                    libgtk-3-0 \
                    libxss1 \
                    libasound2
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
