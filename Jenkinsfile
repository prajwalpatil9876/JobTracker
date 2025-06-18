pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'pip install --user --break-system-packages -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest'
            }
        }
        stage('Deliver') {
            steps {
                echo 'Delivery step (e.g. Dockerize, SCP, etc.)'
                sh 'echo done'
            }
        }
    }
}
