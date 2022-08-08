spe=["Software Modelling &DevOps","Internet Of Things","Cloud & EdgeComputing","Graphics,Gaming & UX Design","Cyber Security & BlockchainTechnology","AI & Intelligence Process Automation","Data Science aand BigDataAnalytics","Computer Communications" ]
print("Hello student, I am student advisor")
print("May I know yourname?")
name=input()
print("Thank you", name)
print("I am here to help you explore through the specialisations offered inCSE Department of K L University.")
print("Here are the list of specialisations")
for i in range(0,8):
    print((i),".",spe[i])
print("Choose any specialisation")
num=input()
dict={
        "0":" 'Global certification':'Professional scrum Master' 'core course in 1st sem':'Software Engineering' ",
        "1":"'Global certification':'None' 'core course in 1st sem':'None'",
        "2":"'Global certification':'Linux Essential(101-160)' 'core course in 1st sem':'Operating Systems'",
        "3":"'Global certification':'UnityDeveloper Advance Certification' 'core course in 1st sem':'EnterpriseProgramming'",
        "4":"'Global certification':'ETHERIUM Developer AdvanceCertification' 'core course in 1st sem':'Computer Networks'",
        "5":"'Global certification':'PCAP|CertifiedAssociatePythonProgramming' 'core course in 1st sem':'AI &Mathematical Programming'",
        "6":"'Global certification':'C100DEV:MongoDB certified DeveloperAssociate' 'core course in 1st sem':'DataBase Management System'",
        "7":"'Global certification':'None' 'core course in 1st sem':'None'"
    }
number=""
for i in num:
    number+=dict.get(i,"")+" "
print(number)
