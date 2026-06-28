pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/Sthompson7/Henry.git'
            }
        }
        stage('Build') {
            steps {
                bat 'docker compose build'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker compose down || exit 0'
                bat 'docker compose up -d'
            }
        }
    }
    post {
        success {
            echo 'Henry Books deployed successfully!'
        }
        failure {
            echo 'Deployment failed. Check logs.'
        }
    }
}