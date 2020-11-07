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
    def __init__(self, userId, name, email, password, userRole):
        self.userId = userId
        self.password = password
        self.name = name
        self.email = email
        self.userRole = userRole
        self.isLoggedIn = False

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.isLoggedIn = True
            return True
        else:
            return False

    def getUserRole(self):
        return self.userRole

    def getEmail(self):
        return self.email

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
        self.isLoggedIn = False
        print('\n\nLogout')
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
    def __init__(self, userId, name, email, password, userRole, weight, height, birthDate, gender):
        Users.__init__(self, userId, name, email, password, userRole)
        self.weight = weight
        self.height = height
        self.birthDate = birthDate
        self.gender=gender
        self.calorieRecord = []

    def consumeFood(self, activity, foodName, foodCalorie):
        calorie = CalorieIntake(activity, foodName, foodCalorie, datetime.datetime.now())
        self.calorieRecord.append(calorie)
        while True:
            print('\n\n0. Exit')
            print('1. Hitung calorie ideal')
            print('2. Bandingkan kalori  makanan dan kalori ideal')
            choose = int(input('Pilih angka: '))

            if choose == 0:
                break
            elif choose == 1:
                age = self.calculateAge()
                ideal = calorie.calculateIdealCalorie(activity, self.weight, self.height, age, self.gender)
                print('\n\nCalorie ideal: ', ideal)
            elif choose == 2:
                calorie.compareIntake(foodCalorie)
                
        return True
    
    def getWeight(self):
        return self.weight
    
    def getHeight(self):
        return self.height
    
    def getGender(self):
        return self.gender
    
    def calculateAge(self):
        today = datetime.date.today()
        day, month, year = map(int, self.birthDate.split('-'))
        birthDate= datetime.date(year, month, day)
        return (today-birthDate).days//365
    
    def bookNutrisionist(self):
        return True

    def sendMessage(self):
        message = chatMessage('test','test','test','test')
        message.sendMessage(message) 
        return True   

class ContentWriter(Users):

    def __init__(self, userId, name, email, password, userRole):
        Users.__init__(self, userId, name, email, password, userRole)

    def createContent(self, title, content):
        content = Content(datetime.datetime.now(), self.name, title, content)
        return content
    
    def editContent(self, title, content):
        try:
            content = Content(datetime.datetime.now(), self.name, title, content)
            return content
        except:
            print('Gagal edit content')
            return None

    def deleteContent(self, contentId):
        return True

class Nutrisionist(Users):
    def __init__(self, userId, name, email, password, userRole, timeShift, nameOfHospital):
        Users.__init__(self, userId, name, email, password, userRole)
        self.timeShift = timeShift
        self.available = True
        self.nameOfHospital = nameOfHospital
        self.rating = 5

    def proofReading(self, content):
        content.approveContent(True)
        return True

class Message():
    def __init__(self, to, message, dari):
        self.message = message
        self.to = to
        self.read = False
        self.dari = dari

    def getTo(self):
        return self.to

    def getRead(self):
        return self.read

    def readMessage(self):
        self.read = True
        return self.message

    def getDari(self):
        return self.dari

class Content:
    def __init__(self, datePublish, writer, title, content):
        self.datePublish = datePublish
        self.writer = writer
        self.title = title
        self.content = content
        self.approved = False

    def approveContent(self, approveStatus):
        self.approved = approveStatus
        print('Berhasil merubah status content')
        return True
    
    def getContent(self, userRole):
        if userRole == 'nutrisionist' or userRole == 'writer' or self.approved:
            data = {
                'publised' : self.datePublish,
                'writer' : self.writer,
                'title' : self.title,
                'content' : self.content
            }
            return data
        else:
            print('Content belum di approved')
            return None

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

    def getRecomendation(self, ideal_cal):
        nilai=random.choice(self.dishes)
        while(nilai > ideal_cal):
            nilai=random.choice(self.dishes)
        return (nilai, self.list_recom[nilai])

