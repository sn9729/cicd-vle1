pipeline {
    agent any

    environment {
        IMAGE_NAME = "cicd-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Load Image Into Minikube') {
            steps {
                bat "\"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe\" image load %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy New Version') {
            steps {
                bat "kubectl set image deployment/cicd-app cicd-app=%IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Wait For Rollout') {
            steps {
                bat "kubectl rollout status deployment/cicd-app"
            }
        }
    }
}