import stanza
import sys
from termcolor import colored, cprint
import pyfiglet
from pyfiglet import Figlet

#print a clean output to the terminal  
print_red = lambda x: cprint(x, 'red')
print_red_bold = lambda x: cprint(x, 'red', attrs = ['bold'])
print_grey = lambda x: cprint(x, 'grey')
print_green = lambda x: cprint(x, 'green')
print_green_bold = lambda x: cprint(x, 'green', attrs = ['bold'])
print_blue_bold_underline = lambda x: cprint(x, 'blue', attrs = ['bold', 'underline'])
print_blue = lambda x: cprint(x, 'blue')
print_blue_bold = lambda x: cprint(x, 'blue', attrs = ['bold'])
print_magenta = lambda x: cprint(x, 'magenta')
print_magenta_bold = lambda x: cprint(x, 'magenta', attrs = ['bold'])
print_yellow_bold = lambda x: cprint(x, 'yellow', attrs = ['bold'])
print_cyan = lambda x: cprint(x, 'cyan')
print_cyan_bold = lambda x: cprint(x, 'cyan', attrs = ['bold'])


print_blue_bold_underline("What career would you like to pursue?")
print_blue("- Full Stack Engineer")
print_blue("- Front End Engineer")
print_blue("- Back End Engineer")
print_blue("- Software QA Engineer")
print_blue("- DevOps Engineer")
print_blue("- Embedded Systems Software Engineer")
print_blue("- Data Engineer")
print_blue("- Mobile App Developer")
print_blue("- Cloud Engineer")

# Command Line arguments
scriptName = sys.argv[0]
resumeName = sys.argv[1]
#positionName = sys.argv[2]
positionName = input("Enter a position: ")

def commandLineArgs(argv, position_name):  
    """
    To Run the program:

    In the terminal, 
    
    # Command Line Arguments
    # argv[0]     argv[1]               argv[2]
    # file name   Resume Name           Position Name
    # test.py     Example_Resume.pdf    "Software Engineering"

    """
    script_name = sys.argv[0]
    resume_name = sys.argv[1]
    position_name = sys.argv[2]

    print(f"Name of the script : {script_name}")
    print(f"Resume Name : {resume_name}")
    print(f"Position Name : {position_name}")

nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit=True)
languages = ['java', 'go', 'python', 'c++', 'mysql', 'c', 'javascript', 'react', 'angular', 'vue', 'django', 'flask', 'node', 'html', 
'ruby', 'php', 'perl', 'scala', 'golang', 'c#', 'css', 'swift', 'jenkins', 'groovy', 'jquery', 'ux and ui frameworks', 'c#',
'node-js', 'smashtest', 'devops', 'kubernetes', 'docker', 'apache', 'mesos', 'hashicorp', 'sql', 'powershell', 'micropython', 
'arduino', 'rust', 'verilog', 'r', 'julia', 'matlab', 'sas', 'html5', 'xamarin', 'flutter', 'react', 'native cloud', 'asp.net',
'angularjs', 'angularjs']

userLangs = []
userGPA = 0
userCourses = []
userExperiences = []
userCompanies = []

topCompanies = ["facebook", "google", "amazon", "netflix", "microsoft", "uber", "lyft", "airbnb", "robinhood", "linkedin", "stripe", "twitter", "box", "roblox", "instacart", "bytedance", "pinterest", "doordash", "spacex", "coinbase", "discord"]

topCompanyBool = False
experienceGoodBool = False
experienceBadBool = False


def getLangs(sentences, i):
    text = ""
    while(text.lower() != 'education'):
        i+=1
        for token in sentences[i].tokens:
            text = token.text
            if text.lower() in languages:
                userLangs.append(text.lower())

def getGPA(sentences, i):
    global userGPA
    text = ""
    while(text.lower() != "coursework"):
        i += 1
        for j in range(0, len(sentences[i].tokens)):
            text = sentences[i].tokens[j].text
            if(text.lower() == "gpa"):
                j += 2
                text = sentences[i].tokens[j].text
                userGPA = float(text)

def getCoursework(sentence):
    global userCourses
    text = ""
    for token in sentence.tokens:
        text += (token.text + " ")
    text = text.strip()
    userCourses = text.split(" , ")

