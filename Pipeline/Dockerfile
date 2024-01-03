pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
          for n in grafana prometheus jenkins nginx sandbox
          do
            echo j3nK1n\\$@dm1n | su - root -c "docker build -t maxkadyshev/$n:jenkins -f Dockerfile/$n ."
            docker push maxkadyshev/$n:jenkins
          done
        '''
      }
    }
  }
}
