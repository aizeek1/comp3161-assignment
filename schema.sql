DROP Database IF EXISTS HospitalDB;
CREATE Database HospitalDB;
USE HospitalDB;

DROP Table IF EXISTS patients;
CREATE Table patients(
patientID       char(50) UNIQUE NOT NULL ,
patient_lname   char(50),
patient_fname   char(50),
patient_mname   char(255),
gender          char(25),
patient_dob     date,
PRIMARY KEY(patientID)
);

DROP Table IF EXISTS patient_address; 
CREATE Table patient_address(
patientID   char(50),
city        char(50),
street      char(50),
FOREIGN KEY(patientID) REFERENCES patients(patientID)
);

DROP Table IF EXISTS patient_phoneno;
CREATE Table patient_phoneno(
patientID       char(50),
phone_number    char(50),
foreign key(patientID) references patients(patientID)
);

DROP Table IF EXISTS patient_family;
CREATE Table patient_family(
patientID  char(50),
relativeID char(50),
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(relativeID) REFERENCES patients(patientID)
);

DROP Table IF EXISTS employee;
CREATE Table employee(
employeeID  char(50) UNIQUE NOT NULL,
password    char(50),
lname       char(50),
fname       char(50),
position    char(25),
PRIMARY KEY(employeeID)
);

