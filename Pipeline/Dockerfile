pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
          for n in Grafana Prometheus Jenkins Nginx Sandbox
          do
            echo j3nK1n\$@dm1n | su - root -c "docker build -t maxkadyshev/$n:jenkins -f ../Dockerfile/$n ../Dockerfile"
            docker push maxkadyshev/$n:jenkins
          done
        '''
      }
    }
  }
}