class CalorieIntake:
    def __init__(self, activity, foodName, foodCalorie, date):
        self.activity = activity
        self.foodName = foodName
        self.foodCalorie = foodCalorie
        self.date = date
        temp = date
        self.ideal = None
        self.idealInput = False

    def calculateIdealCalorie(self, activity, weight, height, age, gender):
        if (activity=='low'):
            activity_value = 1.2
        elif (activity=='moderate'):
            activity_value = 1.3
        else:
            activity_value = 1.4

        if (gender=='L'):
            ideal_cal=activity_value*(66.5+13.8*float(weight)+5*float(height))-(6.8*float(age))
        elif gender == 'P':
            ideal_cal=activity_value*(655.1+9.6*float(weight)+1.9*float(height))-(4.7*float(age))

        self.idealInput = ideal_cal
        return ideal_cal
    
    def getCalorie(self, food):
        calorie = fetch('https://foodie/calorie-list/', food)
        return calorie
    
    def calculateConsumedCalorie(self, food, calorie):
        finished=False
        val = 0
        while finished:
            val=val+calorie[food]
            temp=input("Sudah Selesai? [Ya/Tidak]") #Ini pengennya dia pencet Finished kalo uda wkkw
            finished = True if temp == 'Ya' else False
        return 0
    
    def saveCalorie(self, consumed_cal, ideal_cal, calorieDatabase):
        sisa=ideal_cal-consumed_cal
        print("Sisa Kalori Kamu Hari Ini : ",sisa)
        if temp.date()!=datetime.datetime.today().date():
            calorieDatabase[str(self.date)]=consumed_cal
        return True
    
    def compareIntake(self, consumed_cal):
        print('\n\nideal: ', self.idealInput, ' consumed: ', consumed_cal)
        if consumed_cal<self.idealInput:
            print("Batas Kalori Masih Aman")
        else:
            print("Warning! Batas Kalori sudah Melebihi Batas!")
    
    import matplotlib.pyplot as plt
    def plotGraph(self, calorieDatabase):
        plt.plot(calorieDatabase.keys(),calorieDatabase.values())
        plt.title("Grafik Kalori Harian dari",min(calorieDatabase.keys()),"hingga",max(calorieDatabase.keys()))
        plt.xlabel("Tanggal")
        plt.ylabel("Jumlah Kalori")
        return True

users = []
messages = []
contents = []

def tambahUser(id):
    while True:
        print('\n\n0. untuk keluar')
        print('1. Tambah customers')
        print('2. Tambah nutrisionist')
        print('3. Tambah content writers')
        choose = int(input('Pilih angka: '))

        if choose == 0:
            return None

        elif choose == 1:
            name = input('\n\nYour name: ')
            email = input('Your email: ')
            password = input('Your password: ')
            weight = int(input('Your weight: '))
            height = int(input('Your Height: '))
            birthDate = input('birthDate (day-month-year): ')
            gender = input('Gender P/L: ')

            user = Customer(id, name, email, password, 'customer', weight, height, birthDate, gender)

            return user

        elif choose == 2:
            name = input('\n\nYour name: ')
            email = input('Your email: ')
            password = input('Your password: ')

            timeShift = input('Time shift: ')
            hospital = input('Hospital: ')

            user = Nutrisionist(id, name, email, password, 'nutrisionist', timeShift, hospital)

            return user
        
        elif choose == 3:
            name = input('\n\nYour name: ')
            email = input('Your email: ')
            password = input('Your password: ')

            user = ContentWriter(id, name, email, password, 'writer')

            return user

        else:
            print('\n\nWrong choice\n\n')
            continue
            
def login():
    email = input('Email: ')
    password = input('Password: ')
    for user in users:
        status = user.login(email, password)
        if status:
            return user
    
    return None

def readMessage(email):
    for message in messages:
        to = message.getTo()
        read = message.getRead()
        if email == to and not read:
            print('\n\nmessage dari: ', message.getDari())
            print('isi pesan: ', message.readMessage())

