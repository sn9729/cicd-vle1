pipeline {
    agent any

    stages {

        stage('Clone Latest Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/sn9729/cicd-vle1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-app:latest .'
            }
        }

        stage('Load Into Minikube') {
            steps {
                bat 'minikube image load cicd-app'
            }
        }

        stage('Deploy Update') {
            steps {
                bat 'kubectl rollout restart deployment/cicd-app'
            }
        }
    }
}