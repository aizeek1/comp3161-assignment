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
from faker import Factory

# Object to assist in making mock data
fake = Factory.create()

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
script.write("DROP Table IF EXISTS patients;\n\
CREATE Table patients(\n\
patientID       char(50) UNIQUE NOT NULL,\n\
patient_lname   char(50),\n\
patient_fname   char(50),\n\
patient_mname   char(255),\n\
gender          char(25),\n\
patient_dob     date,\n\
PRIMARY KEY(patientID)\n\
);\n\n")

## Patient Address Table
script.write("DROP Table IF EXISTS patient_address; \n\
CREATE Table patient_address(\n\
patientID   char(50),\n\
city        char(50),\n\
street      char(50),\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID)\n\
);\n\n")

## Patient-PhoneNo
script.write("DROP Table IF EXISTS patient_phoneno;\n\
CREATE Table patient_phoneno(\n\
patientID       char(50),\n\
phone_number    char(50),\n\
foreign key(patientID) references patients(patientID)\n\
);\n\n")

## Patient-history
script.write("DROP Table IF EXISTS patient_family;\n\
CREATE Table patient_family(\n\
patientID  char(50),\n\
relativeID char(50),\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID),\n\
FOREIGN KEY(relativeID) REFERENCES patients(patientID)\n\
);\n\n")

## Employee Table
script.write("DROP Table IF EXISTS employee;\n\
CREATE Table employee(\n\
employeeID  char(50) UNIQUE NOT NULL,\n\
password    char(50),\n\
lname       char(50),\n\
fname       char(50),\n\
position    char(25),\n\
PRIMARY KEY(employeeID)\n\
);\n\n")

