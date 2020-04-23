#Written By Connor Coddington
#Goal of this file is to get information from Canvas to display on startpage

from flask import Flask, render_template, request, redirect

# Importing canvas class
from canvasapi import canvas, Canvas, course, account, __init__, user
import datetime


#This section gets the cerrent date then puts it in the format YYYYMMDD
#We will use this to find assignments that are not due yet
time = datetime.datetime.now()
time = int(time.strftime('%Y%m%d'))
print("Current date:")
print(time)

#This is the APIKEY for Connor Coddington. It will be deleted when the course ends because it is hosted on a public repository
#For real implementation IT at Florida Poly could get a key that can read all users info
#2607~xmwF872jdubyQweLR2MW56dYcFGKxIGNUnpISSBVfbauXsT8SxIidiTWs4rTMNO3

#To get canvasAPI do "git clone https://github.com/ucfopen/canvasapi.git"

#Florida Poly canvas URL
API_URL = "https://floridapolytechnic.instructure.com/"

#Canvas API key
API_KEY = "2607~xmwF872jdubyQweLR2MW56dYcFGKxIGNUnpISSBVfbauXsT8SxIidiTWs4rTMNO3"

#Create Canvas object
canvas = Canvas(API_URL, API_KEY)

#Get all courses user is currently enrolled in
courses = canvas.get_courses()


#Creating lists to hold assignments, courses, and due dates
counter = 0
todoAssignments = []
todoCourses = []
todoDuedates = []


#This loop is the meat of the file
#It will return a list of assignments, courses, and due dates for assignments that are not due yet
for Course in courses:
    try:
        #print(Course)
        #classes = canvas.get_course(Course)
        #Gets course info for every enrolled course
        classes = canvas.get_course(Course)

        #Gets Every assignment from course
        assignments = classes.get_assignments()

        #This for loop goes through every assignment
        for assignment in assignments:
            #print(assignment)
            #print(assignment.due_at)
            #Removes assignments that do not have a due date
            if (assignment.due_at != None):
                #This section takes the due date and converts it to YYYYMMDD format
                year, month, continueSplit = assignment.due_at.split('-')
                day, unused = continueSplit.split('T')

                #print(year,month,day)
                yearint = int(year)
                monthint = int(month)
                dayint = int(day)
                #print(yearint, monthint, dayint)
                dueDate = (10000*yearint) + (100*monthint) + dayint
                #print(dueDate)

                #Enters this if the assignment is not due yet
                if (dueDate >= time):
                    #print(assignment)
                    #Converts info to strings
                    strcourse = str(Course.name)
                    strassignment = str(assignment.name)
                    strduedate = str(assignment.due_at)

                    #Adds all info lists
                    todoCourses.append(strcourse)
                    todoAssignments.append(strassignment)
                    todoDuedates.append(strduedate)
                    counter = counter + 1
    #Courses from previously enrolled classes go to except
    except:
        pass

#Prints lists to console
print(todoDuedates)
print(todoAssignments)
todoCourses[3] = 'Software Engineering(SP 2020_CEN4010.01 ENGR) '
print(todoCourses)

print("Number of assignments:")
print(len(todoDuedates))

#Nice view of assignments that need to be done in console
for x in range(len(todoDuedates)):
    print("----------New Assignment--------")
    print(todoCourses[x])
    print(todoAssignments[x])
    print(todoDuedates[x])


#Creates dictionary that will be placed in the website
dictOfAssignment = {todoCourses[i] : todoAssignments[i] for i in range(0, len(todoAssignments)) }


#This section interacts with the html files
app = Flask(__name__)

#Returns the assignment info to the website
@app.route('/')
def result():
   return render_template('index.html', result = dictOfAssignment)

#Redirect for credits page
@app.route('/credits', methods = ['GET', 'POST'])
def credits():
    if request.method == 'POST':

        return redirect(url_for('index'))

    return render_template('credits.html')


#Hosting information
if __name__ == '__main__':
   app.run(host="0.0.0.0")
  # app.run(debug = True)
