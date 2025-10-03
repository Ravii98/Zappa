pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = "ap-south-2"     // change as needed
        S3_BUCKET = "my-lambda-artifacts-ravi"    // create this bucket in S3 first
        LAMBDA_NAME = "zappa-poc-lambda"        // create this Lambda function in console
        ZIP_FILE = "lambda_code_${env.BUILD_NUMBER}.zip"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies and Package') {
            steps {
                sh '''
                mkdir -p package
                pip install -r requirements.txt --target ./package
                cp -r zappa ./package/
                cd package
                zip -r ../$ZIP_FILE .
                cd ..
                '''
            }
        }

        stage('Upload to S3') {
            steps {
                sh 'aws s3 cp $ZIP_FILE s3://$S3_BUCKET/$ZIP_FILE'
            }
        }

        stage('Deploy to Lambda') {
            steps {
                sh '''
                aws lambda update-function-code \
                    --function-name $LAMBDA_NAME \
                    --s3-bucket $S3_BUCKET \
                    --s3-key $ZIP_FILE
                '''
            }
        }
    }
}
