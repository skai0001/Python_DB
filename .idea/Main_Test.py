
""" Author: Hasan Skaiky
 Date: 24/03/2019
 -unit test"""

import unittest
import mysql.connector

class MyTestCase(unittest.TestCase):
    def test_something(self):

        ''' database connection'''
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mydatabase"
        )
        print "@author: Hasan Skaiky"
        mycursor = mydb.cursor()
        #checks coounts of columns data in db
        mycursor.execute("SELECT COUNT(Years), COUNT(Species) from plants_table")
        expected_result = mycursor.fetchone()
        self.assertEqual(expected_result, (10,10)) #checks if results matches count

if __name__ == '__main__':
    unittest.main()


