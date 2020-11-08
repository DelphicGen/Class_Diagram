from collections import defaultdict
import string
import random
import matplotlib.pyplot as plt

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

    def forgetPassword(self, email):
        if self.email == email:
            newPassword = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 8))
            self.password = newPassword
            return str(newPassword)
        else:
            return False

    def changePassword(self, newPassword):
        self.password = newPassword

    def logout(self):
        self.isLoggedIn = False
        print('\n\nLogout')
        return True

class Admin(Users):
    def __init__(self, email, password, available):
        self.available = True
        self.email = email
        self.password = password

    def verifyUser(self):
        if (self.email != None) and (self.password != None): 
            return True
        else:
            return False

    def solveThreadProblem(self):
        print('Thread solved')
        return True
    
    def deleteContent(self, contents, index):
        try:
            del contents[index]
            print('Content deleted')
            return True
        except:
            print('Failed to delete content')
            return False
    
    def getUserInformation(self, users, email):
        # Search for user through database and return the information
        for user in users:
            if user.getEmail() == email:
                return user
        return None
    
    def sendMessage(self, message):
        # if self.available is False:
        #     print("Halo Customer yang kami sayangi, terima kasih telah mengirim pesan. Admin akan segera membalas pesan kamu, mohon bersabar:)")
        # else:
        #     print("Ceritanya ini admin balas pesan")
        # return None

        # currentRoom = getRoom() # get room chat
        # currentUser = getUser() # get user that is logged in
        # message = Message(currentRoom, message, currentUser)
        # message.sendMessage()
        return True

import datetime
class Customer(Users):
    def __init__(self, userId, name, email, password, userRole, weight, height, birthDate, gender):
        Users.__init__(self, userId, name, email, password, userRole)
        self.weight = weight
        self.height = height
        self.birthDate = birthDate
        self.gender=gender

    def consumeFood(self, activity, foodName, foodCalorie, calorieDatabase):
        calorie = CalorieIntake(activity, foodName, foodCalorie, datetime.datetime.now())
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
        # Search for nutrisionist through list of nutrisionists
        #Ini belum diisi, tapi gak usah book sih soalnya dia live-chat gitu
        return True

    def sendMessage(self):
        #Ini belum diisi habis itu ini bisa dicombine sama yg dibawah
        # currentRoom = getRoom() # get room chat
        # currentUser = getUser() # get user that is logged in
        # message = Message(currentRoom, message, currentUser)
        # message.sendMessage()
        return True   

class ContentWriter(Users):

    def __init__(self, userId, name, email, password, userRole):
        Users.__init__(self, userId, name, email, password, userRole)

    def createContent(self, title, content):
        content = Content(datetime.datetime.now(), self.email, title, content)
        return content
    
    def editContent(self, title, content):
        try:
            content = Content(datetime.datetime.now(), self.email, title, content)
            return content
        except:
            print('Gagal edit content')
            return None

    def deleteContent(self, contents, index):
        if self.email == contents[index].getContent("writer")["writer"]:
            try:
                del contents[index]
                print('Content deleted')
                return True
            except:
                print('Failed to delete content')
                return False
        else:
            print("You are not allowed to delete this content")
            return None

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
    
    def sendMessage(self, message):
        #Ini belum diisi habis itu ini bisa dicombine sama yg dibawah
        # currentRoom = getRoom() # get room chat
        # currentUser = getUser() # get user that is logged in
        # message = Message(currentRoom, message, currentUser)
        # message.sendMessage()
        return True   

class Message():
    def __init__(self, to, message, dari):
        self.message = message
        self.to = to
        self.read = False
        self.dari = dari

    def sendMessage(self, message):
        # save to chat history
        # currentRoom = getRoom() # get room chat
        # currentUser = getUser() # get user that is logged in
        # message = Message(currentRoom, message, currentUser)
        # message.sendMessage()
        return True

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
        # Menambah string ke database chat pada room chat tertentu
        #Ini belum diisi
        return True
    
    def getUserInformation(self, email,user):
        for user in users:
            if user.getEmail() == email:
                return (userID,user)
        return True
    
    def getUserCalorie(self, email, calorieDatabase):
        return calorieDatabase[email]
    
    def getNutrisionistInformation(self, email):
        #Ini belum diisi
        return True
    
    def getMedicalReference(self, need=False):
        if (need):
            doctor=input("Doctor's Name :")
            hospital=input("Hospital's Name :")
            reference_message=input("Message from Nutritionist :")
            reference={'ID':self.consultationID,'Date of Consultation':self.consultationTime,'doctor':doctor,'nutrisionist':nutritionistID,'hospital':hospital,'message':reference_message}
            return reference

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
        # self.ideal = None

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
    
    def saveCalorie(self, email,consumed_cal, ideal_cal, calorieDatabase):
        temp=self.date
        sisa=ideal_cal-consumed_cal
        print("Sisa Kalori Kamu Hari Ini : ",sisa)
        if temp.date()!=datetime.datetime.today().date():
            calorieDatabase[email][str(self.date)]=consumed_cal
        return True
    
    def compareIntake(self, consumed_cal):
        print('\n\nideal: ', self.idealInput, ' consumed: ', consumed_cal)
        if consumed_cal<self.idealInput:
            print("Batas Kalori Masih Aman")
        else:
            print("Warning! Batas Kalori sudah Melebihi Batas!")
    
    def plotGraph(self, calorieDatabase,email):
        plt.plot(calorieDatabase[email].keys(),calorieDatabase[email].values())
        plt.title("Grafik Kalori Harian dari",min(calorieDatabase[email].keys()),"hingga",max(calorieDatabase[email].keys()))
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
            
