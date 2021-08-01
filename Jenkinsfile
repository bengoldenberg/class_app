def create_namespace(namespace){
echo "Creating namespace ${namespace} if needed"

    sh "[ ! -z \"\$(kubectl get ns ${namespace} -o name 2>/dev/null)\" ] || kubectl create ns ${namespace}"
}

def check_get_curl(path)
{
script{
def result = sh (
                returnStdout: true,
                script: 'curl -s -w %{http_code}} "${path}/school/students"')

if (result.contain(200)){
    ok = "Ok"}
else{
    ok = "not OK"} 
echo ${ok}   
}

}
def check_post_curl(path)
{
script{
def result = sh (
                returnStdout: true,
                script: 'curl -d "{"firstname" :"ben", "lastname": "goldenberg", "id": 2, "class": "D2"}" -H "Content-Type: application/json" -s -w %{http_code}} "${path}/school/students"')
if (result.contain(200)){
    ok = "Ok"}
else{
    ok = "not OK"} 
echo ${ok}   
}
}
def check_put_curl(path)
{
script{
def result = sh (
                returnStdout: true,
                script: 'curl -s -w %{http_code}} -X PUT "${path}/school/students/2/6"')
if (result.contain(200)){
    ok = "Ok"}
else{
    ok = "not OK"} 
echo ${ok}   
}
}


pipeline {
    agent
    {
        kubernetes
        {
           yamlFile 'build_agent.yaml' 
        }
    }
   

    environment {
        path = "http://a5d3e0b657cee4faf92a3cf47293ef03-2024788998.eu-west-2.elb.amazonaws.com"
        REGISTRY = '207457565/school:class'
        
                }
    stages {
        stage("build image") 
        {
            steps {
                git branch: 'master',
                credentialsId: 'github_registry',
                url: 'https://github.com/bengoldenberg/class_app.git'
                container('docker')
                {
                  sh "docker build -t ${REGISTRY} -f Dockerfile ."
                }


                      }
        }

        stage('push image to repo')
        {
            steps
            {
                container('docker')
                {
                    withDockerRegistry([credentialsId: "${docker_hub_registry}", url: "207457565/school"])
                     {
                        sh "docker push ${REGISTRY}"
                     }
                }
            }
        }
        stage('deploy to dev')
        {
            input{
                message "please insert the value file"
                parameters{
                string(name: 'name', defaultValue:'',description: 'the name you want to give')
                string(name: 'chart_name', defaultValue:'', description:'the chart name')
                string(name: 'file', defaultValue:'values.yaml',description: 'the value file of helm chart')}
                }
            steps{
              container('helm'){
                
                script{
                namespace = 'dev'
                create_namespace(namespace)
                    sh ""
                    script: 'helm upgrade --install --wait ${params.name} ${params.chart_name} -f ${params.file}  --namespace $namespace'

                      }
                                 }
                }
        }
        stage('Dev tests')
        {
            container('helm')
            {
            
            parallel {
                stage('Curl get_method')
                {
                    steps {
                        script{
                    is_ok = check_get_curl(${path})
                    echo "the get method is working ${is_ok}"   
                              }  
                          }
                }
                stage('curl post_method')
                {
                    steps{
                        script{
                    is_post_ok == check_post_curl(${path})
                    echo "the post method is working ${is_post_ok}"
                              }
                         }
                }
                stage('curl put_method')
                {
                    steps{
                        script{
                    is_put_ok == check_put_curl(${path})
                    echo "the put method is working ${is_post_ok}"
                              }
                         }
                }

            

                   }
            }       
        }
        stage('cleanup dev')
        {
            steps
            {
                container('helm')
                {
                  script
                  {
                    sh ""
                    script: 'helm delete --purge ${params.name}'
                  }
                }
            }
        }
        stage('deploy production')
        {
            input{
                message "Proceed and deploy to Production?"
                parameters{
                choice(name: 'production', choices: ['yes', 'no'], description: 'do yo want to go production?') 
                          }
                 }
            when {
                 allOf{
                    branch 'master'
                    ${params.production} == 'yes'
                      }   
                 }
                steps
                {
                  container('helm'){
                  
                  script{
                            namespace = 'production'
                            create_namespace(namespace)
                            sh ""   
                            script: 'helm upgrade --install --wait ${params.name} ${params.chart_name} -f ${params.file}  --namespace $namespace'

                        }
                                   }  
                
            }
        }

        
    }
}