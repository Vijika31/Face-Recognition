import os
import cv2
import csv
import pandas
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
filename = "C:/Users/maragathaganapathi/Documents/Face Recoganization/PeopleData/Data.csv"
face_detector = cv2.CascadeClassifier('C:/Users/maragathaganapathi/Documents/Face Recoganization/haarcascade_frontalface_default.xml')
enrollment = input('\n enter user id end press <return> ==>  ')
name = input('\n enter user name end press <return> ==>  ')
sampleNum = 0
while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number.
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder
                    cv2.imwrite("C:/Users/maragathaganapathi/Documents/Face Recoganization/TrainingImage/ " + name + "." + enrollment + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('Frame', img)
                # wait for 100 miliseconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 190:
                    break
cam.release()
cv2.destroyAllWindows()


with open(filename, 'a+', newline='') as csvFile:
                row = ['Enrollment', 'Name']
                mydict =[{'Enrollment': enrollment,'Name':name}]
                writer = csv.DictWriter(csvFile, fieldnames=row, delimiter=',')
                #writer.writeheader()
                writer.writerows(mydict)
res = "Images Saved for Enrollment : " + enrollment + " Name : " + name