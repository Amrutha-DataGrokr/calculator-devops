pipeline {
    agent {
        docker {
            image 'public.ecr.aws/sam/build-python3.12:latest'
        }
    }

    stages {
        stage('Verify Docker Agent') {
            steps {
                sh 'python --version'
                sh 'pytest --version'
                sh 'sam --version'
                sh 'pwd'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'python -m pytest'
            }
        }

        stage('SAM Validate') {
            steps {
                sh 'sam validate --template-file template.yaml'
            }
        }

        stage('SAM Build') {
            steps {
                sh 'sam build'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }

        failure {
            echo 'CI pipeline failed'
        }
    }
}
