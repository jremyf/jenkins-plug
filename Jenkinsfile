pipeline {
    agent {
    node {
        label 'my-defined-label'
        customWorkspace '/some/other/path'
	stages {
		stage('build') {
		    steps {
		        sh 'python --version'
		    }
		}
	    }
    }
}
    
}
