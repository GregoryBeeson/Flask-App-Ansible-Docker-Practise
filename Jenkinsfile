pipeline {
    agent any
    stages{

        stage('Stage 1: Build'){
            steps{

                sh "sudo docker-compose build"
            }
        }

        stage('Stage 2: Run'){
            steps{
                sh "sudo docker-compose up -d"
            }
        }
    }
}