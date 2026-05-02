pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/sn9729/cicd-vle1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sn9729/cicd-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push sn9729/cicd-app:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}