def login(defaultRole):
    if defaultRole == "non-admin":
        email = input('Email: ')
        password = input('Password: ')
        for user in users:
            status = user.login(email, password)
            if status:
                return user
    elif defaultRole == "admin":
        admin = Admin("admin@class-diagram.id", "admin", True)
        email = input('Email: ')
        password = input('Password: ')
        status = admin.login(email, password)
        if status is not False:
            return admin
        else:
            return None
    
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

def adminManagement(user):
    while True:
        print("\n\n1. Get user information")
        print("2. Delete content")
        print("3. logout")
        choose = int(input('Choose: '))
        if choose == 1:
            email = input("Email to search: ")
            foundUser = user.getUserInformation(users, email)
            if foundUser is None:
                print("No User Found!")
            else:
                print("User found with email:", foundUser.getEmail(), ",With role: ", foundUser.getUserRole())
        elif choose == 2:
            index = input("Index of content to delete: ")
            user.deleteContent(contents, int(index))
        elif choose == 3:
            user.logout()
            return
        else:
            continue

def userManagement(user):
    
    userRole = user.getUserRole()
    email = user.getEmail()

    readMessage(email)
    calorieDatabase={'abc@gmail.com':{'2020-11-01':1000, '2020-11-02':1500,'2020-11-03':1050}, 
    'def@gmail.com':{'2020-11-01':1200, '2020-11-02':1150,'2020-11-03':1300},
    'ghi@gmail.com':{'2020-11-01':1110, '2020-11-02':1000,'2020-11-03':1000}}

    if userRole == 'customer':
        while True:
            print('\n\n1. Send message')
            print('2. calorie record')
            print('3. read content')
            print('4. Change password')
            print('5. logout')
            choose = int(input('Choose: '))

            if choose == 1:
                message = sendMessage(email)
                messages.append(message)
            elif choose == 2:
                activity = input('\n\nActivity [low, moderete, high]: ')
                foodName = input('Food name: ')
                foodCalorie = int(input('Food calorie: '))

                user.consumeFood(activity, foodName, foodCalorie,calorieDatabase)
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
                newPassword = input("New password: ")
                user.changePassword(newPassword)
            elif choose == 5:
                user.logout()
                return
            else:
                continue
    elif userRole == 'nutrisionist':
        while True:
            print('\n\n1. Send message')
            print('2. read content')
            print('3. proofReading')
            print('4. Change password')
            print('5. logout')
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
                newPassword = input("New password: ")
                user.changePassword(newPassword)
            elif choose == 5:
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
            print('6. Change password')
            print('7. logout')
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
                id = int(input('\n\nId content: '))
                title = input('Title: ')
                isi = input('Content: ')
                content = user.editContent(title, isi)
                if content is not None:
                    if contents[id].getContent("writer")["writer"] == user.getEmail():
                        contents[id] = content
                        print('\n\nEdit content success')
                    else:
                        print("\n\nYou are not allowed to edit this content")
            elif choose == 4:
                id = int(input('\n\nId content: '))
                try:
                    user.deleteContent(contents, id)
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
                newPassword = input("New password: ")
                user.changePassword(newPassword)
            elif choose == 7:
                user.logout()
                return
            else:
                continue

def main():
    print('Simple execute program\n\n')
    
    countUser = 0
    while True:
        print('\n\n1. Tambah user')
        print('2. Login as User')
        print('3. Login as Admin')
        print('4. Forget password')
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
            user = login("non-admin")
            if user is not None:
                print('\n\nLogin success')
                userManagement(user)
            else:
                print('\n\nLogin failed')
        elif choose == 3:
            user = login("admin")
            if user is not None:
                print('\n\nLogin success')
                adminManagement(user)
            else:
                print('\n\nLogin failed')
        elif choose == 4:
            email = input("Email: ")
            newPassword = False
            for user in users:
                newPassword = user.forgetPassword(email)
                if newPassword is not False:
                    break
            if newPassword is False:
                print("Email did not match")
            else:
                # Send new password to user's email
                print("Your new password has been sent to your email", newPassword)
if __name__ == '__main__':
    main()