# AWS Steps 

# Day 1 (Account Creation, SDK, IntelliJ PlugIn, CLI)

  - Created a free tier user in https://signin.aws.amazon.com
  - It asks for a credit card to verify the name and phone number to send text (Hopefully no extra charge      
   [Install AWS in IntelliJIdea](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/setup-toolkit.html) This will setup IntellIj to work with aws account
	In that process , we will creating a IAM User Group and also access keys
		- Installed AWS CLI in Windows
		- > Test aws --version in your command promt
  
# Day 2 (SAM/Lamda, Regions, IntelliJ Integration)
  - Region
	- Works with regional end point
		polly.us-west-2.amazonaws.com/v1/speech
		<<Service>> <Region>			<API Action>
	-	Regions with lexicons (lexicons works only with regions, # (need to explore more))	
	- [Installing AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html)
	-[HelloWorld sam] (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html)
	- SAM deploy --guided failed
			- No configuration for access key id / secret key
			- Provide access key by 
					command -> aws configure
	- Deploy seems to be working (Note run the deploy command inside build directory of the project)
	- Came to IntelliJ, opened the AWS Explorer and passed the secret key and access key combination.
	- Able to view my AWS details in IntelliJ
	- [IntelliJ Link](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/key-tasks.html#key-tasks-first-connect)
	- Deployed using IntelliJ

# Day 3(AWS Account users, IAM, IAM Policies,EC2)	
	- Dont use the root users access id and keys. Create a separate user and group for development purposes.
	- Excerise -> IAM Admin group and user
	- Registration with the book in sybex website and registered the book and created the profile.
	- EC2 Elastic COmpute Cloud, instance types
	- Storage
		Persistent Storage -> Amazon EBS Volumes(Elastic Bean Store)
		Temparory Storage -> Instance Store local to host machine itself.
	- AMI Amazon Machine Image (Provide OS and software with attached storage volumes)
		
# Day 4(Amazon Elastic Cloud Computing, EC2)
	- Instance Types (Little bit, need further study )
	- Storage (Little bit, need further study)

# Day 5 (Amazon Virtual Private Cloud , VPC)
	- Route Tables, IPs
	- Service Groups
	- NACL(Network access control list)
	- NAT (Network Address Translation)
	- DHCP (Dyamic Host COnfiguration Protocol)
	- Excerises Tips:
		While doing ssh, i have to go and select ppk in Putty , Putty Configuration > Connection > SSH > Auth > "Private key file for authentication"
	
# Day 6 (Review - Amazon EC2, VPC(Day 4 and 5 activity))

# Day 7 (Amazon Storage)
	- Storage Fundamentals (Different Type of Storage, Design Consideration)
	- CIA Model

# Day 8 (Amazon Storage Contd)
	- EBS Volume, performance
	- Instance Store
	- S3
	- Object facets, tagging
	
# Day 9 (Amazon Storage Contd)
	- Storage Classes
	- Consistency Model
	- Encryption concepts
	- Access Control
	- Data lake
	
# Day 10 (Amazon Storage Contd)
	- Storage Use cases
	- AWS Storage gateway options
	- Performance
	- EFS
# Day 11 (Hello Databases)
	- Types of Databases
	- Characterisitics of relational DB, Scaling, Encryption
	- Aurora
# Day 12 (Database Contd)
	- Non relational DB
	- Dynamo DB
	- Indexing in Dynamo (GSI Global Secondary Index, LSI Local Secondary Index)
# Day 13 (Database contd)
	- Dynamo DB Stream
	- ThroughPut/Throtling
	- Dataware House
# Day 14 (Database Contd)
	- Red Shift, Red Shift Spectrum
	- In Memory Data store (Elastic Cache)
	- Dynamo DB Accelarator, Amazon Neptune
	
				
				
	
