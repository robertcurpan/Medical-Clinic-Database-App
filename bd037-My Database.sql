-- Tabela Manopera
SELECT * FROM manopera;

INSERT INTO manopera VALUES (NULL, 'dummy', 0);
INSERT INTO manopera VALUES (NULL, 'ghips', 300);
INSERT INTO manopera VALUES (NULL, 'injectie', 30);
INSERT INTO manopera VALUES (NULL, 'consultatie', 100);
INSERT INTO manopera VALUES (NULL, 'ekg', 200);
INSERT INTO manopera VALUES (NULL, 'electrocauterizare', 150);
INSERT INTO manopera VALUES (NULL, 'masaj', 40);
INSERT INTO manopera VALUES (NULL, 'pansament', 20);
INSERT INTO manopera VALUES (NULL, 'perfuzie', 50);


-- Tabela Sectie
SELECT * FROM sectie;

INSERT INTO sectie VALUES (NULL, 'cardiologie');
INSERT INTO sectie VALUES (NULL, 'dermatologie');
INSERT INTO sectie VALUES (NULL, 'ortopedie');
INSERT INTO sectie VALUES (NULL, 'kineto');
INSERT INTO sectie VALUES (NULL, 'pediatrie');


-- Tabela Boala
SELECT * FROM boala;

INSERT INTO boala VALUES (NULL, 'aritmie cardiaca', 'moderat');
INSERT INTO boala VALUES (NULL, 'leziune piele', 'usor');
INSERT INTO boala VALUES (NULL, 'scolioza', 'usor');
INSERT INTO boala VALUES (NULL, 'durere cap', 'moderat');
INSERT INTO boala VALUES (NULL, 'fractura brat', 'grav');
INSERT INTO boala VALUES (NULL, 'durere spate', 'moderat');
INSERT INTO boala VALUES (NULL, 'rabie', 'usor');
INSERT INTO boala VALUES (NULL, 'leziune piele', 'moderat');
INSERT INTO boala VALUES (NULL, 'fractura picior', 'moderat');
INSERT INTO boala VALUES (NULL, 'palpitatii', 'usor');
INSERT INTO boala VALUES (NULL, 'acnee', 'moderat');
INSERT INTO boala VALUES (NULL, 'dermatita', 'usor');
INSERT INTO boala VALUES (NULL, 'cifoza', 'usor');
INSERT INTO boala VALUES (NULL, 'durere cap', 'usor');
INSERT INTO boala VALUES (NULL, 'fractura brat', 'moderat');
INSERT INTO boala VALUES (NULL, 'viroza', 'usor');
INSERT INTO boala VALUES (NULL, 'varicela', 'moderat');
INSERT INTO boala VALUES (NULL, 'aritmie cardiaca', 'usor');
INSERT INTO boala VALUES (NULL, 'stare de rau', 'moderat');
-- In etapa asta trebuie sa se actualizeze suma de bani din contul unui pacient atunci cand "cumpara" medicamente? (Un trigger poate?)

-- Tabela Pacient
SELECT * FROM pacient;

INSERT INTO pacient VALUES(NULL, 'Popescu Ion', '17-JUN-2000', '0721333444', 'Constanta', 'M', 'popescuion@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Florescu Andrei', '05-MAY-1980', '0723222333', 'Braila', 'M', 'florescuandrei@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Popa Cristina', '02-OCT-1990', '0731444222', 'Vaslui', 'F', 'popacristina123@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Manea Robert', '01-APR-1981', '0732123456', 'Bucuresti', 'M', 'manearobertfcsb@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Ana Cameliu', '15-JUN-1983', '0721111111', 'Bucuresti', 'M', 'malone123@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Grasu Dorian', '10-JAN-1982', '0744123321', 'Bucuresti', 'M', 'grasudorian@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Maticiuc Alexandru', '13-AUG-2001', '0721987789', 'Iasi', 'M', 'maticiucalex1@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Grecu Matei', '14-FEB-1995', '0792123123', 'Craiova', 'M', 'grecumatei123456@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Craciun Andra', '25-DEC-2000', '0712345123', 'Cluj', 'F', 'craciunfericit@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Marcu Elena', '17-APR-2004', '0721393828', 'Oradea', 'F', 'marcuelena@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Toma Catalina', '08-MAR-2005', '0741123124', 'Constanta', 'F', 'tomacat@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Ionescu Ion', '23-OCT-1988', '0752123987', 'Barlad', 'M', 'ionion1212@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Benchea Adriana', '14-FEB-2006', '0731456989', 'Satu Mare', 'F', 'bencheaadriana1@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Fetcu Teodora', '25-JUN-1992', '0734334343', 'Targu Mures', 'F', 'fetcuteo@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Cantea Miruna', '18-JUL-1995', '0721939121', 'Iasi', 'F', 'canteamiruu@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Alexandrescu Alin', '25-MAY-1992', '0744444434', 'Vaslui', 'M', 'alexalin123@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Marin Roxana', '23-NOV-1998', '0721222222', 'Bacau', 'F', 'marinroxy@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Astefanoaei Darius', '14-OCT-2002', '0721123555', 'Botosani', 'M', 'astefanoaeidarius@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Corduneanu Marius', '02-MAY-1998', '0722212339', 'Teleorman', 'M', 'mariuscord@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Birca Ioana', '12-JAN-2001', '0777111111', 'Bacau', 'F', 'bircaioanaaa@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Baciu Bianca', '28-JUL-2000', '0789123221', 'Targu Jiu', 'F', 'baciubianca@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Sadoveanu Claudiu', '21-MAR-1992', '0772123000', 'Sibiu', 'M', 'sadoveanuclau@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Teodosie Maria', '10-JAN-2000', '0721200123', 'Brasov', 'F', 'teoomaria@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Ciobanu Andreea', '24-MAY-1985', '0722396362', 'Brasov', 'F', 'andreeaciobanu@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Glanetasu Ion', '10-JUN-1992', '0722345670', 'Sibiu', 'M', 'ionpamant@gmail.com');
INSERT INTO pacient VALUES(NULL, 'Perca Anca', '13-APR-2000', '0711111321', 'Roman', 'F', 'anca-elena.perca@gmail.com');

