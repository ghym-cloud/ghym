pipeline {
  agent any
  stages {
    stage('Grafana') {
      steps {
        script {
          def Grafana = docker.build("maxkadyshev/grafana -t jenkins -f ../Dockerfile/Grafana")
          Grafana.push()
      }
    }
  }
}