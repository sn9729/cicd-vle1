pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t cicd-app:latest .'
            }
        }

        stage('Load Image Into Minikube') {
            steps {
                bat '"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe" image load cicd-app'
            }
        }

        stage('Restart Kubernetes Deployment') {
            steps {
                bat 'kubectl rollout restart deployment/cicd-app'
            }
        }
    }
}