pipeline {
    agent any
    stages{

        stage('Stage 0: Remove Images'){
            steps{
                sh "docker-compose down --rmi all"
            }
        }

        stage('Stage 1: Build'){
            steps{

                sh "docker-compose build"
            }
        }

        stage('Stage 2: Run'){
            steps{
                sh "docker-compose up"
            }
        }
    }
}