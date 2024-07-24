print("Welcome to Quizz Competition..")

player = input("Do you want to participate in the competition (yes/no)? ")
if player.lower() != "yes":
    quit()

print("Let's Start the Play...")

score = 0

Question = input("What is the default port number for PostgreSQL database connections?\n"
                 "a) 3306\nb) 1433\nc) 5432\nd) 1521\n"
                 "Your answer: ")
if Question.lower() == "c":
    print("Correct....")
    score += 1
else:
    print("Wrong")

Question = input("Which AWS service is used to securely store and manage secrets such as database credentials?\n"
                 "a) AWS IAM\nb) AWS Secrets Manager\nc) AWS Lambda\nd) AWS CloudWatch\n"
                 "Your answer: ")
if Question.lower() == "b":
    print("Correct...")
    score += 1
else:
    print("Wrong")

Question = input("Which protocol does SSH use for secure communication?\n"
                 "a) FTP\nb) HTTP\nc) TCP\nd) UDP\n"
                 "Your answer: ")
if Question.lower() == "c":
    print("Correct")
    score += 1
else:
    print("Wrong")

Question = input("In Docker, what command is used to list all running containers?\n"
                 "a) docker ps\nb) docker ls\nc) docker list\nd) docker run\n"
                 "Your answer: ")
if Question.lower() == "a":
    print("Correct")
    score += 1
else:
    print("Wrong")

Question = input("What is the primary purpose of Kubernetes?\n"
                 "a) Container orchestration\nb) Virtual machine management\nc) Continuous integration\nd) Source code versioning\n"
                 "Your answer: ")
if Question.lower() == "a":
    print("Correct...")
    score += 1
else:
    print("Wrong")

Question = input("In Ansible, what is a playbook?\n"
                 "a) A collection of tasks\nb) A single task\nc) A script file\nd) A configuration file\n"
                 "Your answer: ")
if Question.lower() == "a":
    print("Correct..")
    score += 1
else:
    print("Wrong")

Question = input("What does CI/CD stand for?\n"
                 "a) Continuous Improvement / Continuous Development\nb) Continuous Integration / Continuous Delivery\nc) Continuous Implementation / Continuous Deployment\nd) Continuous Inspection / Continuous Distribution\n"
                 "Your answer: ")
if Question.lower() == "b":
    print("Correct")
    score += 1
else:
    print("Wrong")

Question = input("Which command is used to create a new branch in Git?\n"
                 "a) git branch new_branch\nb) git checkout new_branch\nc) git create new_branch\nd) git switch new_branch\n"
                 "Your answer: ")
if Question.lower() == "a":
    print("Correct...")
    score += 1
else:
    print("Wrong")

Question = input("What type of database is PostgreSQL?\n"
                 "a) NoSQL\nb) SQL\nc) Document\nd) Graph\n"
                 "Your answer: ")
if Question.lower() == "b":
    print("Correct")
    score += 1
else:
    print("Wrong")

print(f"Your total score is: {score}/9")
