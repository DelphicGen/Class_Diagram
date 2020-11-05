class iUser:
    def register(password, name, email):
        # check if credentials is
        return True

class Users:
    def __init__(self, userId, password, name, email, userRole):
        self.userId = userId
        self.password = password
        self.name = name
        self.email = email
        self.userRole = userRole

    def login(email, password):
        # check if credentials is 
        return True

    def verifyAccount():
        return True

    def forgetPassword():
        return True

    def changePassword(token):
        return True

    def logout():
        return True

class Admin(User):
    def __init__(self, available):
        self.available = True

    def verifyUser():
        return True

    def solveThreadProblem():
        return True
    
    def deleteContent():
        return True
    
    def getUserInformation(email):
        return True

class Customer(User):
    def __init__(self, weight, height, birthDate):
        self.weight = weight
        self.height = height
        self.birthDate = birthDate

    def bookNutrisionist():
        return True

    def sendMessage():
        message = chatMessage('test','test','test','test')
        message.sendMessage(message)    

class ContentWriter(User):
    def createContent():
        return True
    
    def editContent():
        return True

    def deleteContent():
        return True  

class Nutrisionist(User):
    def __init__(self, timeShift, nameOfHospital):
        self.timeShift = timeShift
        self.available = True
        self.nameOfHospital = nameOfHospital
        self.rating = 5

    def proofReading():
        return True

class Content:
    def __init__(self, datePublish, writer, title, content):
        self.datePublish = datePublish
        self.writer = writer
        self.title = title
        self.content = content
        self.approved = False
    
    def getContent():
        return True;

class Consultation:
    def __init__(self, consultationID, userID, nutrisionistID):
        self.consultationID = consultationID
        self.userID = userID
        self.nutrisionistID = nutrisionistID
    
    def sendMessage(message):
        return True
    
    def replyMessage(message):
        return True
    
    def getUserInformation(email):
        return True
    
    def getUserCalorie(email):
        return True
    
    def getNutrisionistInformation(email):
        return True
    
    def getMedicalReference():
        return True

class RecommendationFood:

    dishes: []
    calorie: []

    def getRecomendation(calorie):
        return 'Makan yang BANYAK biar happy'

class CalorieIntake:
    def __init__(self, activity, foodName, foodCalorie, date):
        self.activity = activity
        self.foodName = foodName
        self.foodCalorie = foodCalorie
        self.date = date
    
    def calculateIdealCalorie():
        return True
    
    def getCalorie(food):
        return 0
    
    def calculateConsumedCalorie():
        return 0
    
    def compareIntake():
        return True
    
    def sendNotification():
        return 'Makan bang'
    
    def saveCalorir():
        return True
    
    def plotGraph():
        return True
