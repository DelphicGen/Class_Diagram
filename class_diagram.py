from collections import defaultdict
import string
import random
class iUser:
    def register(self, password, name, email, userRole):
        # check if credentials is
        registeredEmails = ["abc@gmail.com", "def@gmail.com", "ghi@gmail.com"]
        if email not in registeredEmails:
            return True
        else:
            return False

class Users:
    def __init__(self, userId, password, name, email, userRole):
        self.userId = userId
        self.password = password
        self.name = name
        self.email = email
        self.userRole = userRole
        self.isLoggedIn = False

    def login(self):
        UserDatabase = {"abc@gmail.com": "abcdefg", "def@gmail.com": "password1", "ghi@gmail.com": "password2"} # Get user list from database
        if self.isLoggedIn == True:
            print("Anda sudah login")
        else:
            if self.email in UserDatabase:
                if self.password == UserDatabase[self.email]:
                    print("Login success")
                    self.isLoggedIn = True
                    return True
                else:
                    print("Wrong password")
                    return False
            else:
                print("Email not found")

    def verifyAccount(self):
        return self.isLoggedIn

    def forgetPassword(self):
        if self.isLoggedIn == True:
            newPassword = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
            self.password = str(newPassword)
            return self.password #Send new password to user
        else:
            return False

    def changePassword(self, newPassword):
        UserDatabase = {"abc@gmail.com": "abcdefg", "def@gmail.com": "password1", "ghi@gmail.com": "password2"}
        if self.isLoggedIn == True:
            try:
                UserDatabase[self.email] = newPassword
                self.password = newPassword
                return True
            except:
                return False
        else:
            return False

    def logout(self):
        if self.isLoggedIn == True:
            try:
                self.userId = None
                self.password = None
                self.name = None
                self.email = None
                self.userRole = None
                self.isLoggedIn = False
                return True
            except:
                return False
        else:
            return False

class Admin(Users):
    def __init__(self, available):
        self.available = True

    def verifyUser(self):
        return True

    def solveThreadProblem(self):
        return True
    
    def deleteContent(self):
        return True
    
    def getUserInformation(self, email):
        return True
    
    def replyMessage(self, message):
        return True

import datetime
class Customer(Users):
    def __init__(self, weight, height, birthDate,gender):
        self.weight = weight
        self.height = height
        self.birthDate = birthDate
        self.gender=gender
    
    def getWeight(self):
        return self.weight
    
    def getHeight(self):
        return self.height
    
    def getGender(self):
        return self.gender
    
    def calculateAge(self):
        today = datetime.date.today()
        birthDate= self.birthDate.date()
        return (today-birthDate)//365
    
    def bookNutrisionist(self):
        return True

    def sendMessage(self):
        # message = chatMessage('test','test','test','test')
        # message.sendMessage(message) 
        return True   

class ContentWriter(Users):

    def __init__(self):
        self.content = []

    def createContent(self, title, content):
        content = Content(datetime.datetime.now(), self.name, title, content)
        self.content.append(content)
        return True
    
    def editContent(self, contentId, title, content):
        try:
            content = Content(datetime.datetime.now(), self.name, title, content)
            self.content[contentId] = content
            return True
        except:
            print('Gagal edit content')
            return False

    def deleteContent(self, contentId):
        try:
            del(self.content[contentId])
            return True
        except:
            return False

class Nutrisionist(Users):
    def __init__(self, timeShift, nameOfHospital):
        self.timeShift = timeShift
        self.available = True
        self.nameOfHospital = nameOfHospital
        self.rating = 5

    def proofReading(self):
        return True

class Content:
    def __init__(self, datePublish, writer, title, content):
        self.datePublish = datePublish
        self.writer = writer
        self.title = title
        self.content = content
        self.approved = False

    def approveContent(self, userRole, approveStatus):
        if userRole == 'admin' or userRole == 'nutrisionist':
            self.approved = approveStatus
            print('Berhasil merubah status content')
            return True
        else:
            print('Akses denied')
            return False
    
    def getContent(self):
        return {
            'publised' : self.datePublish,
            'writer' : self.writer,
            'title' : self.title,
            'content' : self.content
        }

class Consultation:
    def __init__(self, consultationID, userID, nutrisionistID, consultationTime):
        self.consultationID = consultationID
        self.userID = userID
        self.nutrisionistID = nutrisionistID
        self.consultationTime=consultationTime
    
    def sendMessage(self, message):
        return True
    
    def replyMessage(self, message):
        return True
    
    def getUserInformation(self, email):
        return True
    
    def getUserCalorie(self, email):
        return True
    
    def getNutrisionistInformation(self, email):
        return True
    
    def getMedicalReference(self):
        return True

import random
class RecommendationFood:

    dishes= ['Sup Ayam']
    calorie= [1000]
    list_recom=defaultdict(list)
    for i in range(len(dishes)):
        list_recom[dishes[i]]=calorie[i]

    def getRecomendation(self, calorie):
        nilai=random.choice(self.dishes)
        return (nilai, self.list_recom[nilai])

class CalorieIntake:
    def __init__(self, activity, foodName, foodCalorie, date):
        self.activity = activity
        self.foodName = foodName
        self.foodCalorie = foodCalorie
        self.date = date
        temp=date

    def calculateIdealCalorie(self, activity, weight, height, age, gender):
        if (activity=='low'):
            activity_value=1.2
        elif (activity=='moderate'):
            activity_value=1.3
        else:
            activity_value=1.4

        if (gender=='Laki-laki'):
            ideal_cal=activity_value*(66.5+13.8*weight+5*height)/(6.8*age)
        else:
            ideal_cal=activity_value*(655.1+9.6*weight+1.9*height)/(4.7*age)
        return ideal_cal
    
    def getCalorie(self, food):
        calorie = []
        return calorie[food]
    
    def calculateConsumedCalorie(self, food, calorie):
        finished=False
        val = 0
        while finished == False:
            val=val+calorie[food]
            temp=input("Sudah Selesai? [Ya/Tidak]") #Ini pengennya dia pencet Finished kalo uda wkkw
            finished = False if temp=='Tidak' else True
        return 0
    
    def saveCalorie(self, consumed_cal, ideal_cal, calorieDatabase):
        sisa=ideal_cal-consumed_cal
        print("Sisa Kalori Kamu Hari Ini : ",sisa)
        if temp.date()!=datetime.datetime.today().date():
            calorieDatabase[str(self.date)]=consumed_cal
        return True
    
    def compareIntake(self, consumed_cal, ideal_cal):
        save=False
        if consumed_cal<ideal_cal:
            print("Batas Kalori Masih Aman")
            if save==True: #ini mau kek dia click save gitu
                saveCalorie(consumed_cal, ideal_cal)
        else:
            print("Warning! Batas Kalori sudah Melebihi Batas!")
    
    import matplotlib.pyplot as plt
    def plotGraph(self, calorieDatabase):
        plt.plot(calorieDatabase.keys(),calorieDatabase.values())
        plt.title("Grafik Kalori Harian dari",min(calorieDatabase.keys()),"hingga",max(calorieDatabase.keys()))
        plt.xlabel("Tanggal")
        plt.ylabel("Jumlah Kalori")
        return True

calorieDatabase={"2020-11-01":1500,"2020-11-02":1100,"2020-11-03":1450}
