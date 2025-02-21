pipeline{
  agent any
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main',url: 'https://github.com/VasaviGujjula/Vasu.git'
      }
    }
    stage('Build') {
      steps {
        sh 'mvn clean install'
      }
    }
    stage('Test') {
      steps {
        sh 'mvn test'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying application'
      }
    }
  }
  post {
    success {
      echo 'Build and test for success'
    }
    failure {
      echo 'Build or tests failed'
    }
  }
}
      
