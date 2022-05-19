import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize', tokenize_no_ssplit=True)
languages = [
    'java',
    'go',
    'python',
    'c++',
    'mysql',
    'c',
    'javascript',
    'react',
    'angular',
    'vue',
    'django',
    'flask',
    'node'
]
userLangs = []
userGPA = 0
userCourses = []
userExperiences = []

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
        i += 1
        text = ""
            
def parseResume():
    text = "" 
    with open('sample-resume.txt') as f:
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

def main():
    parseResume()
    print("Languages: ", userLangs)
    print("GPA: ", userGPA)
    print("Courses: ", userCourses)
    print("Work experience: ", userExperiences)
    

if __name__ == "__main__":
    main()