def getWorkExperience(sentences, i):
    text = ""
    st = []
    while(1):
        for j in range(0, len(sentences[i].tokens)):
            text +=(sentences[i].tokens[j].text + " ")
        if(text.lower() == "leadership & campus involvement "):
            break
        # print(text.lower())
        if('20xx' in text.lower()):
            st = text.lower().split()
            st.remove(',')
            text = " ".join(st)
            userExperiences.append(text)
            t = text.split()
            for w in t:
                if w in topCompanies:
                    userCompanies.append(w)
        i += 1
        text = ""
            
def parseResume():
    text = "" 
    with open(resumeName) as f:
        lines = f.readlines()
    doc = nlp(lines)
    for i, sentence in enumerate(doc.sentences):
        for token in sentence.tokens:
            text += (token.text + " ")
        if(text.lower() == 'skills summary '):
            getLangs(doc.sentences, i)
        if(text.lower() == 'education '):
            getGPA(doc.sentences, i)
        if(text.lower() == 'relevant coursework '):
            i+=1
            getCoursework(doc.sentences[i])
        if(text.lower() == 'work experience '):
            i += 1
            getWorkExperience(doc.sentences, i)
        text = "" 


#missingSkills = []
def getSkillsScore():
    global missingSkills
    missingSkills = []
    numOfSkillsThere = 0
    isInList = False
    skillsScore = 0
    
    if(positionName.replace(" ", "").lower() == "fullstackengineer"):
        neededSkills = ["css", "javascript", "html", "java", "c", "c++", "ruby", "perl", "python", "scala", "react", "jenkins"]
    elif(positionName.replace(" ", "").lower() == "frontendengineer"):
        neededSkills = ["css", "javascript", "html", "react", "angular", "vue", "swift", "jquery"]
    elif(positionName.replace(" ", "").lower() == "backendengineer"):
        neededSkills = ["java", "c", "c++", "ruby", "perl", "python", "scala", "go", "javascript", "php", "golang", "c#"]
    elif(positionName.replace(" ", "").lower() == "softwareqaengineer"):
        neededSkills = ["c", "java", "groovy", "python", "perl", "ruby", "nodejs", "php",  "smashtest"]
    elif(positionName.replace(" ", "").lower() == "devopsengineer"):
        neededSkills = ["kubernetes", "docker", "apachemesos", "jenkins", "hashicorp", "stack"]
    elif(positionName.replace(" ", "").lower() == "embeddedsystemssoftwareengineer"):
        neededSkills = ["c", "c++", "python", "micropython", "java", "arduino", "rust", "verilog", "c#"]
    elif(positionName.replace(" ", "").lower() == "dataengineer"):
        neededSkills = ["sql", "r", "python", "javascript", "scala", "julia", "java", "c", "c++", "matlab", "sas"]
    elif(positionName.replace(" ", "").lower() == "mobileappdeveloper"):
        neededSkills = ["c#", "html5", "java", "python", "c", "c++", "java", "javascript", "xamarin", "flutter", "react", "reactnative"]
    elif(positionName.replace(" ", "").lower() == "cloudengineer"):
        neededSkills = ["java", "c++", "php", "asp.net", "python", "golang", "ruby", "angularjs"]
    else:
        raise("Enter a valid position name!")
    
    #print("needed skillsss", neededSkills)
    #print("userlangs", userLangs)
    #print("MISSING ", missingSkills)
    #compare neededSkills with users skills (userLangs)
    # for skill in neededSkills:
    #     for lang in userLangs:
    #         if skill == lang:
    #             numOfSkillsThere +=1
    #             isInList = True
    #     if(isInList == False):
    #         missingSkills.append(skill)
    #     isInList = False
    for skill in neededSkills:
        if skill not in userLangs:
            missingSkills.append(skill)
        else:
            numOfSkillsThere += 1
    
    #print("missing skills", missingSkills)

    #Calculate score
    if(numOfSkillsThere >= 5):
        skillsScore = 15
    elif(numOfSkillsThere == 4):
        skillsScore = 12
    elif(numOfSkillsThere == 3):
        skillsScore = 9
    elif(numOfSkillsThere == 2):
        skillsScore = 6
    elif(numOfSkillsThere == 1):
        skillsScore = 3
    else:
        skillsScore = 0

    return skillsScore


