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
                sh 'docker compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
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