## Employee Address Table
script.write("DROP Table IF EXISTS employee_address; \n\
CREATE Table employee_address(\n\
employeeID  char(50),\n\
city        char(50),\n\
street      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Employee Phone Number Table
script.write("DROP Table IF EXISTS employee_phoneno;\n\
CREATE Table employee_phoneno(\n\
employeeID      char(50),\n\
phone_number    char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Doctor Table
script.write("DROP Table IF EXISTS doctor;\n\
CREATE Table doctor(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Intern Doctor Table
script.write("DROP Table IF EXISTS doctor_intern;\n\
CREATE Table doctor_intern(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Resident Doctor Table
script.write("DROP Table IF EXISTS doctor_resident;\n\
CREATE Table doctor_resident(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Consultant Doctor Table
script.write("DROP Table IF EXISTS doctor_consultant;\n\
CREATE Table doctor_consultant(\n\
employeeID      char(50),\n\
specialization  char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Nurse Table
script.write("DROP Table IF EXISTS nurse;\n\
CREATE Table nurse(\n\
employeeID  char(50),\n\
dob         date,\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Registered Nurse Table
script.write("DROP Table IF EXISTS nurse_registered;\n\
CREATE Table nurse_registered(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Midwife Nurse Table
script.write("DROP Table IF EXISTS nurse_midwife;\n\
CREATE Table nurse_midwife(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Enrolled Nurse Table
script.write("DROP Table IF EXISTS nurse_enrolled;\n\
CREATE Table nurse_enrolled(\n\
employeeID      char(50),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Medication Table
script.write("DROP Table IF EXISTS medication;\n\
CREATE Table medication(\n\
medID    char(50) UNIQUE NOT NULL,\n\
name     char(50),\n\
stock    int,\n\
PRIMARY KEY(medID)\n\
);\n\n")

## Disease Table
script.write("DROP Table IF EXISTS disease;\n\
CREATE Table disease(\n\
dcode   char(50),\n\
name    char(50),\n\
PRIMARY KEY(dcode)\n\
);\n\n")

## Treatment Table
script.write("DROP Table IF EXISTS treatment;\n\
CREATE Table treatment(\n\
treatmentID     char(50),\n\
name            char(50),\n\
category        char(50),\n\
PRIMARY KEY(treatmentID)\n\
);\n\n")

## Results Table
script.write("DROP Table IF EXISTS results;\n\
CREATE Table results(\n\
treatmentID      char(50),\n\
description      char(255),\n\
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)\n\
);\n\n")

## Scans Table
script.write("DROP Table IF EXISTS scans;\n\
CREATE Table scans(\n\
treatmentID      char(50),\n\
image_location   char(255),\n\
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)\n\
);\n\n")

## Procedure Table
script.write("DROP Table IF EXISTS procedures;\n\
CREATE Table procedures(\n\
procedureID      char(50),\n\
-- treatmentID      char(50),\n\
description      char(255),\n\
PRIMARY KEY(procedureID)\n\
-- FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)\n\
);\n\n")

## Treatment Given Table
script.write("DROP Table IF EXISTS treatment_given;\n\
CREATE Table treatment_given(\n\
patientID       char(50),\n\
treatmentID     char(50),\n\
treatment_type  char(255),\n\
date_given      date,\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID),\n\
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)\n\
);\n\n")

## Vitals Table
script.write("DROP Table IF EXISTS vitals;\n\
CREATE Table vitals(\n\
vitalID      char(50),\n\
name         char(50),\n\
description  char(255),\n\
PRIMARY KEY(vitalID)\n\
);\n\n")

## Diagnosis Table
script.write("DROP Table IF EXISTS diagnosis;\n\
CREATE Table diagnosis(\n\
diagnosisID      char(50),\n\
description      char(255),\n\
PRIMARY KEY(diagnosisID)\n\
);\n\n")

script.write("DROP Table IF EXISTS patient_doctor;\n\
CREATE Table patient_doctor(\n\
patientID   char(50),\n\
employeeID  char(50),\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

script.write("DROP Table IF EXISTS medication_disease;\n\
CREATE Table medication_disease(\n\
medID   char(50),\n\
dcode   char(50),\n\
FOREIGN KEY(medID) REFERENCES medication(medID),\n\
FOREIGN KEY(dcode) REFERENCES disease(dcode)\n\
);\n\n")

script.write("DROP Table IF EXISTS medication_given;\n\
CREATE Table medication_given(\n\
patientID   char(50),\n\
medID       char(50),\n\
employeeID  char(50),\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID),\n\
FOREIGN KEY(medID) REFERENCES medication(medID),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)\n\
);\n\n")

## Records Table
script.write("DROP Table IF EXISTS record;\n\
CREATE Table record(\n\
patientID   char(50),\n\
employeeID  char(50),\n\
diagnosisID char(50),\n\
dcode       char(50),\n\
vitalID     char(50),\n\
record_date date,\n\
FOREIGN KEY(patientID) REFERENCES patients(patientID),\n\
FOREIGN KEY(employeeID) REFERENCES employee(employeeID),\n\
FOREIGN KEY(diagnosisID) REFERENCES diagnosis(diagnosisID),\n\
FOREIGN KEY(dcode) REFERENCES disease(dcode),\n\
FOREIGN KEY(vitalID) REFERENCES vitals(vitalID)\n\
);\n\n")

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
employeeIDs = []
doctors = []
nurses = []
secretaries = []

## List of diseases
diagnosi = ['influenza', 'thyroid fever', 'chicken pox', 'measels', 'HIV', 'Hepatitis', 'broken bone', 'bone fracture', 'sprain ligament', 'food poisoning', \
            'lead poisoning', 'venom poisoning', 'liver failure', 'heart attack', 'lung cancer', 'collapsed lung']
vitals = ['heart rate', 'temperature', ' brain activity', 'muscle reaction', 'eye sensitivity', 'ear sensitivity', 'skin sensitivity']            
treatments = ['Routine Plan', 'Routine Plan & Observation', 'Emergency Operation', 'Transfer to Another Ward', 'Transfer to Another Hospital']
diseases = ['pulmanary disfunction', 'cardiac atrophy', 'acute paralysis', 'neural disfunction', 'auto-immune distress']
procedures = ['surgery', 'solution injection', 'observation', 'blood transfusion', 'ressusitation', 'incubation', 'routine medication']
medications = ['antibiotics Type A', 'antibiotics Type B', 'antibiotics Type C', 'painkiller Lvl 1', 'painkiller Lvl 2', 'painkiller Lvl 3' \
                'blood thinners', 'clotting agent', 'protein', 'vitamin A', 'vitamin B', 'vitamin C', 'vitamin D', 'vitamin E', 'calcium', 'water']

## Other IDs
diagnosi_IDs = []
diseasesIDs = []
medicationIDs = []
procedureIDs = []
treatmentIDs = []
vitalIDs = []

## Returns ID string
def createID(prefix, number):
    userID = prefix # Replaced 'P-' with prefix to support multiple IDs of the same structure
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
    
def createRandomDate():
    # Format: yyyy/mm/dd
    dob = '2000/01/01'      # default value
    
    yyyy = 2017 - random.randint(0, 10) # Chooses a year based of base year
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
    addr_sql_template = "INSERT INTO patient_address VALUES ('{}', '{}', '{}');"
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
            userID = createID('P-', userCount +1)   # Creates new User ID
            patientIDs.append(userID)               # Adds new User ID to list
            dob = createRandomBirthday()            # Creates a randon date of birth (format: yyyy/mm/dd)
            street = fake.street_name()             # Uses the Faker library to create random street name
            city = fake.city()                      # Uses the Faker library to create random city
            sql = sql_template.format(userID, lname, fname, mname, gender, dob)
            addr_sql = addr_sql_template.format(userID, city, street)
            script.write(sql)
            script.write("\n")
            script.write(addr_sql)
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

def generateDoctors(amount):
    count = 0
    dr_sql_template = "INSERT INTO employee VALUES ('{}', '{}', '{}', '{}', '{}');"
    addr_sql_template = "INSERT INTO employee_address VALUES ('{}', '{}', '{}');"
    phone_sql_template = "INSERT INTO employee_phoneno VALUES ('{}', '{}');"
    addDr_sql_template = "INSERT INTO doctor VALUES ('{}');"
    intern_sql_template = "INSERT INTO doctor_intern VALUES ('{}');"
    resDr_sql_template = "INSERT INTO doctor_resident VALUES ('{}');"
    conDr_sql_template = "INSERT INTO doctor_consultant VALUES ('{}', '{}');"
    
    specialties = ['Neurology', 'Cardiology', 'Dermatology', 'Pathology', 'Anethisology', 'Citology']
    
    while count < amount:
        # Doctor Bio
        employeeID = createID('D-', count +1)
        employeeIDs.append(employeeID)
        fname = fake.first_name()
        lname = fake.last_name()
        position = 'Doctor'
        password = 'doctor{}'.format((count + 1))
        sql = dr_sql_template.format(employeeID, password, fname, lname, position)
        script.write(sql)
        script.write('\n')
        # Add to Doctor's table
        sql = addDr_sql_template.format(employeeID)
        script.write(sql)
        script.write('\n')
        
        # Doctor Address
        city = fake.city()
        street = fake.street_address()
        sql = addr_sql_template.format(employeeID, city, street)
        script.write(sql)
        script.write('\n')
        
        # Doctor number
        phone = createRandomPhone()
        sql = phone_sql_template.format(employeeID, phone)
        script.write(sql)
        script.write('\n')
        count += 1
        
        # Sequentially gives doctor a category
        if  count % 3 == 0 :
            # Marks Dr as an intern
            doctors.append(employeeID)
            sql = intern_sql_template.format(employeeID)
            script.write(sql)
            script.write('\n')
        elif count % 3 == 1 :
            # Marks Dr as an resident
            doctors.append(employeeID)
            sql = resDr_sql_template.format(employeeID)
            script.write(sql)
            script.write('\n')
        else:
            # Marks Dr as a consultant
            specialty = specialties[random.randint(0, len(specialties) -1)]
            sql = conDr_sql_template.format(employeeID, specialty)
            script.write(sql)
            script.write('\n')
        
    script.write('\n')

def pair_Patients_Doctors():
    maxDocs = len(doctors)
    docIndex = 0
    pair_sql_template = "INSERT INTO patient_doctor VALUES ('{}', '{}');"
    
    for patient in patientIDs:
        # Resets position once at the end of list
        if docIndex >= maxDocs:
            docIndex = 0
        
        sql = pair_sql_template.format(patient, doctors[docIndex])
        script.write(sql)
        script.write('\n')
        
    script.write('\n')

def generateNurses(amount):
    count = 0
    nurse_sql_template = "INSERT INTO employee VALUES ('{}', '{}', '{}', '{}', '{}');"
    addr_sql_template = "INSERT INTO employee_address VALUES ('{}', '{}', '{}');"
    phone_sql_template = "INSERT INTO employee_phoneno VALUES ('{}', '{}');"
    addnurse_sql_template = "INSERT INTO nurse VALUES ('{}', '{}');"
    reg_sql_template = "INSERT INTO nurse_registered VALUES ('{}');"
    mwife_sql_template = "INSERT INTO nurse_midwife VALUES ('{}');"
    enr_sql_template = "INSERT INTO nurse_enrolled VALUES ('{}');"
    
    while count < amount:
        # Nurse Bio
        employeeID = createID('N-', count +1)
        employeeIDs.append(employeeID)
        nurses.append(employeeID)
        fname = fake.first_name()
        lname = fake.last_name()
        position = 'Nurse'
        password = 'nurse{}'.format((count + 1))
        sql = nurse_sql_template.format(employeeID, password, fname, lname, position)
        script.write(sql)
        script.write('\n')
        # Add to Nurse's table
        dob = createRandomBirthday()
        sql = addnurse_sql_template.format(employeeID, dob)
        script.write(sql)
        script.write('\n')
        
        # Doctor Address
        city = fake.city()
        street = fake.street_address()
        sql = addr_sql_template.format(employeeID, city, street)
        script.write(sql)
        script.write('\n')
        
        # Doctor number
        phone = createRandomPhone()
        sql = phone_sql_template.format(employeeID, phone)
        script.write(sql)
        script.write('\n')
        count += 1
        
        # Sequentially gives doctor a category
        if  count % 3 == 0 :
            # Marks Dr as an intern
            sql = reg_sql_template.format(employeeID)
            script.write(sql)
            script.write('\n')
        elif count % 3 == 1 :
            # Marks Dr as an resident
            sql = mwife_sql_template.format(employeeID)
            script.write(sql)
            script.write('\n')
        else:
            # Marks Dr as a consultant
            sql = enr_sql_template.format(employeeID)
            script.write(sql)
            script.write('\n')
        
    script.write('\n')
    
def generateSecretaries(amount):
    count = 0
    sec_sql_template = "INSERT INTO employee VALUES ('{}', '{}', '{}', '{}', '{}');"
    addr_sql_template = "INSERT INTO employee_address VALUES ('{}', '{}', '{}');"
    phone_sql_template = "INSERT INTO employee_phoneno VALUES ('{}', '{}');"
    
    while count < amount:
        # Secretary Bio
        employeeID = createID('S-', count +1)
        employeeIDs.append(employeeID)
        secretaries.append(employeeID)
        fname = fake.first_name()
        lname = fake.last_name()
        position = 'Secretary'
        password = 'secretary{}'.format((count + 1))
        sql = sec_sql_template.format(employeeID, password, fname, lname, position)
        script.write(sql)
        script.write('\n')
        count += 1

def generateMedication():
    count = 0
    med_sql_template = "INSERT INTO medication VALUES ('{}', '{}', {});"
    for medicine in medications:
        medID = createID('MED-', count +1)
        medicationIDs.append(medID)
        stock = random.randint(0, 10000)
        sql = med_sql_template.format(medID, medicine, stock)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def generateDiseases():
    count = 0
    dis_sql_template = "INSERT INTO disease VALUES ('{}', '{}');"
    for virus in diseases:
        dcode = createID('VIR-', count +1)
        diseasesIDs.append(dcode)
        sql = dis_sql_template.format(dcode, virus)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def generateTreatments():
    count = 0
    sql_template = "INSERT INTO treatment VALUES ('{}', '{}', '{}');"
    for treat in treatments:
        ID = createID('TRM-', count +1)
        treatmentIDs.append(ID)
        # Randomly chooses a type for SQL
        choice = random.randint(0, 3)
        if choice == 0:
            case_type = 'Light'
        elif choice == 1:
            case_type = 'Routine'
        else:
            case_type = 'Heavy'
            
        sql = sql_template.format(ID, treat, case_type)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def generateVitals():
    count = 0
    sql_template = "INSERT INTO vitals VALUES ('{}', '{}', '{}');"
    for treat in vitals:
        ID = createID('VIT-', count +1)
        vitalIDs.append(ID)
        # Randomly chooses a type for SQL
        choice = random.randint(0, 3)
        if choice == 0:
            case_type = 'High'
        elif choice == 1:
            case_type = 'Low'
        else:
            case_type = 'Normal'
            
        sql = sql_template.format(ID, treat, case_type)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def generateDiagnosi():
    count = 0
    sql_template = "INSERT INTO diagnosis VALUES ('{}', '{}');"
    for treat in diagnosi:
        ID = createID('DG-', count +1)
        diagnosi_IDs.append(ID)
        sql = sql_template.format(ID, treat)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def generateProcedures():
    count = 0
    sql_template = "INSERT INTO procedures VALUES ('{}', '{}');"
    for treat in procedures:
        ID = createID("PRO-", count +1)
        procedureIDs.append(ID)
        sql = sql_template.format(ID, treat)
        script.write(sql)
        script.write('\n')
        count +=1
        
    script.write('\n')
    
def pair_Medication_Disease():
    sql_template = "INSERT INTO medication_disease VALUES ('{}', '{}');"
    for virus in diseasesIDs:
        amount = random.randint(1, 6)    # creates a random amount of medicine needed for virus
        count = 0
        while count < amount:
            i = random.randint(0, len(medicationIDs) -1)
            sql = sql_template.format(medicationIDs[i], virus)
            script.write(sql)
            script.write('\n')
            count +=1
        
    script.write('\n')  
    
def generateRecord(amount):
    count = 0
    
    sql_template = "INSERT INTO record VALUES ('{}', '{}', '{}', '{}', '{}', '{}');"
    sql2_template= "INSERT INTO treatment_given VALUES ('{}', '{}', '{}', '{}');"
    sql3_template= "INSERT INTO medication_given VALUES ('{}', '{}', '{}');"
    if count < amount:
        for ID in patientIDs:
            choice = random.randint(0,2)
            if choice == 0:
                employee = doctors[random.randint(0, len(doctors) -1)]
            else :
                employee = nurses[random.randint(0, len(doctors) -1)]
            
            diagnosis = diagnosi_IDs[random.randint(0, len(diagnosi_IDs) -1)]
            vital = vitalIDs[random.randint(0, len(vitalIDs) -1)]
            disease = diseasesIDs[random.randint(0, len(diseasesIDs) -1)]
            record_date = createRandomDate()
            
            # Creates the record
            sql = sql_template.format(ID, employee, diagnosis, disease, vital, record_date)
            script.write(sql)
            script.write('\n')
            
            ## --FIX----
            #Creates the treatment
            if choice == 0:
                treatment = treatmentIDs[random.randint(0, len(treatmentIDs) -1)]
                date_given = createRandomDate()
                desc = 'Standard'
                sql = sql2_template.format(ID, treatment, desc, date_given)
                script.write(sql)
                script.write('\n')
            else:
                medication = medicationIDs[random.randint(0, len(medicationIDs) -1)]
                sql = sql3_template.format(ID, medication, employee)
                script.write(sql)
                script.write('\n')
            
            ## --END_OF_ISSUE---
            count += 1
            if count >= amount:
                break
        # END-- of FOR-LOOP
        
    # END-- of IF-Statement
    script.write('\n')
    
###
#  END of Script
###
amount = 5
workers=3

generateUsers(amount)
generateDoctors(workers)
generateNurses(workers)
generateSecretaries(workers)

pair_Patients_Doctors()
generateDiagnosi()
generateDiseases()
generateMedication()
generateProcedures()
generateTreatments()
generateVitals()
pair_Medication_Disease()

generateRecord(300)

print 'Doctors: {}, Patients: {}'.format(len(doctors), len(patientIDs))
print "Done."
script.close()