pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }

    environment {
        PATH = "$HOME/.local/bin:$PATH"
        PYTHONPATH = "${env.WORKSPACE}" // Make PYTHONPATH globally available
    }

    triggers {
        pollSCM('H/2 * * * *')  // Poll every 2 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo '📦 Building project...'
                sh 'pip install --user --break-system-packages -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh 'pytest'
            }
        }

        stage('Deliver') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo '🚀 Delivering...'
                sh 'echo Deployment step here.'
            }
        }
    }
}
