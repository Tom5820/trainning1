import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="customer"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE customer")
# mycursor.execute("CREATE TABLE customers (customerid AUTO_INCREMENT PRIMARY KEY, firstname NVARCHAR(255),lastname NVARCHAR(255), companyname NVARCHAR(255), billingaddress1 NVARCHAR(255), billingaddress2 NVARCHAR(255), city NVARCHAR(255), state NVARCHAR(10), postalcode NVARCHAR(255), country NVARCHAR(255), phonenumber NVARCHAR(12), emailaddress NVARCHAR(150), createdate  DATETIME())")
sql = "INSERT INTO customers (customerid, firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postalcode, country, phonenumber, emailaddress, createdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = [
  ('69906', 'Justin','arsenault',' ','732 eastford rd ',' ', 'southbridge', 'MA', '1550', 'United States', '508-735-9694', 'hondarider2508@gmail.com', '2019-1-10 6:47:00'),
  
  ('69907', 'Wade','Banks',' ',' 606 Ride Way',' ', ' EVANS ', 'GA', '30809', 'United States', '706-836-3122', 'bankswade77@gmail.com', '2019-1-10 7:03:00'),

  ('69908', 'Sean','Powers',' ','293 ROSENSTEEL ',' ', 'SALTSBURG', 'PA', '15681', 'United States', '7244647895', 'bonez62@netzero.com', '2019-1-10 7:31:00'),

  ('69909', 'Riley','Cocke',' Western counters ',' 1008 18th st ',' 4 ', 'Paso Robles', 'CA', '93446', 'United States', '8059752151', 'dailydriven90ls@gmail.com', '2019-1-10 8:27:00'),
  
  ('69910', 'Sherrilyn','Carroll',' ',' 12008 238TH AVE E ',' ', 'BUCKLEY', 'WA', '98321-9680', 'United States', '3608970890', 'action@centurytel.net', '2019-1-10 8:51:00'),
  
  ('69911', 'Ricky','Johnson',' ','144 Velvet Ride Rd ',' ', 'BRADFORD', 'AR', '72020', 'United States', '15012780369', 'rjgalute@gmail.com', '2019-1-10 9:34:00'),
  
  ('69912', 'Sandra','Lemunyon',' Low Koutryn Trukkin','6123 Warner Rd ',' ', 'Columbus', 'GA', '31909', 'United States', '3363546684', 'Crazyred1992@outlook.com', '2019-1-10 9:43:00'),
  
  ('69913', 'Thomas','Campbell',' ','22875 Bravo Place ',' ', 'Salinas', 'CA', '93908', 'United States', '8318097979', 'Soup5511@gmail.com', '2019-1-10 10:44:00'),
  
  ('69914', 'Tom','Crenshaw',' ',' 228 Florence Dr ',' ', 'Aptos', 'CA', '95003', 'United States', '831-431-0906', 'tomcrencat@gmail.com', '2019-1-10 10:49:00'),
  
  ('69915', 'John','Lowery',' 1967 ','887 S ROOESVELT ',' PORTALES ', 'Redding', 'NM', '88130', 'United States', '5752658263', 'tomcrencat@gmail.com', '2019-1-10 10:49:00'),
  
  ('69916', 'Stephen','Schroeder',' ',' 2078 Butte St ',' ', 'Redding', 'CA', '96001', 'United States', '210-421-6098', 'stephencschroeder@sbcglobal.net', '2019-1-10 11:29:00'),
  
  ('69917', 'Vicent','Loesch',' ','732 Minnesota St ',' ', 'Shakopee', 'MN', '55379', 'United States', '6125584360', 'vloesch@comcast.net', '2019-1-10 11:50:00'),
  
  ('69918', 'Thimothy','Pickering',' ',' 166 Capron Farm Dr ',' ', 'Warwich', 'RI', '2886', 'United States', '401-533-6677', 'timepick67@gmail.com', '2019-1-10 12:16:00'),
  
  ('69919', 'Matthew','Gangne',' ',' 167 Brickyard Rd ',' ', 'Southampton', 'MA', '1073', 'United States', '413-326-1338', 'electricmatt@yahoo.com', '2019-1-10 12:18:00'),
  
  ('69920', 'Jeff',' ',' ',' ',' ', '', '', '', '', '', 'justjeffnv@gmail.com', '2019-1-10 12:57:00'),
  
  ('69921', 'James','Sharp',' James ','5318 Acorn ct ',' ', 'League City', 'TX', '77573', 'United States', '2817281319', 'jrsharp1955@comcast.net', '2019-1-10 13:04:00'),
  
  ('69922', 'Lucas','Walker',' ','6744 Bayou Glen Rd ',' ', 'Houston', 'TX', '77057', 'United States', '2108627702', 'lhwalker.cl300@hotmail.com', '2019-1-10 13:14:00'),
  
  ('69923', 'Pierre Andre','Martel',' ','10 DE BRAINE ',' ', 'BLANEVILLE', 'QC', 'j7b1z1', 'Canada', '514-629-0849', 'pierre-andremartel@hotmail.com', '2019-1-10 13:32:00'),

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 