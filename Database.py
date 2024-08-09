import mysql.connector

# Establish a connection
connection = mysql.connector.connect(
    host='69.48.178.203',
    user='qttnet_2407Blue_User',
    password='d00edjuhme',
    database='qttnet_2407Blue'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM Ammunition")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
connection.close()
#4.4.146.42