def getGPAScore():
    GPAScore = 0
    if(userGPA >= 3.5):
        GPAScore = 10
    elif(userGPA >= 3.3):
        GPAScore = 8
    elif(userGPA >= 3):
        GPAScore = 6
    elif(userGPA >= 2.5):
        GPAScore = 4
    elif(userGPA >= 2):
        GPAScore = 2
    else:
        GPAScore = 0

    return GPAScore


def getExperienceScore():
    experienceScore = 0
    numOfValidInternships = 0
    #fake_user_companies = ["google", "asfour crystal"]

    #check if he worked for a top company (score = 10)
    '''for userCompany in fake_user_companies:
        # if userCompany in topCompanies, (replace with line below)
        for topCompany in topCompanies:
            if userCompany == topCompany:
                experienceScore = 20
                topCompanyBool = 1
                return experienceScore, topCompanyBool'''
    if len(userCompanies) > 0:
        experienceScore = 20
        topCompanyBool = 1
        return experienceScore, topCompanyBool

    # count the number of valid internships
    for experience in userExperiences:
        fullExperince = experience.split()
        for word in fullExperince:
            if word == "software" or word == "engineer" or word == "engineering":
                numOfValidInternships += 1
    
    # calculate experince score
    if numOfValidInternships >= 3:
        experienceScore = 18
        experienceGoodBool = True
    elif numOfValidInternships == 2:
        experienceScore = 16
    elif numOfValidInternships == 1:
        experienceScore = 12
    else:
        experienceScore = 0
        experienceBadBool = True

    return experienceScore, topCompanyBool
  

def getOverallScore():
    finalSkillsScore = getSkillsScore() #skills are worth 15 points
    finalGPAScore = getGPAScore()   #gpa is worth only 10 points
    finalExperienceScore, bool = getExperienceScore() # experience is worth 20 points
    overallScore = ((finalSkillsScore + finalGPAScore + finalExperienceScore) / 45) * 100
    return overallScore

def getExperienceRecommendations():
    expScore, boolean = getExperienceScore()
    if expScore == 20:
        print("You worked at a top company! Your work experience is great!")
    elif expScore == 18:
        print("You have a great amount of solid internships! The only recommendation we have is to try to get an internship at a top company.")
    elif expScore == 16:
        print("You have a good amount of solid internships! We recommend getting one more solid internship, especially at a top company.")
    elif expScore == 12:
        print("You only have one solid internship, we recommend getting one or two more internships, especially at a top compnay!")
    elif expScore == 0:
        print("You have no solid internships! We recommend improving your experience by getting at least two/three solid internships, especially if you can get one at a top company.")

def getSkillsRecommendations():
    print("The skills you should add to your resume are", end = ' ')
    for i in range(len(missingSkills)):
        if missingSkills[i] != missingSkills[len(missingSkills) - 1]:
            print(missingSkills[i], end = ', ')
        else:
            print("and", missingSkills[i])
            
def getGPARecommendations():
    if getGPAScore() == 10:
        print("Your GPA is perfect!")
    elif getGPAScore() == 8:
        print("Your GPA is pretty good, we recommend improving it to 3.5 or higher")
    elif getGPAScore() == 6:
        print("Your GPA needs some improvement, we recommend improving it to 3.5 or higher")
    elif getGPAScore() == 4:
        print("Your GPA is very weak, we recommend improving it to 3.5 or higher")
    else:
        print("Your GPA is terrible, you should increase it in any way, we recommend improving it to 3.5 or higher") 

