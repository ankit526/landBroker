import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '9826',
    database = 'realstate'
)

cur = connection.cursor()

def getdata(id):
    query = "SELECT * FROM plot where id = "+id
    cur.execute(query)
    rows = cur.fetchall()
    # for row in rows:
    #     print("ID:", row[0])
    #     print("mclient:", row[1])
    #     print("mgov:", row[2])
    #     print("marea:", row[3])
    #     print("empid:", row[4])
    #     print("Address:", row[5])
    #     print("Issue:", row[6])
    #     print("--------------------")
    if(len(rows) == 0):
        return 0
    return rows[0]

def showall():
    query = "SELECT * FROM plot"
    cur.execute(query)
    rows = cur.fetchall()
    # for row in rows:
    #     print("ID:", row[0])
    #     print("mclient:", row[1])
    #     print("mgov:", row[2])
    #     print("marea:", row[3])
    #     print("empid:", row[4])
    #     print("Addresssssss:", row[5])
    #     print("--------------------")
    return rows


def uploadetail(empid, mclient, mgov, marea,address,issue):
    q = "INSERT INTO plot(mclient, mgov, marea, empid,address,issue) VALUES (%s, %s, %s, %s,%s,%s)"
    try:
        cur.execute(q, (mclient, mgov, marea, empid,address,issue))
        connection.commit()  # Commit the transaction
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)


#uploadetail(1, 1000, 1200, 900)
#showall()
