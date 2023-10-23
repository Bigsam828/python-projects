#Created by AJS  (Ajayi samuel oluwatimileyin)
#this is a script to calculate the GPA and CGPA for  higher instiution students of higher institutions
#note that the calculations and the grading system used here is based on the grading system used in LASU
#this calculator asks for the total number (n) of semesters a student intends to calculate for 
#then it asks how many subjects a student offered for each semester
#it then collects the course name, course unit, and (it collects either the score(eg 70), and grades it(eg A or B), then converts into course points(eg 5.0 or 4.0 ), or it collects a grade and converts it into course points. no matter the type of value given, it will always be converted fd +-nto course points ) 
#it then calculates the quality points for each course by multiplying the individual course units by the individual course points scored by the student
#it repeats the process for the remaining courses
#it then calculates the sum of the course units and course points for the number of courses specified 
#it then uses the total course units (TCU) and the total quality points (TQP) for the first semester to calculate the GPA by dividing the TQP by the TCU
#then it caculates the CGPA, which is the quotient of the sum of the TQP for number of semesters and the sum of the TCU for the same number of semesters but since the total number of semesters by the first semester is always one: the CGPA by the first semester, is always the same as the GPA for the first semester

# the program simply repeats the above process for the next n-1 number of semesters but collecting the CUs and score or grades or CP for each semester
# and calculates the GPA for each semester
# but unlike the CGPA for the first semester, CGPA by the second semester will not be equal to the the GPA of the second semester. This is because the total quality point and total course unit used to calculate the CGPA by the second semester will be gotten by adding the TQP and TCU used to calculate the GPA for the first and second semester
# And just like that the number of TCUs and TQPs used to calculate for the every suceeding CGPA to calculate will increase based on the number of TCUs and TQPs already calculated

#collecting the user's name
def name_collector():
    fname = input('Please enter your first name')
    mname = input( 'Enter your middle name')
    lname = input ('Enter your last name')
    dept = input('Enter your department')
    names = {fname : fname, mname : mname, lname : lname }
    return names

def position_func():

    '''this function uses the number of semesters (n) a user inputs
    to calculate for the gdp to determine what number of the number
    of semesters(n) the user entered i.e wether the user is asking for the 1st, 2nd, 3rd or nth number of the number of semesters the user entered  '''
    global x
    if i==1 or i== 21 or i == 31 or i == 41:
        x='st'
    elif i==2 or i== 22 or i== 32 or i == 42: 
        x='nd'
    elif i==3 or i== 23 or i== 33 or i == 43:
        x='rd'
    elif i >= 4 :
        x='th'
    else:
        print('Error', end='\n')
        print('Please restart the program and enter a correct value')
    print(x)
    return x

def position_func2():

    '''this function uses the number of courses (q) a user inputs
    to calculate for the gdp to determine what number of the number
    of courses(no_courses_offered) the user entered i.e wether the user is asking for the 1st, 2nd, 3rd or nth number of the number of courses the user entered  '''
    global x
    if q==1 or q== 21 or q== 31:
        x='st'
    elif q==2 or q== 22 or q== 32:
        x='nd'
    elif q==3 or q== 23 or q== 33:
        x='rd'
    elif q>=4 :
        x='th'
    else:
        print('Error', end='\n')
        print('Please restart the program and enter a correct value')
    print(x)
    return x

def score_collector() :
    ''' This function collects the score for a subject
    and checks wether the value entered as the score for
    that subject is correct. It then prints an error message
    if the value entered is wrong. It also collects the units
    for each course'''
    global score
    global course_unit
    
    # collecting the scores and using tests to determine ensure the correct values are entered
    while True:

        score = input(f'please input your score e.g(90, 95) for the {q}{position_func2()} course : ')
        score = score.strip()
        score = score.casefold()
        try: 
            score = int(score)
            if score == ValueError:
                pass

            else:
                break

        except ValueError:
            print('Please enter a correct value (make sure you enter a number)' )
            if score.isalnum():
                print("There shouldn\'t be an alphabet in the score " )


    # collecting the course units and using tests to determine ensure the correct values are entered
    while True:
        course_unit = input('enter the course unit : ')
        try:
            course_unit = int(course_unit)
            if course_unit == ValueError:
                pass

            else:
                break
            
        except ValueError:
            print('Please enter a correct value (make sure you enter a number :) )' )
            if course_unit.isalnum():
                print("There shouldn\'t be an alphabet in the course unit " )
            

            
