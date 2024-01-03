pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
          foreach n ( Grafana Prometheus Jenkins Nginx Sandbox )
            docker build -t maxkadyshev/$n:jenkins -f ../Dockerfile/$n ../Dockerfile
            docker push maxkadyshev/$n:jenkins
          end
        '''
      }
    }
  }
}
