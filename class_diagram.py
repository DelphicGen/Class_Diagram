from collections import defaultdict
class iUser:
    def register(self, password, name, email):
        # check if credentials is
        return True

class Users:
    def __init__(self, userId, password, name, email, userRole):
        self.userId = userId
        self.password = password
        self.name = name
        self.email = email
        self.userRole = userRole

    def login(self, email, password):
        # check if credentials is 
        return True

    def verifyAccount(self):
        return True

    def forgetPassword(self):
        return True

    def changePassword(self, token):
        return True

    def logout(self):
        return True

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
    def createContent(self):
        return True
    
    def editContent(self):
        return True

    def deleteContent(self):
        return True  

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
    
    def getContent(self):
        return True

class Consultation:
    def __init__(self, consultationID, userID, nutrisionistID,consultationTime):
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
    
    def calculateIdealCalorie(self):
        return True
    
    def getCalorie(self, food):
        return 0
    
    def calculateConsumedCalorie(self):
        return 0
    
    def compareIntake(self):
        return True
    
    def sendNotification(self):
        return 'Makan bang'
    
    def saveCalorie(self):
        return True
    
    def plotGraph(self):
        return True
