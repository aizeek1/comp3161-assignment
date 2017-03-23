'''
----------------
Python Script
----------------
Code that should generate a SQL file that will:
1. Create a database
2. Create tables
3. Populate tables

The tables section can be adjusted easily.
A loop that will ask for an amount will be made
'''

import os
import random
from sys import argv

filename = 'schema.sql'

## IF script exists
if os.path.exists("./schema.sql"):
    print "Updating script..."
    
## Create Database
script = open(filename, 'w')
script.write("DROP Database IF EXISTS HospitalDB;")
script.write("\n")
script.write("CREATE Database HospitalDB;")
script.write("\n")
script.write("USE HospitalDB;")
script.write("\n\n")

###
# Create Tables
###

## Patient Table
script.write("DROP Table IF EXISTS patients;")
script.write("\n")
script.write("CREATE Table patients(")
script.write("\n")
script.write("patientID char(50),")
script.write("\n")
script.write("patient_lname char(50),")
script.write("\n")
script.write("patient_fname char(50),")
script.write("\n")
script.write("patient_mname char(255),")
script.write("\n")
script.write("gender char(25),")
script.write("\n")
script.write("patient_dob date,")
script.write("\n")
script.write("primary key(patientID)")
script.write("\n")
script.write(");")
script.write("\n\n")

## Patient-PhoneNo
script.write("DROP Table IF EXISTS patient_phoneno;")
script.write("\n")
script.write("CREATE Table patient_phoneno(")
script.write("\n")
script.write("patientID char(50),")
script.write("\n")
script.write("phone_number char(50),")
script.write("\n")
script.write("foreign key(patientID) references patients(patientID)")
script.write("\n")
script.write(");")
script.write("\n\n")

## Patient-history
script.write("DROP Table IF EXISTS patient_family;")
script.write("\n")
script.write("CREATE Table patient_family(")
script.write("\n")
script.write("patientID char(50),")
script.write("\n")
script.write("relativeID char(50),")
script.write("\n")
script.write("FOREIGN KEY(patientID) REFERENCES patients(patientID),")
script.write("\n")
script.write("FOREIGN KEY(relativeID) REFERENCES patients(patientID)")
script.write("\n")
script.write(");")
script.write("\n\n")

###
#  DB Population Section
###

## List of all names (Christian names can serve as middle names)
surnames = ['Anderson', "Andrews", 'Beckford', 'Brooks', 'Bryan', 'Campbell', 'Cruz', 'Davis', 'Dawson', 'Dixon', 'Donaldson', 'Dunn', 'Douglas',\
            'Evans','Ford', "Gibson", 'Golding', 'Gonzales', 'Henriques', 'Holdson', 'Jackson', 'Jefferson', 'Kennedy', 'Koleman', 'Lewis', 'Lopez', 'McDonald', \
            'McIntyre', 'Miller', 'Morgan', 'Morrison', 'Nelson', 'Newman', 'Osborne', 'Patterson', 'Pinnock', 'Powers', 'Quinn', 'Reed', 'Robinson', "Sanders", \
            'Simmons', 'Taylor', 'Teape', 'Trowers', 'Valentine', 'Vermillion', 'Walborn', 'Watson', 'Williams', 'Wolfe', 'Wilson', "Xanders", 'Yipp', 'Zolerman']

christianMaleNames = ['Abraham', 'Andrew', 'Arnold', 'Benjamin', 'Bill', 'Boris', 'Carl', 'Clifford', 'Clyde', 'Daniel', 'Dexter', 'Douglas', 'Earl', 'Eustis' \
                      'Emanuel' 'Erick', 'Franklin', 'Fredrick',  'Garfield','Greggory', 'Gordon', 'Gabriel', 'Garry', 'Howard', 'Jack', 'Jacob', 'Jackson', \
                      'Justin', 'Kelly', 'Ken', 'Kenneth', 'Kevin', 'Keith', 'Lewis', 'Logan', 'Marcus', 'Maxwell', 'Mitchum', 'Melvin', 'Morgan', 'Nelson', \
                      'Javier', 'Jordan', 'Oliver', 'Osborne', 'Patrick', 'Paul', 'Quinton', 'Ray', 'Reece', 'Robert', 'Ronald', 'Samuel', 'Simon', \
                      'Timothy', 'Tyrese', 'Uther', 'Vincent', 'Wallace', 'Watson', 'Wendel', 'West', 'Wilbert', 'Willis', 'William', 'Wilson', 'Xander', \
                      'Xavier', 'Zackery']

