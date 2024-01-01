pipeline {
  agent any
  stages {
    stage('Grafana') {
      steps {
        def Grafana = docker.build("maxkadyshev/grafana:10.2.3-jenkins", -f "../Dockerfile/Grafana")
        docker.Grafana.push()
      }
    }
  }
}