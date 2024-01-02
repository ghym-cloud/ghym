pipeline {
  agent any
  stages {
    stage('Grafana') {
      steps {
        sh '''
          docker build -t maxkadyshev/grafana:jenkins -f ../Dockerfile/Grafana
          docker push maxkadyshev/grafana:jenkins
        '''
      }
    }
  }
}