christianFemaleNames = ['Abigail', 'Angella', 'Angelica', 'Amanda', 'Ann', 'Becky', 'Bella', 'Blaire', 'Bonnie', 'Brittney', 'Carly', 'Carlene', 'Carrol',  \
                        'Christian', 'Clowey', 'Daniella', 'Emily', 'Eve', 'Fiona', 'Gabriella', 'Heather', 'Isabelle', 'Jackalin','Jennifer', 'Jessica', \
                        'Jhenai', 'Jordan', 'Josie', 'Jody', 'Jody-Ann', 'Karlene', 'Keezia', 'Kelly', 'Kelly-Ann', 'Kimberly', 'Levi-Ann', 'Lisa', 'Lucy', \
                        'Mary', 'Mary-Ann' 'Mellisa', 'Megan', 'Minerva', 'Molly', 'Nicoline', 'Nelly', 'Olive', 'Patrice', 'Penelope', 'Rebecca', 'Roberta', 'Samantha', \
                        'Sara', 'Simone', 'Susane', 'Taylor', 'Tiffany', 'Trisha', 'Trudy', 'Trudy-Ann', 'Ulga', 'Valentine', 'Victoria', 'Wanda', 'Wendy', 'Yvone', 'Zoey']

## List of all primary keys (for tracking and assigning purposes - to create connection within db)
patientIDs = []

## Returns ID string
def createUserID(number):
    userID = 'P-'
    # ID will have a 8 digit padding
    if number < 10:
        userID += '0000000{}'.format(number)
    elif number < 100:
        userID += '000000{}'.format(number)
    elif number < 1000:
        userID += '00000{}'.format(number)
    elif number < 10000:
        userID += '0000{}'.format(number)
    elif number < 100000:
        userID += '000{}'.format(number)
    elif number < 1000000:
        userID += '00{}'.format(number)
    elif number < 10000000:
        userID += '0{}'.format(number)
    else:
        userID += '{}'.format(number)

    return userID

## Returns a random date of birth
def createRandomBirthday():
    # Format: yyyy/mm/dd
    dob = '2000/01/01'      # default value
    
    yyyy = 2017 - random.randint(0, 75) # Chooses a year based of base year
    mm = random.randint(0,12)
    dd = random.randint(0,30)
    ## Adjustment for the month of February
    if mm == 2:
        dd = random.randint(0,28)
        
    
    dob = "{}/{}/{}".format(yyyy,mm,dd)
    return dob
    
## Returns a random phone number
def createRandomPhone():
    phone_template = '+1-({})-{}-{}'
    areacode = random.randint(99,999)
    partA = random.randint(0,1000) - 1
    partB = random.randint(0,10000) - 1
    
    # Add Padding (if necessary) for parts A and B
    if partA < 10:
        numA = '00{}'.format(partA)
    elif partA < 100:
        numA = '0{}'.format(partA)
    else:
        numA = '{}'.format(partA)
    
    if partB < 10:
        numB = '000{}'.format(partB)
    elif partB < 100:
        numB = '00{}'.format(partB)
    elif partB < 1000:
        numB = '0{}'.format(partB)
    else:
        numB = '{}'.format(partB)
        
    phone = phone_template.format(areacode, numA, numB)
    return phone
    
