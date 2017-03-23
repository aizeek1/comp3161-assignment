DROP Database IF EXISTS HospitalDB;
CREATE Database HospitalDB;
USE HospitalDB;

DROP Table IF EXISTS patients;
CREATE Table patients(
patientID char(50),
patient_lname char(50),
patient_fname char(50),
patient_mname char(255),
gender char(25),
patient_dob date,
primary key(patientID)
);

DROP Table IF EXISTS patient_phoneno;
CREATE Table patient_phoneno(
patientID char(50),
phone_number char(50),
foreign key(patientID) references patients(patientID)
);

DROP Table IF EXISTS patient_family;
CREATE Table patient_family(
patientID char(50),
relativeID char(50),
FOREIGN KEY(patientID) REFERENCES patients(patientID),
FOREIGN KEY(relativeID) REFERENCES patients(patientID)
);

-- [patient] and [patient_phoneno] data values --

INSERT INTO patients VALUES ('P-00000001', 'Anderson', 'Abraham', 'Andrew', 'male', '2011/11/19');
INSERT INTO patient_phoneno VALUES ('P-00000001', '+1-(233)-443-5920');
INSERT INTO patients VALUES ('P-00000002', 'Anderson', 'Abigail', 'Angella', 'female', '2013/11/30');
INSERT INTO patient_phoneno VALUES ('P-00000002', '+1-(694)-927-0225');
INSERT INTO patients VALUES ('P-00000003', 'Anderson', 'Andrew', 'Abraham', 'male', '1998/10/13');
INSERT INTO patient_phoneno VALUES ('P-00000003', '+1-(499)-604-2163');
INSERT INTO patients VALUES ('P-00000004', 'Anderson', 'Angella', 'Abigail', 'female', '1955/10/21');
INSERT INTO patient_phoneno VALUES ('P-00000004', '+1-(177)-327-5345');
INSERT INTO patients VALUES ('P-00000005', 'Anderson', 'Arnold', 'Abraham', 'male', '1980/2/8');
INSERT INTO patient_phoneno VALUES ('P-00000005', '+1-(575)-866-8986');
INSERT INTO patients VALUES ('P-00000006', 'Anderson', 'Angelica', 'Abigail', 'female', '2017/2/21');
INSERT INTO patient_phoneno VALUES ('P-00000006', '+1-(381)-356-8709');
INSERT INTO patients VALUES ('P-00000007', 'Anderson', 'Benjamin', 'Abraham', 'male', '1987/7/10');
INSERT INTO patient_phoneno VALUES ('P-00000007', '+1-(470)-658-1686');
INSERT INTO patients VALUES ('P-00000008', 'Anderson', 'Amanda', 'Abigail', 'female', '1973/0/9');
INSERT INTO patient_phoneno VALUES ('P-00000008', '+1-(977)-941-5866');
INSERT INTO patients VALUES ('P-00000009', 'Anderson', 'Bill', 'Abraham', 'male', '1945/8/9');
INSERT INTO patient_phoneno VALUES ('P-00000009', '+1-(303)-054-4136');
INSERT INTO patients VALUES ('P-00000010', 'Anderson', 'Ann', 'Abigail', 'female', '1990/6/1');
INSERT INTO patient_phoneno VALUES ('P-00000010', '+1-(442)-747-2642');
INSERT INTO patients VALUES ('P-00000011', 'Anderson', 'Boris', 'Abraham', 'male', '1999/4/14');
INSERT INTO patient_phoneno VALUES ('P-00000011', '+1-(679)-672-7137');
INSERT INTO patients VALUES ('P-00000012', 'Anderson', 'Becky', 'Abigail', 'female', '2016/6/1');
INSERT INTO patient_phoneno VALUES ('P-00000012', '+1-(886)-261-0049');
INSERT INTO patients VALUES ('P-00000013', 'Anderson', 'Carl', 'Abraham', 'male', '1977/5/28');
INSERT INTO patient_phoneno VALUES ('P-00000013', '+1-(858)-747-0298');
INSERT INTO patients VALUES ('P-00000014', 'Anderson', 'Bella', 'Abigail', 'female', '1993/1/11');
INSERT INTO patient_phoneno VALUES ('P-00000014', '+1-(458)-392-2506');
INSERT INTO patients VALUES ('P-00000015', 'Anderson', 'Clifford', 'Abraham', 'male', '2008/12/25');
INSERT INTO patient_phoneno VALUES ('P-00000015', '+1-(473)-816-1163');
INSERT INTO patients VALUES ('P-00000016', 'Anderson', 'Blaire', 'Abigail', 'female', '2010/12/14');
INSERT INTO patient_phoneno VALUES ('P-00000016', '+1-(528)-358-9687');
INSERT INTO patients VALUES ('P-00000017', 'Anderson', 'Clyde', 'Abraham', 'male', '1963/4/26');
INSERT INTO patient_phoneno VALUES ('P-00000017', '+1-(337)-943-5861');
INSERT INTO patients VALUES ('P-00000018', 'Anderson', 'Bonnie', 'Abigail', 'female', '1963/5/1');
INSERT INTO patient_phoneno VALUES ('P-00000018', '+1-(284)-871-2610');
INSERT INTO patients VALUES ('P-00000019', 'Anderson', 'Daniel', 'Abraham', 'male', '1944/8/5');
INSERT INTO patient_phoneno VALUES ('P-00000019', '+1-(571)-492-9175');
INSERT INTO patients VALUES ('P-00000020', 'Anderson', 'Brittney', 'Abigail', 'female', '1998/6/13');
INSERT INTO patient_phoneno VALUES ('P-00000020', '+1-(654)-495-8639');
INSERT INTO patients VALUES ('P-00000021', 'Anderson', 'Dexter', 'Abraham', 'male', '1952/7/13');
INSERT INTO patient_phoneno VALUES ('P-00000021', '+1-(467)-901-8254');
INSERT INTO patients VALUES ('P-00000022', 'Anderson', 'Carly', 'Abigail', 'female', '1980/5/25');
INSERT INTO patient_phoneno VALUES ('P-00000022', '+1-(552)-372-7528');
INSERT INTO patients VALUES ('P-00000023', 'Anderson', 'Douglas', 'Abraham', 'male', '1975/4/1');
INSERT INTO patient_phoneno VALUES ('P-00000023', '+1-(556)-369-2543');
INSERT INTO patients VALUES ('P-00000024', 'Anderson', 'Carlene', 'Abigail', 'female', '2012/9/16');
INSERT INTO patient_phoneno VALUES ('P-00000024', '+1-(663)-170-9624');
INSERT INTO patients VALUES ('P-00000025', 'Anderson', 'Earl', 'Abraham', 'male', '1949/4/26');
INSERT INTO patient_phoneno VALUES ('P-00000025', '+1-(390)-837-0169');
INSERT INTO patients VALUES ('P-00000026', 'Anderson', 'Carrol', 'Abigail', 'female', '2001/6/27');
INSERT INTO patient_phoneno VALUES ('P-00000026', '+1-(716)-098-8099');
INSERT INTO patients VALUES ('P-00000027', 'Anderson', 'EustisEmanuelErick', 'Abraham', 'male', '1997/0/15');
INSERT INTO patient_phoneno VALUES ('P-00000027', '+1-(812)-921-1617');
INSERT INTO patients VALUES ('P-00000028', 'Anderson', 'Christian', 'Abigail', 'female', '2016/12/16');
INSERT INTO patient_phoneno VALUES ('P-00000028', '+1-(689)-840-4525');
INSERT INTO patients VALUES ('P-00000029', 'Anderson', 'Franklin', 'Abraham', 'male', '1995/3/6');
INSERT INTO patient_phoneno VALUES ('P-00000029', '+1-(124)-207-1646');
INSERT INTO patients VALUES ('P-00000030', 'Anderson', 'Clowey', 'Abigail', 'female', '1977/6/12');
INSERT INTO patient_phoneno VALUES ('P-00000030', '+1-(120)-872-1863');
INSERT INTO patients VALUES ('P-00000031', 'Anderson', 'Fredrick', 'Abraham', 'male', '1987/2/8');
INSERT INTO patient_phoneno VALUES ('P-00000031', '+1-(488)-807-8854');
INSERT INTO patients VALUES ('P-00000032', 'Anderson', 'Daniella', 'Abigail', 'female', '2013/4/4');
INSERT INTO patient_phoneno VALUES ('P-00000032', '+1-(299)-144-4715');
INSERT INTO patients VALUES ('P-00000033', 'Anderson', 'Garfield', 'Abraham', 'male', '1983/11/24');
INSERT INTO patient_phoneno VALUES ('P-00000033', '+1-(569)-798-8770');
INSERT INTO patients VALUES ('P-00000034', 'Anderson', 'Emily', 'Abigail', 'female', '1995/0/15');
INSERT INTO patient_phoneno VALUES ('P-00000034', '+1-(549)-633-0949');
INSERT INTO patients VALUES ('P-00000035', 'Anderson', 'Greggory', 'Abraham', 'male', '1990/8/19');
INSERT INTO patient_phoneno VALUES ('P-00000035', '+1-(539)-456-5772');
INSERT INTO patients VALUES ('P-00000036', 'Anderson', 'Eve', 'Abigail', 'female', '1950/9/9');
INSERT INTO patient_phoneno VALUES ('P-00000036', '+1-(115)-269-9450');
INSERT INTO patients VALUES ('P-00000037', 'Anderson', 'Gordon', 'Abraham', 'male', '1973/4/16');
INSERT INTO patient_phoneno VALUES ('P-00000037', '+1-(478)-569-5702');
INSERT INTO patients VALUES ('P-00000038', 'Anderson', 'Fiona', 'Abigail', 'female', '2016/9/19');
INSERT INTO patient_phoneno VALUES ('P-00000038', '+1-(101)-276-9584');
INSERT INTO patients VALUES ('P-00000039', 'Anderson', 'Gabriel', 'Abraham', 'male', '1979/6/7');
INSERT INTO patient_phoneno VALUES ('P-00000039', '+1-(853)-265-7968');
INSERT INTO patients VALUES ('P-00000040', 'Anderson', 'Gabriella', 'Abigail', 'female', '2003/9/17');
INSERT INTO patient_phoneno VALUES ('P-00000040', '+1-(295)-655-5164');
INSERT INTO patients VALUES ('P-00000041', 'Anderson', 'Garry', 'Abraham', 'male', '1982/8/20');
INSERT INTO patient_phoneno VALUES ('P-00000041', '+1-(616)-173-3382');
INSERT INTO patients VALUES ('P-00000042', 'Anderson', 'Heather', 'Abigail', 'female', '1989/12/10');
INSERT INTO patient_phoneno VALUES ('P-00000042', '+1-(533)-158-0529');
INSERT INTO patients VALUES ('P-00000043', 'Anderson', 'Howard', 'Abraham', 'male', '2010/10/18');
INSERT INTO patient_phoneno VALUES ('P-00000043', '+1-(687)-676-5030');
INSERT INTO patients VALUES ('P-00000044', 'Anderson', 'Isabelle', 'Abigail', 'female', '1957/7/12');
INSERT INTO patient_phoneno VALUES ('P-00000044', '+1-(595)-622-5691');
INSERT INTO patients VALUES ('P-00000045', 'Anderson', 'Jack', 'Abraham', 'male', '2015/2/11');
INSERT INTO patient_phoneno VALUES ('P-00000045', '+1-(947)-638-8470');
INSERT INTO patients VALUES ('P-00000046', 'Anderson', 'Jackalin', 'Abigail', 'female', '1975/4/0');
INSERT INTO patient_phoneno VALUES ('P-00000046', '+1-(852)-494-1280');
INSERT INTO patients VALUES ('P-00000047', 'Anderson', 'Jacob', 'Abraham', 'male', '2008/7/22');
INSERT INTO patient_phoneno VALUES ('P-00000047', '+1-(275)-007-5508');
INSERT INTO patients VALUES ('P-00000048', 'Anderson', 'Jennifer', 'Abigail', 'female', '2014/4/30');
INSERT INTO patient_phoneno VALUES ('P-00000048', '+1-(172)-971-3977');
INSERT INTO patients VALUES ('P-00000049', 'Anderson', 'Jackson', 'Abraham', 'male', '2001/4/9');
INSERT INTO patient_phoneno VALUES ('P-00000049', '+1-(549)-222-6507');
INSERT INTO patients VALUES ('P-00000050', 'Anderson', 'Jessica', 'Abigail', 'female', '1956/5/6');
INSERT INTO patient_phoneno VALUES ('P-00000050', '+1-(505)-934-2585');
INSERT INTO patients VALUES ('P-00000051', 'Anderson', 'Justin', 'Abraham', 'male', '1963/7/24');
INSERT INTO patient_phoneno VALUES ('P-00000051', '+1-(623)-386-5605');
INSERT INTO patients VALUES ('P-00000052', 'Anderson', 'Jhenai', 'Abigail', 'female', '1978/7/13');
INSERT INTO patient_phoneno VALUES ('P-00000052', '+1-(394)-907-8601');
INSERT INTO patients VALUES ('P-00000053', 'Anderson', 'Kelly', 'Abraham', 'male', '1990/6/14');
INSERT INTO patient_phoneno VALUES ('P-00000053', '+1-(831)-417-5815');
INSERT INTO patients VALUES ('P-00000054', 'Anderson', 'Jordan', 'Abigail', 'female', '1989/0/7');
INSERT INTO patient_phoneno VALUES ('P-00000054', '+1-(623)-861-7400');
INSERT INTO patients VALUES ('P-00000055', 'Anderson', 'Ken', 'Abraham', 'male', '1960/2/27');
INSERT INTO patient_phoneno VALUES ('P-00000055', '+1-(403)-106-1765');
INSERT INTO patients VALUES ('P-00000056', 'Anderson', 'Josie', 'Abigail', 'female', '1976/8/18');
INSERT INTO patient_phoneno VALUES ('P-00000056', '+1-(237)-014-7591');
INSERT INTO patients VALUES ('P-00000057', 'Anderson', 'Kenneth', 'Abraham', 'male', '1997/9/5');
INSERT INTO patient_phoneno VALUES ('P-00000057', '+1-(354)-331-4526');
INSERT INTO patients VALUES ('P-00000058', 'Anderson', 'Jody', 'Abigail', 'female', '1972/6/26');
INSERT INTO patient_phoneno VALUES ('P-00000058', '+1-(869)-166-7213');
INSERT INTO patients VALUES ('P-00000059', 'Anderson', 'Kevin', 'Abraham', 'male', '1978/0/23');
INSERT INTO patient_phoneno VALUES ('P-00000059', '+1-(775)-612-4600');
INSERT INTO patients VALUES ('P-00000060', 'Anderson', 'Jody-Ann', 'Abigail', 'female', '1952/5/1');
INSERT INTO patient_phoneno VALUES ('P-00000060', '+1-(982)-537-1372');
INSERT INTO patients VALUES ('P-00000061', 'Anderson', 'Keith', 'Abraham', 'male', '2013/6/7');
INSERT INTO patient_phoneno VALUES ('P-00000061', '+1-(320)-602-1633');
INSERT INTO patients VALUES ('P-00000062', 'Anderson', 'Karlene', 'Abigail', 'female', '2016/6/26');
INSERT INTO patient_phoneno VALUES ('P-00000062', '+1-(107)-391-9335');
INSERT INTO patients VALUES ('P-00000063', 'Anderson', 'Lewis', 'Abraham', 'male', '2008/2/13');
INSERT INTO patient_phoneno VALUES ('P-00000063', '+1-(991)-478-7283');
INSERT INTO patients VALUES ('P-00000064', 'Anderson', 'Keezia', 'Abigail', 'female', '1983/9/27');
INSERT INTO patient_phoneno VALUES ('P-00000064', '+1-(481)-341-9480');
INSERT INTO patients VALUES ('P-00000065', 'Anderson', 'Logan', 'Abraham', 'male', '1995/9/22');
INSERT INTO patient_phoneno VALUES ('P-00000065', '+1-(418)-841-6056');
INSERT INTO patients VALUES ('P-00000066', 'Anderson', 'Kelly', 'Abigail', 'female', '1979/12/20');
INSERT INTO patient_phoneno VALUES ('P-00000066', '+1-(500)-059-4137');
INSERT INTO patients VALUES ('P-00000067', 'Anderson', 'Marcus', 'Abraham', 'male', '1945/7/1');
INSERT INTO patient_phoneno VALUES ('P-00000067', '+1-(838)-524-6483');
INSERT INTO patients VALUES ('P-00000068', 'Anderson', 'Kelly-Ann', 'Abigail', 'female', '1976/12/13');
INSERT INTO patient_phoneno VALUES ('P-00000068', '+1-(918)-435-6318');
INSERT INTO patients VALUES ('P-00000069', 'Anderson', 'Maxwell', 'Abraham', 'male', '1989/9/24');
INSERT INTO patient_phoneno VALUES ('P-00000069', '+1-(432)-093-3616');
INSERT INTO patients VALUES ('P-00000070', 'Anderson', 'Kimberly', 'Abigail', 'female', '2013/4/13');
INSERT INTO patient_phoneno VALUES ('P-00000070', '+1-(768)-158-0409');
INSERT INTO patients VALUES ('P-00000071', 'Anderson', 'Mitchum', 'Abraham', 'male', '1949/5/1');
INSERT INTO patient_phoneno VALUES ('P-00000071', '+1-(918)-631-2923');
INSERT INTO patients VALUES ('P-00000072', 'Anderson', 'Levi-Ann', 'Abigail', 'female', '1955/11/22');
INSERT INTO patient_phoneno VALUES ('P-00000072', '+1-(408)-120-2560');
INSERT INTO patients VALUES ('P-00000073', 'Anderson', 'Melvin', 'Abraham', 'male', '1955/8/26');
INSERT INTO patient_phoneno VALUES ('P-00000073', '+1-(282)-602-9007');
INSERT INTO patients VALUES ('P-00000074', 'Anderson', 'Lisa', 'Abigail', 'female', '2001/12/3');
INSERT INTO patient_phoneno VALUES ('P-00000074', '+1-(505)-121-3758');
INSERT INTO patients VALUES ('P-00000075', 'Anderson', 'Morgan', 'Abraham', 'male', '1989/12/9');
INSERT INTO patient_phoneno VALUES ('P-00000075', '+1-(674)-067-2649');
INSERT INTO patients VALUES ('P-00000076', 'Anderson', 'Lucy', 'Abigail', 'female', '1971/6/19');
INSERT INTO patient_phoneno VALUES ('P-00000076', '+1-(729)-319-8308');
INSERT INTO patients VALUES ('P-00000077', 'Anderson', 'Nelson', 'Abraham', 'male', '1956/3/11');
INSERT INTO patient_phoneno VALUES ('P-00000077', '+1-(233)-918-6788');
INSERT INTO patients VALUES ('P-00000078', 'Anderson', 'Mary', 'Abigail', 'female', '2014/10/5');
INSERT INTO patient_phoneno VALUES ('P-00000078', '+1-(817)-517-8750');
INSERT INTO patients VALUES ('P-00000079', 'Anderson', 'Javier', 'Abraham', 'male', '1992/10/5');
INSERT INTO patient_phoneno VALUES ('P-00000079', '+1-(817)-736-5453');
INSERT INTO patients VALUES ('P-00000080', 'Anderson', 'Mary-AnnMellisa', 'Abigail', 'female', '2012/11/2');
INSERT INTO patient_phoneno VALUES ('P-00000080', '+1-(242)-999-0282');
INSERT INTO patients VALUES ('P-00000081', 'Anderson', 'Jordan', 'Abraham', 'male', '1969/9/16');
INSERT INTO patient_phoneno VALUES ('P-00000081', '+1-(633)-463-9872');
INSERT INTO patients VALUES ('P-00000082', 'Anderson', 'Megan', 'Abigail', 'female', '1995/1/24');
INSERT INTO patient_phoneno VALUES ('P-00000082', '+1-(651)-130-6252');
INSERT INTO patients VALUES ('P-00000083', 'Anderson', 'Oliver', 'Abraham', 'male', '2017/0/22');
INSERT INTO patient_phoneno VALUES ('P-00000083', '+1-(965)-364-7280');
INSERT INTO patients VALUES ('P-00000084', 'Anderson', 'Minerva', 'Abigail', 'female', '1956/2/8');
INSERT INTO patient_phoneno VALUES ('P-00000084', '+1-(273)-523-6067');
INSERT INTO patients VALUES ('P-00000085', 'Anderson', 'Osborne', 'Abraham', 'male', '1993/9/18');
INSERT INTO patient_phoneno VALUES ('P-00000085', '+1-(462)-382-3537');
INSERT INTO patients VALUES ('P-00000086', 'Anderson', 'Molly', 'Abigail', 'female', '1970/1/11');
INSERT INTO patient_phoneno VALUES ('P-00000086', '+1-(504)-190-0340');
INSERT INTO patients VALUES ('P-00000087', 'Anderson', 'Patrick', 'Abraham', 'male', '1978/2/10');
INSERT INTO patient_phoneno VALUES ('P-00000087', '+1-(874)-112-1876');
INSERT INTO patients VALUES ('P-00000088', 'Anderson', 'Nicoline', 'Abigail', 'female', '1950/8/20');
INSERT INTO patient_phoneno VALUES ('P-00000088', '+1-(772)-00-1-0494');
INSERT INTO patients VALUES ('P-00000089', 'Anderson', 'Paul', 'Abraham', 'male', '1963/9/8');
INSERT INTO patient_phoneno VALUES ('P-00000089', '+1-(972)-756-1635');
INSERT INTO patients VALUES ('P-00000090', 'Anderson', 'Nelly', 'Abigail', 'female', '1991/4/6');
INSERT INTO patient_phoneno VALUES ('P-00000090', '+1-(472)-841-2735');
INSERT INTO patients VALUES ('P-00000091', 'Anderson', 'Quinton', 'Abraham', 'male', '1951/2/23');
INSERT INTO patient_phoneno VALUES ('P-00000091', '+1-(220)-613-0230');
INSERT INTO patients VALUES ('P-00000092', 'Anderson', 'Olive', 'Abigail', 'female', '1983/0/16');
INSERT INTO patient_phoneno VALUES ('P-00000092', '+1-(679)-227-2998');
INSERT INTO patients VALUES ('P-00000093', 'Anderson', 'Ray', 'Abraham', 'male', '1969/0/28');
INSERT INTO patient_phoneno VALUES ('P-00000093', '+1-(357)-656-6148');
INSERT INTO patients VALUES ('P-00000094', 'Anderson', 'Patrice', 'Abigail', 'female', '1960/2/26');
INSERT INTO patient_phoneno VALUES ('P-00000094', '+1-(313)-294-0660');
INSERT INTO patients VALUES ('P-00000095', 'Anderson', 'Reece', 'Abraham', 'male', '1979/11/7');
INSERT INTO patient_phoneno VALUES ('P-00000095', '+1-(295)-176-5276');
INSERT INTO patients VALUES ('P-00000096', 'Anderson', 'Penelope', 'Abigail', 'female', '1958/5/22');
INSERT INTO patient_phoneno VALUES ('P-00000096', '+1-(736)-119-5785');
INSERT INTO patients VALUES ('P-00000097', 'Anderson', 'Robert', 'Abraham', 'male', '1972/9/9');
INSERT INTO patient_phoneno VALUES ('P-00000097', '+1-(209)-317-1512');
INSERT INTO patients VALUES ('P-00000098', 'Anderson', 'Rebecca', 'Abigail', 'female', '1974/1/24');
INSERT INTO patient_phoneno VALUES ('P-00000098', '+1-(653)-944-9099');
INSERT INTO patients VALUES ('P-00000099', 'Anderson', 'Ronald', 'Abraham', 'male', '2009/10/15');
INSERT INTO patient_phoneno VALUES ('P-00000099', '+1-(406)-667-9446');
INSERT INTO patients VALUES ('P-00000100', 'Anderson', 'Roberta', 'Abigail', 'female', '1986/8/10');
INSERT INTO patient_phoneno VALUES ('P-00000100', '+1-(751)-816-0680');