DROP Table IF EXISTS employee_address; 
CREATE Table employee_address(
employeeID  char(50),
city        char(50),
street      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS employee_phoneno;
CREATE Table employee_phoneno(
employeeID      char(50),
phone_number    char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS doctor;
CREATE Table doctor(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS doctor_intern;
CREATE Table doctor_intern(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS doctor_resident;
CREATE Table doctor_resident(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS doctor_consultant;
CREATE Table doctor_consultant(
employeeID      char(50),
specialization  char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS nurse;
CREATE Table nurse(
employeeID  char(50),
dob         date,
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS nurse_registered;
CREATE Table nurse_registered(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS nurse_midwife;
CREATE Table nurse_midwife(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS nurse_enrolled;
CREATE Table nurse_enrolled(
employeeID      char(50),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS medication;
CREATE Table medication(
medID    char(50) UNIQUE NOT NULL,
name     char(50),
stock    int,
PRIMARY KEY(medID)
);

DROP Table IF EXISTS disease;
CREATE Table disease(
dcode   char(50),
name    char(50),
PRIMARY KEY(dcode)
);

DROP Table IF EXISTS treatment;
CREATE Table treatment(
treatmentID     char(50),
name            char(50),
category        char(50),
PRIMARY KEY(treatmentID)
);

DROP Table IF EXISTS results;
CREATE Table results(
treatmentID      char(50),
description      char(255),
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)
);

DROP Table IF EXISTS scans;
CREATE Table scans(
treatmentID      char(50),
image_location   char(255),
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)
);

DROP Table IF EXISTS procedures;
CREATE Table procedures(
procedureID      char(50),
-- treatmentID      char(50),
description      char(255),
PRIMARY KEY(procedureID)
-- FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)
);

DROP Table IF EXISTS treatment_given;
CREATE Table treatment_given(
patientID       char(50),
treatmentID     char(50),
treatment_type  char(255),
date_given      date,
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(treatmentID) REFERENCES treatment(treatmentID)
);

DROP Table IF EXISTS vitals;
CREATE Table vitals(
vitalID      char(50),
name         char(50),
description  char(255),
PRIMARY KEY(vitalID)
);

DROP Table IF EXISTS diagnosis;
CREATE Table diagnosis(
diagnosisID      char(50),
description      char(255),
PRIMARY KEY(diagnosisID)
);

DROP Table IF EXISTS patient_doctor;
CREATE Table patient_doctor(
patientID   char(50),
employeeID  char(50),
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS medication_disease;
CREATE Table medication_disease(
medID   char(50),
dcode   char(50),
FOREIGN KEY(medID) REFERENCES medication(medID),
FOREIGN KEY(dcode) REFERENCES disease(dcode)
);

DROP Table IF EXISTS medication_given;
CREATE Table medication_given(
patientID   char(50),
medID       char(50),
employeeID  char(50),
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(medID) REFERENCES medication(medID),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID)
);

DROP Table IF EXISTS record;
CREATE Table record(
patientID   char(50),
employeeID  char(50),
diagnosisID char(50),
dcode       char(50),
vitalID     char(50),
record_date date,
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(employeeID) REFERENCES employee(employeeID),
FOREIGN KEY(diagnosisID) REFERENCES diagnosis(diagnosisID),
FOREIGN KEY(dcode) REFERENCES disease(dcode),
FOREIGN KEY(vitalID) REFERENCES vitals(vitalID)
);

-- [patient] and [patient_phoneno] data values --

INSERT INTO patients VALUES ('P-00000001', 'Anderson', 'Abraham', 'Andrew', 'male', '2015/2/28');
INSERT INTO patient_address VALUES ('P-00000001', 'Micheleville', 'Jones Inlet');
INSERT INTO patient_phoneno VALUES ('P-00000001', '+1-(844)-639-0715');
INSERT INTO patients VALUES ('P-00000002', 'Anderson', 'Abigail', 'Angella', 'female', '1952/4/2');
INSERT INTO patient_address VALUES ('P-00000002', 'East Robertview', 'Bailey Divide');
INSERT INTO patient_phoneno VALUES ('P-00000002', '+1-(541)-604-2181');
INSERT INTO patients VALUES ('P-00000003', 'Anderson', 'Andrew', 'Abraham', 'male', '1984/7/10');
INSERT INTO patient_address VALUES ('P-00000003', 'Lake Erin', 'Brittany Drive');
INSERT INTO patient_phoneno VALUES ('P-00000003', '+1-(550)-484-3697');
INSERT INTO patients VALUES ('P-00000004', 'Anderson', 'Angella', 'Abigail', 'female', '1942/1/10');
INSERT INTO patient_address VALUES ('P-00000004', 'Lake Sarah', 'Molly Terrace');
INSERT INTO patient_phoneno VALUES ('P-00000004', '+1-(150)-048-9307');
INSERT INTO patients VALUES ('P-00000005', 'Anderson', 'Arnold', 'Abraham', 'male', '1942/8/4');
INSERT INTO patient_address VALUES ('P-00000005', 'Wolfefort', 'Gonzalez Village');
INSERT INTO patient_phoneno VALUES ('P-00000005', '+1-(621)-878-4751');

INSERT INTO employee VALUES ('D-00000001', 'doctor1', 'Laura', 'Wallace', 'Doctor');
INSERT INTO doctor VALUES ('D-00000001');
INSERT INTO employee_address VALUES ('D-00000001', 'Port Stevenland', '29058 Hendrix Unions');
INSERT INTO employee_phoneno VALUES ('D-00000001', '+1-(502)-219-8449');
INSERT INTO doctor_resident VALUES ('D-00000001');
INSERT INTO employee VALUES ('D-00000002', 'doctor2', 'Andrea', 'Williams', 'Doctor');
INSERT INTO doctor VALUES ('D-00000002');
INSERT INTO employee_address VALUES ('D-00000002', 'Nealburgh', '43706 Bradley Orchard Suite 238');
INSERT INTO employee_phoneno VALUES ('D-00000002', '+1-(516)-554-1736');
INSERT INTO doctor_consultant VALUES ('D-00000002', 'Dermatology');
INSERT INTO employee VALUES ('D-00000003', 'doctor3', 'Anthony', 'Boyle', 'Doctor');
INSERT INTO doctor VALUES ('D-00000003');
INSERT INTO employee_address VALUES ('D-00000003', 'Roberthaven', '4404 Jackson Plains');
INSERT INTO employee_phoneno VALUES ('D-00000003', '+1-(842)-518-6585');
INSERT INTO doctor_intern VALUES ('D-00000003');

INSERT INTO employee VALUES ('N-00000001', 'nurse1', 'Kelly', 'Anderson', 'Nurse');
INSERT INTO nurse VALUES ('N-00000001', '1968/4/14');
INSERT INTO employee_address VALUES ('N-00000001', 'West Douglasside', '7420 Bailey Station Apt. 660');
INSERT INTO employee_phoneno VALUES ('N-00000001', '+1-(951)-902-5103');
INSERT INTO nurse_midwife VALUES ('N-00000001');
INSERT INTO employee VALUES ('N-00000002', 'nurse2', 'Victor', 'Wallace', 'Nurse');
INSERT INTO nurse VALUES ('N-00000002', '1984/4/19');
INSERT INTO employee_address VALUES ('N-00000002', 'Port Brooke', '6485 Daniel View');
INSERT INTO employee_phoneno VALUES ('N-00000002', '+1-(991)-923-6711');
INSERT INTO nurse_enrolled VALUES ('N-00000002');
INSERT INTO employee VALUES ('N-00000003', 'nurse3', 'Jose', 'Anderson', 'Nurse');
INSERT INTO nurse VALUES ('N-00000003', '1984/9/11');
INSERT INTO employee_address VALUES ('N-00000003', 'Navarrochester', '44720 Eugene Alley Suite 144');
INSERT INTO employee_phoneno VALUES ('N-00000003', '+1-(339)-700-8813');
INSERT INTO nurse_registered VALUES ('N-00000003');

INSERT INTO employee VALUES ('S-00000001', 'secretary1', 'Jenna', 'Wu', 'Secretary');
INSERT INTO employee VALUES ('S-00000002', 'secretary2', 'Jesse', 'Reid', 'Secretary');
INSERT INTO employee VALUES ('S-00000003', 'secretary3', 'Christina', 'Fernandez', 'Secretary');
INSERT INTO patient_doctor VALUES ('P-00000001', 'D-00000001');
INSERT INTO patient_doctor VALUES ('P-00000002', 'D-00000001');
INSERT INTO patient_doctor VALUES ('P-00000003', 'D-00000001');
INSERT INTO patient_doctor VALUES ('P-00000004', 'D-00000001');
INSERT INTO patient_doctor VALUES ('P-00000005', 'D-00000001');

INSERT INTO diagnosis VALUES ('DG-00000001', 'influenza');
INSERT INTO diagnosis VALUES ('DG-00000002', 'thyroid fever');
INSERT INTO diagnosis VALUES ('DG-00000003', 'chicken pox');
INSERT INTO diagnosis VALUES ('DG-00000004', 'measels');
INSERT INTO diagnosis VALUES ('DG-00000005', 'HIV');
INSERT INTO diagnosis VALUES ('DG-00000006', 'Hepatitis');
INSERT INTO diagnosis VALUES ('DG-00000007', 'broken bone');
INSERT INTO diagnosis VALUES ('DG-00000008', 'bone fracture');
INSERT INTO diagnosis VALUES ('DG-00000009', 'sprain ligament');
INSERT INTO diagnosis VALUES ('DG-00000010', 'food poisoning');
INSERT INTO diagnosis VALUES ('DG-00000011', 'lead poisoning');
INSERT INTO diagnosis VALUES ('DG-00000012', 'venom poisoning');
INSERT INTO diagnosis VALUES ('DG-00000013', 'liver failure');
INSERT INTO diagnosis VALUES ('DG-00000014', 'heart attack');
INSERT INTO diagnosis VALUES ('DG-00000015', 'lung cancer');
INSERT INTO diagnosis VALUES ('DG-00000016', 'collapsed lung');

INSERT INTO disease VALUES ('VIR-00000001', 'pulmanary disfunction');
INSERT INTO disease VALUES ('VIR-00000002', 'cardiac atrophy');
INSERT INTO disease VALUES ('VIR-00000003', 'acute paralysis');
INSERT INTO disease VALUES ('VIR-00000004', 'neural disfunction');
INSERT INTO disease VALUES ('VIR-00000005', 'auto-immune distress');

INSERT INTO medication VALUES ('MED-00000001', 'antibiotics Type A', 2645);
INSERT INTO medication VALUES ('MED-00000002', 'antibiotics Type B', 2195);
INSERT INTO medication VALUES ('MED-00000003', 'antibiotics Type C', 7939);
INSERT INTO medication VALUES ('MED-00000004', 'painkiller Lvl 1', 6472);
INSERT INTO medication VALUES ('MED-00000005', 'painkiller Lvl 2', 443);
INSERT INTO medication VALUES ('MED-00000006', 'painkiller Lvl 3blood thinners', 8807);
INSERT INTO medication VALUES ('MED-00000007', 'clotting agent', 3931);
INSERT INTO medication VALUES ('MED-00000008', 'protein', 9019);
INSERT INTO medication VALUES ('MED-00000009', 'vitamin A', 2650);
INSERT INTO medication VALUES ('MED-00000010', 'vitamin B', 1049);
INSERT INTO medication VALUES ('MED-00000011', 'vitamin C', 7269);
INSERT INTO medication VALUES ('MED-00000012', 'vitamin D', 4863);
INSERT INTO medication VALUES ('MED-00000013', 'vitamin E', 5133);
INSERT INTO medication VALUES ('MED-00000014', 'calcium', 5652);
INSERT INTO medication VALUES ('MED-00000015', 'water', 7165);

INSERT INTO procedures VALUES ('PRO-00000001', 'surgery');
INSERT INTO procedures VALUES ('PRO-00000002', 'solution injection');
INSERT INTO procedures VALUES ('PRO-00000003', 'observation');
INSERT INTO procedures VALUES ('PRO-00000004', 'blood transfusion');
INSERT INTO procedures VALUES ('PRO-00000005', 'ressusitation');
INSERT INTO procedures VALUES ('PRO-00000006', 'incubation');
INSERT INTO procedures VALUES ('PRO-00000007', 'routine medication');

INSERT INTO treatment VALUES ('TRM-00000001', 'Routine Plan', 'Routine');
INSERT INTO treatment VALUES ('TRM-00000002', 'Routine Plan & Observation', 'Heavy');
INSERT INTO treatment VALUES ('TRM-00000003', 'Emergency Operation', 'Routine');
INSERT INTO treatment VALUES ('TRM-00000004', 'Transfer to Another Ward', 'Routine');
INSERT INTO treatment VALUES ('TRM-00000005', 'Transfer to Another Hospital', 'Routine');

INSERT INTO vitals VALUES ('VIT-00000001', 'heart rate', 'Normal');
INSERT INTO vitals VALUES ('VIT-00000002', 'temperature', 'Low');
INSERT INTO vitals VALUES ('VIT-00000003', ' brain activity', 'Normal');
INSERT INTO vitals VALUES ('VIT-00000004', 'muscle reaction', 'Low');
INSERT INTO vitals VALUES ('VIT-00000005', 'eye sensitivity', 'High');
INSERT INTO vitals VALUES ('VIT-00000006', 'ear sensitivity', 'High');
INSERT INTO vitals VALUES ('VIT-00000007', 'skin sensitivity', 'Low');

INSERT INTO medication_disease VALUES ('MED-00000011', 'VIR-00000001');
INSERT INTO medication_disease VALUES ('MED-00000002', 'VIR-00000001');
INSERT INTO medication_disease VALUES ('MED-00000012', 'VIR-00000001');
INSERT INTO medication_disease VALUES ('MED-00000012', 'VIR-00000001');
INSERT INTO medication_disease VALUES ('MED-00000007', 'VIR-00000001');
INSERT INTO medication_disease VALUES ('MED-00000011', 'VIR-00000002');
INSERT INTO medication_disease VALUES ('MED-00000007', 'VIR-00000002');
INSERT INTO medication_disease VALUES ('MED-00000001', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000011', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000015', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000008', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000014', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000002', 'VIR-00000003');
INSERT INTO medication_disease VALUES ('MED-00000009', 'VIR-00000004');
INSERT INTO medication_disease VALUES ('MED-00000001', 'VIR-00000004');
INSERT INTO medication_disease VALUES ('MED-00000006', 'VIR-00000005');
INSERT INTO medication_disease VALUES ('MED-00000003', 'VIR-00000005');

INSERT INTO record VALUES ('P-00000001', 'D-00000001', 'DG-00000013', 'VIR-00000004', 'VIT-00000004', '2011/8/0');
INSERT INTO treatment_given VALUES ('P-00000001', 'TRM-00000005', 'Standard', '2016/2/8');
INSERT INTO record VALUES ('P-00000002', 'N-00000001', 'DG-00000012', 'VIR-00000002', 'VIT-00000003', '2010/2/16');
INSERT INTO medication_given VALUES ('P-00000002', 'MED-00000010', 'N-00000001');
INSERT INTO record VALUES ('P-00000003', 'N-00000002', 'DG-00000005', 'VIR-00000001', 'VIT-00000002', '2010/6/5');
INSERT INTO medication_given VALUES ('P-00000003', 'MED-00000013', 'N-00000002');
INSERT INTO record VALUES ('P-00000004', 'D-00000001', 'DG-00000014', 'VIR-00000003', 'VIT-00000004', '2009/5/13');
INSERT INTO treatment_given VALUES ('P-00000004', 'TRM-00000005', 'Standard', '2014/2/17');
INSERT INTO record VALUES ('P-00000005', 'N-00000001', 'DG-00000007', 'VIR-00000003', 'VIT-00000003', '2016/1/11');
INSERT INTO medication_given VALUES ('P-00000005', 'MED-00000013', 'N-00000001');

