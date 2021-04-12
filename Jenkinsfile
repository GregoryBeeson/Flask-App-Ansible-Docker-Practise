pipeline {
    agent any
        environment{
            DATABASE_URI = credentials("DATABASE_URI")
        }
    stages{

        stage('Stage 1: Test')
        {
            sh "echo place holder"
        }

        stage('Stage 2: Build')
        {
            steps{

                sh "sudo docker-compose build"
            }
        }

        stage('Stage 3: Push')
        {
            steps{
                sh "docker-compose push"
            }
        }

        stage('Stage 4: Ansible')
        {
            steps{
                sh "/home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }

        stage('Stage 5: Run')
        {
            steps{
                sh "sudo docker-compose up -d"
            }
        }
    }
}