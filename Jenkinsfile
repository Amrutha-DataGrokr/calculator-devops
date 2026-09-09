pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }

    stages {
        stage('Source') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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