-- Tabela Cont
SELECT * FROM cont;

INSERT INTO cont VALUES('1', '1234567812345678', 500);
INSERT INTO cont VALUES('2', '1122334411223344', 1000);
INSERT INTO cont VALUES('3', '5327933342176720', 1200);
INSERT INTO cont VALUES('4', '3058703171469903', 2000);
INSERT INTO cont VALUES('5', '9724475232216772', 450);
INSERT INTO cont VALUES('6', '4317696738384092', 920);
INSERT INTO cont VALUES('7', '2802377965603324', 400);
INSERT INTO cont VALUES('8', '6024725796313902', 1020);
INSERT INTO cont VALUES('9', '9175613850628622', 350);
INSERT INTO cont VALUES('10', '2810914081552596', 300);
INSERT INTO cont VALUES('11', '7256174621759280', 300);
INSERT INTO cont VALUES('12', '8515572509062788', 850);
INSERT INTO cont VALUES('13', '5781468302350412', 250);
INSERT INTO cont VALUES('14', '2250136398756217', 700);
INSERT INTO cont VALUES('15', '8445799608341198', 820);
INSERT INTO cont VALUES('16', '9961169442894011', 900);
INSERT INTO cont VALUES('17', '7772592611313432', 950);
INSERT INTO cont VALUES('18', '7284290248203844', 380);
INSERT INTO cont VALUES('19', '8285594054308174', 750);
INSERT INTO cont VALUES('20', '1572312615660695', 500);
INSERT INTO cont VALUES('21', '5031877452140804', 600);
INSERT INTO cont VALUES('22', '8991102304077258', 1500);
INSERT INTO cont VALUES('23', '5522772657054388', 500);
INSERT INTO cont VALUES('24', '4395018146693905', 2000);
INSERT INTO cont VALUES('25', '2218018853625591', 300);


-- Tabela Medicament
SELECT * FROM medicament;

INSERT INTO medicament VALUES (NULL, 'pastile inima', 80);
INSERT INTO medicament VALUES (NULL, 'crema cicatrizanta', 40);
INSERT INTO medicament VALUES (NULL, 'nurofen', 30);
INSERT INTO medicament VALUES (NULL, 'sindolor gel', 80);
INSERT INTO medicament VALUES (NULL, 'strepsils', 20);
INSERT INTO medicament VALUES (NULL, 'coldrex', 30);
INSERT INTO medicament VALUES (NULL, 'crema fata', 20);
INSERT INTO medicament VALUES (NULL, 'dummy', 0);

-- Tabela Internare
SELECT * FROM internare;

INSERT INTO internare VALUES (NULL, '10-JAN-2019', 1, 2, 2, 4); 
INSERT INTO internare VALUES (NULL, '11-JAN-2019', 2, 1, 1, 5); 
INSERT INTO internare VALUES (NULL, '12-MAR-2019', 3, 4, 3, 7); 
INSERT INTO internare VALUES (NULL, '15-MAY-2013', 9, 5, 16, 1);
INSERT INTO internare VALUES (NULL, '12-OCT-2014', 13, 5, 2, 8); 
INSERT INTO internare VALUES (NULL, '10-DEC-2020', 25, 3, 9, 2);
INSERT INTO internare VALUES (NULL, '25-AUG-2020', 10, 5, 7, 3); 
INSERT INTO internare VALUES (NULL, '10-NOV-2020', 24, 1, 10, 1);
INSERT INTO internare VALUES (NULL, '05-MAR-2021', 4, 1, 18, 5); 
INSERT INTO internare VALUES (NULL, '27-AUG-2021', 18, 4, 6, 7);


-- Tabela M x N
SELECT * FROM Internare_Medicament_Relmxn;

