node("jenkins-slave"){
    checkout scm
    sh "ls"
    stage("Build"){
        container('docker') {
            sh "docker ps"
        }
    }

    stage("Test"){
        
    }

    stage("Deploy to Prod"){
        
    }
}



