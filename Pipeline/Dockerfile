pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
          for i in $(ls /var/jenkins_home/workspace/Dockerfile/Dockerfile | grep -v misc)
          do
            echo j3nK1n\\$@dm1n | \
            su - root -c "docker build -t maxkadyshev/$i:latest -f /var/jenkins_home/workspace/Dockerfile/Dockerfile/$i /var/jenkins_home/workspace/Dockerfile/Dockerfile \
            && docker push maxkadyshev/$i:latest"
          done
        '''
      }
    }
  }
}
