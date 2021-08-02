node("jenkins-slave"){
    path = "a9e890b95691f48ff976655669e48df7-1804216955.eu-west-2.elb.amazonaws.com "
    registry = '207457565/school:class'
    properties([
        parameters(
            [
                string(name: 'name',defaultValue:'school',description: 'the name you want to give'),
                string(name: 'chart_name',defaultValue:'school-app', description:'the chart name'),
                string(name: 'file', defaultValue:'school-app/values.yaml',description: 'the value file of helm chart')
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
                namespace = 'dev'
                container('helm')
                {
                checkout scm
                sh "helm upgrade --install --wait ${name} ${chart_name} -f ${file}  --namespace ${namespace}"
                }
            }
        }

                stage('Curl get_method')
                {
                    is_ok = check_get_curl("${path}")
                    echo "the get method is working ${is_ok}"   
                                
                }
                stage('curl post_method')
                {

                    is_post_ok == check_post_curl("${path}")
                    echo "the post method is working ${is_post_ok}"
                              
                }
                stage('curl put_method')
                {
                   
                    is_put_ok == check_put_curl("${path}")
                    echo "the put method is working ${is_post_ok}"                       

                }
    }

    stage("Deploy to Prod"){
        
    }
}

def check_get_curl(path)
{
    def result = sh (
                    returnStdout: true,
                    script: 'curl -s -w %{http_code} "${path}/school/students"')

    if (result.contain(200)){
        ok = "Ok"}
    else{
        ok = "not OK"} 
    echo "${ok}"   
}

def check_post_curl(path)
{

    def result = sh (
                    returnStdout: true,
                    script: 'curl -d "{"firstname" :"ben", "lastname": "goldenberg", "id": 2, "class": "D2"}" -H "Content-Type: application/json" -s -w %{http_code} "${path}/school/students"')
    if (result.contain(200)){
        ok = "Ok"}
    else{
        ok = "not OK"} 
    echo "${ok}"   
}

def check_put_curl(path)
{

    def result = sh (
                    returnStdout: true,
                    script: 'curl -s -w %{http_code} -X PUT "${path}/school/students/2/6"'
                    )
    if (result.contain(200)){
        ok = "Ok"}
    else{
        ok = "not OK"} 
    echo "${ok}"   
}




// def create_namespace(namespace)
// {
//     container('kubectl')
//     {
//         echo "Creating namespace ${namespace} if needed"

//         sh "[ ! -z \"\$(kubectl get ns ${namespace} -o name 2>/dev/null)\" ] || kubectl create ns ${namespace}"
//     }
// }