node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
        }
        stage ('Build') {
        	sh """
			virtualenv venv
			virtualenv --relocatable venv 
			pip install -r ./requirements.txt
			pip install -e .
			"""
        }
        stage ('Tests') {
	        sh """
			. venv/bin/activate
			pip install -r ./requirements.txt
			pip install -e .
			python venv/bin/pytest /test
			"""
        }
      	stage ('Deploy') {
            sh "echo 'shell scripts to deploy to server...'"
      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}