def sendMessage(email):
    to = input('ke: ')
    pesan = input('message: ')
    message = Message(to, pesan, email)
    return message

def userManagement(user):
    
    userRole = user.getUserRole()
    email = user.getEmail()

    readMessage(email)

    if userRole == 'customer':
        while True:
            print('\n\n1. Send message')
            print('2. calorie record')
            print('3. read content')
            print('4. logout')
            choose = int(input('Choose: '))

            if choose == 1:
                message = sendMessage(email)
                messages.append(message)
            elif choose == 2:
                activity = input('\n\nActivity [low, moderete, high]: ')
                foodName = input('Food name: ')
                foodCalorie = int(input('Food calorie: '))

                user.consumeFood(activity, foodName, foodCalorie)
                print('success')
            elif choose == 3:
                id = int(input('\n\nPilih id content: '))
                try:
                    content = contents[id]
                    if content is not None:
                        print('\n\n', content.getContent(userRole))
                except:
                    print('\n\nid content salah')
            elif choose == 4:
                user.logout()
                return
            else:
                continue
    elif userRole == 'nutrisionist':
        while True:
            print('\n\n1. Send message')
            print('2. read content')
            print('3. proofReading')
            print('4. logout')
            choose = int(input('Choose: '))

            if choose == 1:
                message = sendMessage(email)
                messages.append(message)
            elif choose == 2:
                id = int(input('\n\nPilih id content: '))
                try:
                    content = contents[id]
                    if content is not None:
                        print('\n\n', content.getContent(userRole))
                except:
                    print('\n\nid content salah')
            elif choose == 3:
                id = int(input('\n\nPilih id content: '))
                try:
                    content = contents[id]
                    if content is not None:
                        print('\n\n', content.getContent(userRole))
                        user.proofReading(content)
                except:
                    print('\n\nid content salah')
            elif choose == 4:
                user.logout()
                return
            else:
                continue
    elif userRole == 'writer':
        while True:
            print('\n\n1. Send message')
            print('2. tambah content')
            print('3. Edit content')
            print('4. Delete content')
            print('5. Read content')
            print('6. logout')
            choose = int(input('Choose: '))

            if choose == 1:
                message = sendMessage(email)
                messages.append(message)
            elif choose == 2:
                title = input('\n\nTitle: ')
                isi = input('Content: ')
                content = user.createContent(title, isi)
                contents.append(content)
                print('\n\nYour id content: ', len(contents)-1)
            elif choose == 3:
                # bug bisa edit content orang lain
                id = int(input('\n\nId content: '))
                title = input('Title: ')
                isi = input('Content: ')
                content = user.editContent(title, isi)
                if content is not None:
                    contents[id] = content
                    print('\n\nEdit content success')

            elif choose == 4:
                # bug bisa delete content orang lain
                id = int(input('\n\nId content: '))
                try:
                    contents[id] = None
                    print('Delete content successfully')
                except:
                    print('Id salah')
            elif choose == 5:
                id = int(input('\n\nPilih id content: '))
                try:
                    content = contents[id]
                    if content is not None:
                        print('\n\n', content.getContent(userRole))
                except:
                    print('\n\nid content salah')
            elif choose == 6:
                user.logout()
                return
            else:
                continue

def main():
    print('Simple execute program\n\n')

    countUser = 0
    while True:
        print('\n\n1. Tambah user')
        print('2. Login')
        # print('3. Lupa password')
        choose = int(input('Pilih angka: '))

        if choose == 1:
            user = tambahUser(countUser)
            if user is not None:
                users.append(user)
                userManagement(user)
                countUser += 1
            else:
                continue

        elif choose == 2:
            user = login()
            if user is not None:
                print('\n\nLogin success')
                userManagement(user)
            else:
                print('\n\nLogin failed')

if __name__ == '__main__':
    main()