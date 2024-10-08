pipeline {
    agent any // Use your agent here with installed package manager (npm, go, python, etc.)

    triggers {
        GenericTrigger(
            genericVariables: [
                // GitHub
                [key: 'JF_GIT_REPO', value: '$.repository.name'],
                [key: 'JF_GIT_PULL_REQUEST_ID', value: '$.number'],
                [key: 'JF_GIT_OWNER', value: '$.pull_request.user.login'],
                [key: 'TRIGGER_KEY', value: '$.action'],
                // Add other VCS triggers if needed
            ],
            causeString: 'Pull Request Trigger',
            printContributedVariables: false,
            token: 'MyJobToken'
        )
    }

    environment {
        // [Mandatory]
        JF_GIT_PROVIDER = "github"
        JF_URL = "https://kimt.jfrog.io"
        JF_ACCESS_TOKEN = credentials("JF_ACCESS_TOKEN") 
        JF_GIT_TOKEN = credentials("JF_GIT_TOKEN")
        JF_RELEASES_REPO = ""
        JF_GIT_OWNER = "JfrogEden"
        JF_GIT_REPO = "todo_from_chat"
        JF_GIT_PULL_REQUEST_ID = "1"
        JF_GIT_BASE_BRANCH = "main"
        PYTHON_ENV = "venv"
        JF_INSTALL_DEPS_CMD = "pip install"
        JFROG_CLI_LOG_LEVEL=DEBUG
        // [Mandatory for on-premise]
        JF_GIT_API_ENDPOINT = "https://api.github.com/"
    }
    stages {
        
        //stage('Check Python Installation') {
        //    steps {
        //        script {
        //            sh 'python3 --version || echo "Python3 not found"'
        //            sh 'pip3 --version || echo "Pip3 not found"'
        //        }
        //    }
        //}
        //
        //stage('Install Python and Pip') {
        //    steps {
        //        script {
        //            sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv'
        //        }
        //    }
        //}       
        //
        //stage('Install Dependencies') {
        //    steps {
        //        script {
        //            // Install virtualenv
        //            sh 'pip install virtualenv'
        //            // Verify installation
        //            sh 'which virtualenv'
        //        }
        //    }
        //}
        
        //withPythonEnv('/home/edenb/python-example/venv/bin/python'){
        //}

        stage('Download Frogbot') {
            steps {
                script {
                    echo 'On linux or MacOS'
                    sh """ curl -fLg "https://releases.jfrog.io/artifactory/frogbot/v2/[RELEASE]/getFrogbot.sh" | sh"""
                }
            }
        }
        
        stage('Scan Repository') {
            steps {
                sh "./frogbot scan-repository"
                //sh "./frogbot scan-repository"
            }
        }
        
        stage('Scan Pull Request') {
            steps {
                sh "./frogbot scan-pull-request"
            }
        }
        
        //stage('Set Up Python Environment') {
        //    steps {
        //        script {
        //            // Create virtual environment
        //            sh "python3 -m venv $env.PYTHON_ENV"
        //            // Activate virtual environment and install dependencies
        //            sh """
        //                source $env.PYTHON_ENV/bin/activate
        //               pip3 install -r requirements.txt
        //            """
        //        }
        //    }
        //}

        //stage('Run Python Script') {
        //    steps {
        //        script {
        //            // Activate virtual environment and run your Python script
        //            sh """
        //                source $env.PYTHON_ENV/bin/activate
        //                python your_script.py
        //            """
        //        }
        //    }
        //}
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

