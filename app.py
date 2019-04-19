from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

studentDB = [
{
'rollNo':'11',
'name':'John Lewis',
'sec':'A',
},
{
'rollNo':'12',
'name':'shelder jackson',
'sec':'C'
},
{
'rollNo':'21',
'name':'Gary  jackson',
'sec':'F'
},
]

@app.route("/",methods=['GET'])
def welcome():
    return"Welcome to pyhton"

@app.route("/student/getStudents",methods=['GET'])
def getStudents():
    return jsonify({"stud":studentDB})

@app.route("/student/getStudents/<rollNo>",methods=['GET'])
def getStudentdetails(rollNo):
     student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]
     print(student)
     return jsonify({"stud":student})

@app.route("/student/getStudents/<rollNo>",methods=['PUT'])
def updateStudentDetails(rollNo):
     student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]
     if('rollNo' in request.json):
         print("Student available")
     if('name' in request.json):
         student[0]['name']= request.json['name']
     return jsonify({"stud":student[0]})

@app.route("/student/addStudent",methods=['POST'])
def addStudent():
    student= {
    'rollNo':request.json['rollNo'],
    'name':request.json['name'],
    'sec':request.json['sec']
    }
    studentDB.append(student)
    return jsonify({"stud":studentDB})

@app.route("/student/removeStudent/<rollNo>",methods=['DELETE'])
def removeStudent(rollNo):
    student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]
    if(len(student) > 0):
        studentDB.remove(student[0])
    return jsonify({"stud":studentDB})

if(__name__=="__main__"):
    app.run()
