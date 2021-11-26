pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/anish-9999/Jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Fib.py"
                sh "./Fib.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
