pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cicd-app:latest .'
            }
        }

        stage('Load Into Minikube') {
            steps {
                sh 'minikube image load cicd-app'
            }
        }

        stage('Deploy Update') {
            steps {
                sh 'kubectl rollout restart deployment/cicd-app'
            }
        }
    }
}