INSERT INTO internare_medicament_relmxn VALUES (1, 2, 1, '10-JAN-2019');
INSERT INTO internare_medicament_relmxn VALUES (2, 1, 3, '11-JAN-2019');
INSERT INTO internare_medicament_relmxn VALUES (3, 8, 1, '12-MAR-2019');
INSERT INTO internare_medicament_relmxn VALUES (4, 6, 6, '15-MAY-2013');
INSERT INTO internare_medicament_relmxn VALUES (5, 2, 1, '13-OCT-2014');
INSERT INTO internare_medicament_relmxn VALUES (6, 3, 3, '10-DEC-2020');
INSERT INTO internare_medicament_relmxn VALUES (7, 8, 1, '25-AUG-2020');
INSERT INTO internare_medicament_relmxn VALUES (8, 1, 3, '10-NOV-2020');
INSERT INTO internare_medicament_relmxn VALUES (9, 1, 5, '05-MAR-2021');
INSERT INTO internare_medicament_relmxn VALUES (10, 4, 1, '28-AUG-2021');


-- Testare functionalitate

-- 1) Numarul total al pacientilor internati la o anumita sectie -> vom face pt cardiologie
SELECT COUNT(*) as "Internari cardiologie"
FROM pacient p, internare i
WHERE p.ID_pacient = i.Pacient_ID_pacient
    AND i.Sectie_ID_sectie = 1;
    
-- 2) Media varstelor (ani) a pacientilor internati la fiecare sectie intr-un anumit an -> vom face pt 2020
SELECT s.denumire, AVG((i.data_internare - p.data_nasterii) / 365)
FROM pacient p, internare i, sectie s
WHERE p.ID_pacient = i.Pacient_ID_pacient AND i.Sectie_ID_sectie = s.ID_Sectie
    AND TO_CHAR(i.data_internare, 'YYYY') = '2020'
GROUP BY s.denumire;

-- 3) Suma totala de bani incasata pe vanzarea medicamentelor intr-un anumit an -> vom face pt 2021
SELECT SUM(m.pret * imr.cantitate) as "Suma bani incasata pe medicamente"
FROM internare i, medicament m, internare_medicament_relmxn imr
WHERE imr.Internare_nr_internare = i.nr_internare AND imr.Medicament_ID_medicament = m.ID_medicament
    AND TO_CHAR(i.data_internare, 'YYYY') = '2021';
    
-- 4) Boala (bolile) cea (cele) mai frecventa(e) in istoria internarilor in clinica (indiferent de gravitate)
SELECT b.denumire as "Denumire boala", COUNT(*) as "Frecventa boala"
FROM boala b, internare i
WHERE i.Boala_ID_boala = b.ID_boala
GROUP BY b.denumire
HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                    FROM internare i, boala b
                    WHERE i.Boala_ID_boala = b.ID_boala
                    GROUP BY b.denumire);

-- 5) Proportia pacientilor care au intampinat forme usoare ale unor boli
SELECT tabela2.nr_usor * 100 / tabela1.nr_tot || '%' as "Procentaj pacienti cu forma usoar a bolii" 
FROM 
    (SELECT COUNT(*) nr_tot FROM internare) tabela1,
    (SELECT COUNT(*) nr_usor FROM internare i, boala b WHERE i.Boala_ID_boala = b.ID_boala AND b.severitate = 'usor') tabela2;
    
-- 6) Care este medicamentul cu cea mai mare cantitate vanduta pana in prezent
SELECT m.denumire, SUM(cantitate) as "Cantitate Max"
FROM internare i, internare_medicament_relmxn imr, medicament m
WHERE imr.Internare_nr_internare = i.nr_internare AND imr.Medicament_ID_medicament = m.ID_medicament
GROUP BY m.denumire
HAVING SUM(cantitate) = (SELECT MAX(SUM(cantitate)) FROM internare_medicament_relmxn GROUP BY Medicament_ID_medicament);

-- 7) Care sunt sectiile cu cele mai multe internari pana in prezent
SELECT s.denumire, COUNT(*) as "Numar de internari"
FROM internare i, sectie s
WHERE i.Sectie_ID_sectie = s.ID_sectie
GROUP BY s.denumire
HAVING COUNT(*) = (SELECT MAX(COUNT(*)) FROM internare GROUP BY Sectie_ID_sectie);


-- Verificare constrangeri

-- 1) CHECK severitate violated (poate lua doar valorile 'usor', 'moderat' si 'grav')
UPDATE boala
SET severitate = 'foarte grav'
WHERE denumire = 'leziune piele';

-- 2) CHECK email violated
UPDATE pacient
SET email='emailfaraarond'
WHERE ID_pacient = 3;

-- 3) TRIGGER data_nasterii (nu putem avea pacienti cu varsta mai mica decat 6 luni)
INSERT INTO pacient VALUES (NULL, 'Andrei Codrin', '15-OCT-2021', '0712345678', NULL, NULL, NULL);

-- 4) CHECK nume violated (numele trebuie sa contine macar un nume de familie si un prenume)
INSERT INTO pacient VALUES (NULL, 'Andrei', '15-OCT-2016', '0712345678', NULL, NULL, NULL);

-- 5) CHECK nume violated (numele nu poate contine cifre)
INSERT INTO pacient VALUES (NULL, 'Andrei Cosmin2', '15-OCT-2016', '0712345678', NULL, NULL, NULL);
