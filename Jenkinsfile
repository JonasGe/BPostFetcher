pipeline {
  agent {
    docker {
      image 'frolvlad/alpine-python3'
    }

  }
  stages {
    stage('dependencies') {
      steps {
        echo 'I detected a change in the force...'
      }
    }

    stage('Next step') {
      agent {
        docker {
          image 'frolvlad/alpine-python3'
        }

      }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        echo 'Done'
      }
    }

  }
}