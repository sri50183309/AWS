# AWS Steps 

# Day 1 (Account Creation, SDK, IntelliJ PlugIn, CLI)

  - Created a free tier user in https://signin.aws.amazon.com
  -     * It asks for a credit card to verify the name and phone number to send text (Hopefully no extra charge      
  * [Install AWS in IntelliJIdea](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-toolkit.html) This will setup IntellIj to work with aws account
      * In that process , we will creating a IAM User Group and also access keys
  - Installed AWS CLI in Windows
  - > Test aws --version in your command promt
  
# Day 2 (SAM/Lamda, Regions, IntelliJ Integration)
  - Region
	- * Works with regional end point
		polly.us-west-2.amazonaws.com/v1/speech
		<<Service>> <Region>			<API Action>
	- *	Regions with lexicons (lexicons works only with regions, # (need to explore more))	
	- * [Installing AWS SAM CLI] (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html)
	- *[HelloWorld sam] (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)
	- * SAM deploy --guided failed
			- * No configuration for access key id / secret key
			- * Provide access key by 
					command -> aws configure
	- * Deploy seems to be working (Note run the deploy command inside build directory of the project)
	- * Came to IntelliJ, opened the AWS Explorer and passed the secret key and access key combination.
	- * Able to view my AWS details in IntelliJ
	- [IntelliJ Link] (https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/key-tasks.html#key-tasks-first-connect)
	- * Deployed using IntelliJ
				
				
	
