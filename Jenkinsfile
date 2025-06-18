pipeline {
    agent any

    environment {
        PATH = "$HOME/.local/bin:$PATH"
    }

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
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo 'Delivering...'
                sh 'echo Deployment step here.'
            }
        }
    }
}