## Returns a single string with all the middle names
def getMiddleNames(amount, isMale, names, fname):
    mname = ""
    
    # Ensures that the first name and middle names are not the same
    if (fname in names):
        #print "[GetMiddleNames]: replacing..."
        if isMale:
            # Use for loop to choose a name from the list, breaking when it finds one not in use
            for name in christianMaleNames:
                if not(name in fname):
                    #print "[GetMiddleNames]: changing {} for {}...".format(fname, name)
                    names = names.replace(fname, name)
                    break
        else:
            # Use for loop to choose a name from the list, breaking when it finds one not in use
            for name in christianFemaleNames:
                if not(name in fname):
                    #print "[GetMiddleNames]: changing {} for {}...".format(fname, name)
                    names = names.replace(fname, name)
                    break
                
    if (amount <= 0):
        return names
    else:
        # Choose from the gender
        if isMale:
            # Use for loop to choose a name from the list, breaking when it finds one not in use
            for name in christianMaleNames:
                if not(name in names):
                    mname = name
                    break
        else:
            # Use for loop to choose a name from the list, breaking when it finds one not in use
            for name in christianFemaleNames:
                if not(name in names):
                    mname = name
                    break
    
    return  getMiddleNames(amount -1, gender, names + ' ' + mname)
    
## Generates all users
def generateUsers(amount):
    # Variables to keep track of users and the names available
    userCount = 0
    lname_count = len(surnames)
    male_names = len(christianMaleNames)
    female_names = len(christianFemaleNames)
    
    # Variable for assisting in tracking user generation when alternating between new male and female user
    name_limit = 0
    if male_names > female_names:
        name_limit = male_names
    else:
        name_limit = female_names
        
    '''
    Cycle that will create script to insert new user data
    '''
    # Section Heading
    script.write("-- [patient] and [patient_phoneno] data values --\n\n")
    
    lname_index = 0
    fname_index = 0
    mname_index = 0
    male_mname_count = 0
    female_mname_count = 0
    isMale = True
    skipStep = False    # Triggers the off-case where it should move to the next position
    sql_template = "INSERT INTO patients VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"
    phone_sql_template = "INSERT INTO patient_phoneno VALUES ('{}', '{}');"
    while userCount < amount:
        #
        
        # Will create users starting from middle name, then last name, then first name
        if isMale and (fname_index < len(christianMaleNames)) and not(skipStep):
            gender = 'male'
            fname = christianMaleNames[fname_index]
            mname = getMiddleNames(male_mname_count, isMale,christianMaleNames[mname_index], fname)
            isMale = False  # Causes next run to create a female user
            #print "{} {} {}\n".format(fname, mname, gender)
        elif (fname_index < len(christianFemaleNames)) and not(skipStep):
            fname = christianFemaleNames[fname_index]
            mname = getMiddleNames(female_mname_count, isMale,christianFemaleNames[mname_index], fname)
            gender = 'female'
            isMale = True   # Causes next run to create a male user
            skipStep = True
            #print "{} {} {}\n".format(fname, mname, gender)
        else:
            # Moves to the next name location after a male and female user is made
            fname_index += 1
            isMale = True
            skipStep = False
            #print "[SKIPPING] FirstName Index: {}".format(fname_index)
            
        # Runs as long as we didn't use up all of the first name combinations
        if not(skipStep):
            lname = surnames[lname_index]           # Gets a last name from the list of surnames
            userID = createUserID(userCount +1)     # Creates new User ID
            patientIDs.append(userID)               # Adds new User ID to list
            dob = createRandomBirthday()            # Creates a randon date of birth (format: yyyy/mm/dd)
            sql = sql_template.format(userID, lname, fname, mname, gender, dob)
            script.write(sql)
            script.write("\n")
            userCount += 1
            
            # Gives each user (despite age) a number
            phone = createRandomPhone()             # Creates a random phone number for user
            phone_sql = phone_sql_template.format(userID, phone)
            script.write(phone_sql)
            script.write("\n")
        
        # Checks if all of the first names were used up
        if fname_index >= name_limit:
            fname_index = 0
            lname_index += 1
        # Checks if all of the last names were used up
        if lname_index >= len(surnames):
            lname_index = 0
            mname_index +=1
        # Checks if we used up all of the middle name before increasing middle names
        if (mname_index >= male_names) and isMale and not(skipStep):
            male_mname_count += 1
        if (mname_index >= female_names) and not(isMale) and not(skipStep):
            female_mname_count += 1
        # Resets the index for middle name (Assuming count is set to add new mname)
        if mname_index >= name_limit:
            mname_index = 0
            
    script.write("\n")
    
    ### END of generateUser function ###

###
#  END of Script
###
generateUsers(100)
print "Done."
script.close()