def score_converter():
    ''' This function calculates the grade point 
    for a particular course by collecting the
    score for a particular course, and then
    comparing it against a set of conditions.
    
    It takes no parameter as the required data(score)
    is collected by the function, when it is called.'''

    global grade_point
    if score >= 70 :
        grade = 'a'
        grade_point= 5.0
    elif (score >= 60 and  score <= 69):
        grade = 'b'
        grade_point = 4.0
    elif (score >= 50 and score <= 59):
        grade = 'c'
        grade_point = 3.0
    elif (score >= 45 and score <= 49):
        grade = 'd'
        grade_point = 2.0
    elif (score >= 40 and score <= 44):
        grade = 'e'
        grade_point = 1.0
    elif score <= 39:
        grade = 'f'
        grade_point = 0.0
    return grade_point
    


def Gpa_calc():   
    global i
    global n
    global q

    #collecting number of iterations/semester and ensuring that the right value is entered
    while 1:
        try:
            n = int(input("For how many semesters do you intend to calculate : "))
            if n == ValueError:
                ...
            else : 
                break
            
        except ValueError:
            print('Oops! that was no valid number. try again')

    # ensuring that a number less than zero is not entered 
    if n<=0:
        print('Error please enter a valid number ')

    else:
        #creating lists to store the sum of the quality points and sum of the course units per semester 
        TQP_list = []
        TCU_list = []
        #creatin a list to store the gpas of every semester 
        Gpa_list = []
        #storing the values of the CGPAs after every semester/iteration in a list 
        CGPA_list=[]
        i=1

        #creating a loop to collect number of courses for the nunber of semesters specified. each iteration is for 1 semester
        while i< n+1:
            #creating lists to store the grade points and course units gotten per course
            grade_points = []
            course_units = []
            quality_points = []

            #collecting number of courses for the current iteration/semester and ensuring that the right value is entered
            while 1:
                try:
                    no_courses_offered=int(input(f'How many courses did you offer for the {i}{position_func()} semester : ')) 
                    if no_courses_offered == ValueError:
                        ...
                    else : 
                        break
            
                except ValueError:
                    print('Oops! that was no valid number. try again')
            
            q=1
            #creating a loop to collect the grade and course units for the number of courses specified. each iteration is 1 course
            
            while q < no_courses_offered+1:
                #using a function to collect the scores
                score_collector()
                
                #storing the grade points in the list created earlier
                grade_points.append(score_converter())
                print('grade points =',grade_points)

                #storing the course units in the list created earlier
                course_units.append(course_unit)    
                print('course_units =',course_units)   

                quality_point = grade_point * course_unit
                quality_points.append(quality_point)
                print('quality_point is =' ,quality_points)
                q+=1
            #summing the quality point values and the course unit values present in the individual lists to get TQP and TCU
            sum_quality_points = sum(quality_points)
            print("total quality point is =",sum_quality_points)
            sum_course_units = sum(course_units)
            print("total course unit is =",sum_course_units)

            #dividing the TQP by TCU to get GPA for a semester
            Gpa  = sum_quality_points/sum_course_units
            print("gpa for ", i,position_func()," semester is =",Gpa)

            #storing the sum of quality points for each semester into a list  
            TQP_list.append(sum_quality_points)
            print("total_quality_points_list =",TQP_list)

            #storing the sum of course unit for each semester into a list
            TCU_list.append(sum_course_units)
            print("total_course_units_list =", TCU_list)

            #storing the GPAs in a list
            Gpa_list.append(Gpa)
            print('Gpa list =', Gpa_list)

            #calculating for CGPA by summing the total course 
            CGPA = sum(TQP_list)/sum(TCU_list)
            print ( 'cgpa  after', i ,position_func(),'semester =',CGPA)
            
            CGPA_list.append(CGPA)
            print('cgpa list = ',CGPA_list)
 
            i+=1

    print(f'list of Gpas for the {n} semesters = {Gpa_list}')  
    print(f'list of CGPAs from the first semester upto the last are {CGPA_list}')





try:x=int(input('Please enter a number'))
except ValueError:
    print('Oops! that was no valid number. try again')
    
Gpa_calc()