pipeline {
  agent any
  stages {
    stage('Grafana') {
      steps {
        def Grafana = docker.build("maxkadyshev/grafana -t jenkins -f ../Dockerfile/Grafana")
        docker.Grafana.push()
      }
    }
  }
}