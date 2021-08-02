node("jenkins-slave"){
    path = "http://a172c6135e0664f02b3d68cef4c1f1f7-264409871.eu-west-2.elb.amazonaws.com "
    registry = '207457565/school:class'
    properties([
        parameters(
            [
                string(name: 'name',description: 'the name you want to give'),
                string(name: 'chart_name', description:'the chart name'),
                string(name: 'file', defaultValue:'values.yaml',description: 'the value file of helm chart')
            ]
        )
    ])  
    
    sh "ls"
    stage("Build"){
        container('docker') {
            checkout scm
            sh "docker build -t ${registry} -f Dockerfile ."
        }
    }

    stage("Test"){
        
    }

    stage("Deploy to Prod"){
        
    }
}