def giveOverallFeedback():
    if getOverallScore() == 100:
        print_magenta("You have a perfect resume for the position you are applying for! You meet all of the requirements for this job, there's no need to improve anything to your resume. \nWe very strongly recommend that you continue pursuing this career.")
    elif getOverallScore() >= 90:
        print_magenta("You have an amazing resume for the position you are applying for! You meet almost all of the requirements for this job. \nWith very minimal additions to your resume, you'll have a perfect resume and you'll be set for the job. \nWe strongly recommend that you continue pursuing this career.")
    elif getOverallScore() >= 80:
        print_magenta("You have a great resume for the position you are applying for! You meet most of the requirements for this job. \nWith a few additions to your resume, you'll have a perfect resume and you'll be set for the job. \nWe recommend that you continue pursuing this career.")
    elif getOverallScore() >= 70:
        print_magenta("You have a decent resume for the position you are applying for. You meet a decent amount of the requirements for this job. \nWith some additions to your resume, you'll have a perfect resume and you'll be set for the job. \nWe suggest that you continue pursuing this career.")
    elif getOverallScore() >= 60:
        print_magenta("You have a satisfactory level resume for the position you are applying for. You meet a few amount of the requirements for this job. \nWith a lot of additions to your resume, you'll have a perfect resume and you'll be set for the job. \nYou could still continue pursuing this career.")
    elif getOverallScore() >= 50:
        print_magenta("You have a poor resume for the position you are applying for. You meet very few of the requirements for this job. \nYou need to make many additions to your resume in order to have a strong resume for this postion. \nYou could still continue pursuing this career, but we recommend looking for another positon in the same field.")
    elif getOverallScore() >= 30:
        print_magenta("You have a very poor resume for the position you are applying for. You meet a very low amount of the requirements for this job. \nYou need to make so many additions to your resume in order to have an acceptable resume for this postion. \nWe recommend looking for another positon, maybe in the same field.")
    else:
        print_magenta("You have an extremely poor resume for the position you are applying for. You meet almost none of requirements for this job. \nYou would have to completely update your resume in order to have a acceptable resume for this postion. \nWe recommend that you persue a different career.")
    
#def giveMoreAdvice():
    #if worked at a top company: emphasize that
    #if they have over three expreinces, emphazise that
    #if they dont have good exprience, talk about your projects
    #if they have a 4.0 emphasize that
    #if you have a low gpa, take off the resume
    #for each roll, specify what important skill to emphasize


def additionalAdvice():
    #print(topCompanyBool)
    expScore, topCompBool = getExperienceScore()
    if topCompBool == True:
        print_cyan("While talking about your resume, make sure you emphasize that you worked at a top company, as that is one of the strongest elements of your resume. \nHaving work experience at one of the top tech comanies in the world puts you at a huge advatange for the position you are applying for.\n")
    if experienceGoodBool:
        print_cyan("While talking about your resume, make sure you emphasize the number of valid internsips/work experience you have, as that is one of the strongest elements of your resume. \nHaving 3 or more solid internships shows that you have more than enough work experience, which puts you at a huge advatange for the position you are applying for.\n")
    if experienceBadBool:
        print_cyan("Because you have no solid internships or work experience, we recommend that you talk about your perosonal projects (or any valid projects) in order to make up for the lack of work experience you have. \nMake sure you get a valid internship as soon as possible in order to improve your chances for this position, but for now dicuss your projects as well.\n")
    if userGPA == 4.0:
       print_cyan("While talking about your resume, make sure you emphasize that you have a 4.0 GPA, as that is one of the strongest elements of your resume. \nHaving a perfect GPA demonstarates that you are hard working, intelligent, have good work ethic, ect., which are all attributes that employers are looking for.\n")
    if userGPA <= 2.5:
        print_cyan("We recommend that you completely take off your GPA off of your resume because it is extremely low. \nMost employers will not even ask about your GPA, so there is no reason for you to keep something that will deteriorate your resume.")
    

def main():
    #printPositions()
    #commandLineArgs(sys.argv, positionName)
    parseResume()
    #displayOutput()
    print_yellow_bold("\n**************************** RESUME GRADE REPORT ****************************")
    print_red_bold("\nYour OVERALL SCORE for your resume is: ")
    print(getOverallScore(), "%\n")
    giveOverallFeedback()
    print("\n")
    print_blue_bold("Here is a breakdown of your SCORES for each section of your resume:")
    print_blue("\nExperience: ")
    score, boolean = getExperienceScore()
    print(score , "/ 20")
    print_blue("\nSkills: ")
    print(getSkillsScore(), "/ 15")
    print_blue("\nGPA: ") 
    print(getGPAScore(), "/ 10")
    print("\n")
    print_green_bold("Here is a breakdown of your RECOMMENDATIONS for each section of your resume:")
    print_green("\nExperience: ")
    getExperienceRecommendations()
    print_green("\nSkills: ")
    getSkillsRecommendations()
    print_green("\nGPA: ")
    getGPARecommendations()
    print("\n")
    print_cyan_bold("Extra Recommendations:\n")
    additionalAdvice()


if __name__ == "__main__":
    main()
    