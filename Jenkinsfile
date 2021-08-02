node("jenkins-slave"){
    path = "http://a172c6135e0664f02b3d68cef4c1f1f7-264409871.eu-west-2.elb.amazonaws.com "
    registry = '207457565/school:class'
    properties([
        parameters(
            [
                string(name: 'name',defaultValue:'school',description: 'the name you want to give'),
                string(name: 'chart_name',defaultValue:'school-app', description:'the chart name'),
                string(name: 'file', defaultValue:'values.yaml',description: 'the value file of helm chart')
            ]
        )
    ])  
    
    sh "ls"
    stage("Build"){
        container('docker') {
            checkout scm
            sh "docker build -t ${registry} -f Dockerfile ."
            withDockerRegistry([credentialsId: "docker_hub_registry"])
            {
                sh "docker push ${registry}"
            }
        }
    }

    stage("test"){
        stage("deploy to dev")
        {
            node("jenkins-helm")
            {
                container('helm')
                {
                namespace = 'dev'
                create_namespace(namespace)
                sh "helm upgrade --install --wait ${name} ${chart_name} -f ${file}  --namespace ${namespace}"
                }
            }
        }
    }

    stage("Deploy to Prod"){
        
    }
}





def create_namespace(namespace){
echo "Creating namespace ${namespace} if needed"

    sh "[ ! -z \"\$(kubectl get ns ${namespace} -o name 2>/dev/null)\" ] || kubectl create ns ${namespace}"
}