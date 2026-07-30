@Library('Shared') _
pipeline {
    agent any

    environment {
        SONAR_HOME = tool "Sonar"
    }
    
    parameters {
        string(name: 'DOCKER_TAG', defaultValue: '', description: 'Setting docker image for latest push')
       
    }
    
    stages {

        stage("Validate Parameters") {
            steps {
                script {
                    if (!params.DOCKER_TAG) {
                        error("DOCKER_TAG must be provided.")
                    }
                }
            }
        }

        stage('Git: Code Checkout') {
            steps {
                script {
                    code_checkout(
                        "https://github.com/LondheShubham153/Wanderlust-Mega-Project.git",
                        "main"
                    )
                }
            }
        }

        stage("Trivy: Filesystem scan") {
            steps {
                script {
                    trivy_scan()
                }
            }
        }

        stage("OWASP: Dependency check") {
            steps {
                script {
                    owasp_dependency()
                }
            }
        }

        stage("SonarQube: Code Analysis") {
            steps {
                script {
                    sonarqube_analysis("Sonar", "webmart", "webmart")
                }
            }
        }

        stage("SonarQube: Code Quality Gates") {
            steps {
                script {
                    sonarqube_code_quality()
                }
            }
        }
        
        stage("Docker build"){
            steps{
                script{
                    docker_build("django-app","${params.DOCKER_TAG}","tarasankar393")
                }
            }
        }
        
        stage("Docker push"){
            steps{
                script{
                    docker_push("django-app","${params.DOCKER_TAG}","tarasankar393")
                }
            }
        }
    }
    post {
        success {
            echo "CI Pipeline completed successfully"
            build job: "webmart-CD", parameters:[
              string(name:"DOCKER_TAG", value:"${params.DOCKER_TAG}")
            ]
        }
        failure {
            echo "CI Pipeline failed"
        }
    }
}