pipeline {
    agent any

    stages {

        stage('Source') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build Docker CI Environment') {
            steps {
                bat 'docker build -t calculator-ci .'
            }
        }

        stage('Install Dependencies and Unit Tests') {
            steps {
                bat 'docker run --rm -v "%CD%:/workspace" -w /workspace calculator-ci pip install -r requirements.txt'
                bat 'docker run --rm -v "%CD%:/workspace" -w /workspace calculator-ci python -m pytest'
            }
        }

        stage('SAM Validate') {
            steps {
                bat 'docker run --rm -v "%CD%:/workspace" -w /workspace calculator-ci sam validate --template-file template.yaml --region ap-south-1'
            }
        }

        stage('SAM Build') {
            steps {
                bat 'docker run --rm -v "%CD%:/workspace" -w /workspace calculator-ci sam build --region ap-south-1'
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
