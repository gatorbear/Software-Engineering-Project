from flask import Flask, render_template, request, redirect



#Written By Connor Coddington
#Goal of this file is to get information from Canvas to display on startpage

# Importing canvas class
from canvasapi import canvas, Canvas, course, account, __init__, user
import datetime


#time = int(datetime.now())
time = datetime.datetime.now()
time = int(time.strftime('%Y%m%d'))
print("Current date:")
print(time)


# time = datetime.datetime.now()
# time.str()
# currentyear, currentmonth, currentday = time.split('-')
# print(currentyear,currentmonth,currentday)
# print(time)

#timeint = 10000*datetime.year + 100*datetime.month + datetime.day
# timeint = int(time)
# print(timeint)

print("I hope you can see this")

#2607~xmwF872jdubyQweLR2MW56dYcFGKxIGNUnpISSBVfbauXsT8SxIidiTWs4rTMNO3

#Florida Poly canvas URL
API_URL = "https://floridapolytechnic.instructure.com/"

#Canvas API key
API_KEY = "2607~xmwF872jdubyQweLR2MW56dYcFGKxIGNUnpISSBVfbauXsT8SxIidiTWs4rTMNO3"

#Create Canvas object
canvas = Canvas(API_URL, API_KEY)



#account = canvas.get_account(4613)
#user = canvas.get_user(4613)
#logins = user.get_user_logins()

#for login in logins:
#    print(login)

courses = canvas.get_courses()

todoCanvas = {'Assignment' : 'Course'}
#todoCanvas
counter = 0
todoAssignments = []
todoCourses = []
todoDuedates = []

for Course in courses:
    try:
        print(Course)
        #classes = canvas.get_course(Course)
        classes = canvas.get_course(Course)

        assignments = classes.get_assignments()

        for assignment in assignments:
            #print(assignment)
            #print(assignment.due_at)
            if (assignment.due_at != None):
                year, month, continueSplit = assignment.due_at.split('-')
                day, unused = continueSplit.split('T')

                #print(year,month,day)
                yearint = int(year)
                monthint = int(month)
                dayint = int(day)
                #print(yearint, monthint, dayint)
                dueDate = (10000*yearint) + (100*monthint) + dayint
                #print(dueDate)
                if (dueDate >= time):
                    #print(assignment)
                    #print("Im NOT DUE YET AAAAHAHHAHAHH")
                    strcourse = str(Course.name)
                    strassignment = str(assignment.name)
                    strduedate = str(assignment.due_at)
                    todoCourses.append(strcourse)
                    todoAssignments.append(strassignment)
                    todoDuedates.append(strduedate)
                    counter = counter + 1
    except:
        pass

print(todoDuedates)
print(todoAssignments)
todoCourses[3] = 'Software Engineering(SP 2020_CEN4010.01 ENGR) '
print(todoCourses)

print(len(todoDuedates))

for x in range(len(todoDuedates)):
    print("----------New Assignment--------")
    print(todoCourses[x])
    print(todoAssignments[x])
    print(todoDuedates[x])



dictOfAssignment = {todoCourses[i] : todoAssignments[i] for i in range(0, len(todoAssignments)) }


app = Flask(__name__)

@app.route('/')
def result():
   return render_template('index.html', result = dictOfAssignment)

@app.route('/credits', methods = ['GET', 'POST'])
def credits():
    if request.method == 'POST':

        return redirect(url_for('index'))

    return render_template('credits.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0")
  # app.run(debug = True)
