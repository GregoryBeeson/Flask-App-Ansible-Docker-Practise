pipeline {
    agent any
    stages{

        stage('Stage 0: Build'){
            steps{

                sh "docker-compose build"
            }
        }

        stage('Stage 1: Run'){
            steps{
                sh "docker-compose up -d"
            }
        }
    }
}