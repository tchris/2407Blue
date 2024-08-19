import mysql.connector

class Ammo:
    def __init__(self, AmmoType = ""):
        self.AmmoType = AmmoType
    
    def cartidge(self, AmmoType):
        connection = mysql.connector.connect(
            host='69.48.178.203',
            user='qttnet_2407Blue_User',
            password='d00edjuhme',
            database='qttnet_2407Blue'
        )
        # Create a cursor object to interact with the database
        cursor = connection.cursor()
        query = "SELECT * FROM `Ammunition 2.0` WHERE `Name` LIKE " + AmmoType
        # Execute a query
        cursor.execute(query)
        # Fetch the results
        results = cursor.fetchall()
        # Close the connection
        connection.close()
        
        return results

