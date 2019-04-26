""" Author: Hasan Skaiky
 Date: 24/03/2019  """


import sys
import datetime
import mysql.connector


''' database connection'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
'''create db object'''
mycursor = mydb.cursor()

''' set to add database data into '''
data_set = {''}

var = 1


''' menu for user selection '''
menu = "\nPlease select one of the following: \n" \
       "1.Reload the data from the database, replacing the in-memory data\n" \
       "2.Display all the records held in the database\n" \
       "3.Create a new record and store it in the data base\n" \
       "4.Select, display and edit a record held in the database\n" \
       "5.Delete a record from the database\n" \
       "6.Add table to the set and sort it\n" \
       "0.EXIT\n\n "

'''''''''''''''''''DATABSE QUERIES'''''''''''''''''''
insert_to_db_rec1 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,169,1,12,0,0,'AF,IW','');")
insert_to_db_rec2 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,172,1,47,0,0,'LP','');")
insert_to_db_rec3 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,175,1,48,0,0,'AF, LP','');")
insert_to_db_rec4 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,178,1,48,3,0,'LP','');")
insert_to_db_rec5 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,181,1,33,3,0,'LP','');")
insert_to_db_rec6 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,184,1,28,8,0,'LP','');")
insert_to_db_rec7 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,188,1,11,25,0,'LP','');")
insert_to_db_rec8 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,190,1,2,24,7,'LP','');")
insert_to_db_rec9 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,193,1,0,8,23,'AF','');")
insert_to_db_rec10 = ("INSERT INTO plants_table VALUES (0,'Dryas integrifolia',2016,196,1,0,0,31,'LP','');")

'''''''''''''''''''END OF QUIERIES'''''''''''''''''''

def main():

    try:
        '''call function print_name() to print authors name '''
        print_name()

        ''' loops through the menu'''
        while var == 1:

                ''' get input from user '''
                user_selection = input(menu)
                type(user_selection)

                ''' checks what users selects '''
                if user_selection == 1:

                    create_db() #create database
                    mycursor.execute("USE mydatabase;") #use the database we created
                    create_db_table() #create table

                    mycursor.execute(insert_to_db_rec1)
                    mycursor.execute(insert_to_db_rec2)
                    mycursor.execute(insert_to_db_rec3)
                    mycursor.execute(insert_to_db_rec4)
                    mycursor.execute(insert_to_db_rec5)
                    mycursor.execute(insert_to_db_rec6)
                    mycursor.execute(insert_to_db_rec7)
                    mycursor.execute(insert_to_db_rec8)
                    mycursor.execute(insert_to_db_rec9)
                    mycursor.execute(insert_to_db_rec10)

                    print "Data has been added..!\n"
                    mydb.commit() #commit to the db

                if user_selection == 2: # displays the table data in db

                    try:
                        print_name()
                        print

                        mycursor.execute("USE mydatabase;") #use the database we created
                        mycursor.execute("Select * FROM  plants_table")
                        for x in mycursor:
                            print(x)
                            print
                    except:
                        print "ERROR_..!"

                ''' get input 3 from user '''
                if user_selection == 3:

                    try:  #this will handle the exceptions and raise errors

                        print_name()
                        print
                        mycursor.execute("USE mydatabase;")

                        species = raw_input('Enter the species:\n')
                        year = input ('Enter the year:\n')
                        julian_year = input('Enter the Julian year:\n')
                        plant_id = input ('Enter the Plant id number:\n')
                        buds_num = input ('Enter the number of buds:\n')
                        flowers_num = input ('Enter the number of flowers:\n')
                        flowers_matured_num = input ('Enter the number of matured flowers:\n')
                        observer = raw_input ('Enter the number of observer:\n')
                        observer_comment = raw_input ('Enter the number of observer comment:\n')

                        mycursor.execute("""INSERT INTO plants_table (Species,Years,Julian_Day_of_Year,Plant_Identification,Number_of_Buds,Number_of_Flowers,Number_of_Flowers_Matured,Observer_Initials,Observer_Comments) 
                                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) """,(species,year,julian_year,plant_id,buds_num,flowers_num,flowers_matured_num,observer,observer_comment))

                        mydb.commit()

                        print "Data has been added ..."

                    except Exception:
                        print "ERROR_..!"
                ''' if users select 4  '''
                if user_selection == 4:

                    ''' "4.Select, display and edit a record held in the simple data structure\n" '''
                    try:
                        print_name()
                        mycursor.execute("USE mydatabase;")

                        #get row id to update
                        select_row_id = input('Please select by index the row you want to edit:\n')

                        #get new Values from user
                        new_species_value = raw_input('Please input the new species value\n')
                        new_years_value   = input('Please input the new years value\n')
                        new_julianDay_value = input('Please input the new Julian Day value\n')
                        new_plantid_value = input('Please input the new Plant Id value\n')
                        new_numbuds_value = input('Please input the new Number of Buds value\n')
                        new_numFlowers_value = input('Please input the new Number of Flowers value\n')
                        new_flowersMatured_value = input('Please input the new Flowers matured value\n')
                        new_observerinit_value = raw_input('Please input the new value\n')
                        new_obsComment_value = raw_input('Please input the new value\n')


                        db_update = "UPDATE plants_table SET Species = %s, Years = %s, Julian_Day_of_Year = %s, Plant_Identification = %s, Number_of_Buds= %s, Number_of_Flowers=%s," \
                                    " Number_of_Flowers_Matured= %s, Observer_Initials=%s, Observer_Comments=%s" \
                                    " WHERE id = %s"


                        val = (new_species_value,new_years_value,new_julianDay_value,new_plantid_value,new_numbuds_value,new_numFlowers_value,
                                new_flowersMatured_value,new_observerinit_value,new_obsComment_value,select_row_id)

                        mycursor.execute(db_update,val)
                        mydb.commit()


                    except:
                        print "ERROR_...!"
                '''if users select option 5'''
                if user_selection == 5:
                    ''''"5.Delete a record from the simple data structure\n" '''
                    try:
                        print_name()
                        mycursor.execute("USE mydatabase;")

                        #get row id to update
                        select_row_id = input('Please select by index the row you want to delete:\n')

                        data_delete = "DELETE FROM plants_table WHERE id = %s"

                        mycursor.execute(data_delete,(select_row_id,))

                        mydb.commit()

                    except:
                        print "ERROR_...!"
                '''if users select option 6'''
                if user_selection == 6: # adds table to the set and sorted

                    try:
                        print_name()
                        mycursor.execute("USE mydatabase;")
                        mycursor.execute("SELECT * FROM plants_table")
                        for x in mycursor:
                            #add table data to Set
                            data_set.add(x)

                        '''print set before sorting'''
                        print ('\n'.join(map(str, data_set)))
                        print_name()
                        print
                        '''print set after sorting'''
                        print ('\n'.join(map(str, sorted(data_set))))

                    except:
                        print "ERROR_...!"


                elif user_selection == 0: # to exits
                    break

    except Exception as e: # handles exceptions
        print (e)          #print error


    finally:               #closes
        mydb.close()
        print "BYE BYE..."


''''''''''''''''''''' Functions '''''''''''''''''''''''

def print_name():
    print "\n@auther: Hasan Skaiky"
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(x)

def create_db():
    delete_db = ("DROP DATABASE IF EXISTS mydatabase;")

    create_db = ("CREATE DATABASE mydatabase;")

    mycursor.execute(delete_db)
    mycursor.execute(create_db)
    print "Database has been created..!\n"

def create_db_table():
    delete_table = ("DROP TABLE IF EXISTS plants_table;")

    create_table = ("""CREATE TABLE plants_table (id INTEGER auto_increment, Species varchar(100), Years year, Julian_Day_of_Year INTEGER, 
                                              Plant_Identification INTEGER,Number_of_Buds INTEGER, Number_of_Flowers INTEGER, 
                                              Number_of_Flowers_Matured INTEGER,Observer_Initials varchar(25),Observer_Comments varchar(50), 
                                              PRIMARY KEY (id) );""")

    mycursor.execute(delete_table)
    mycursor.execute(create_table)
    print "Table has been create..!\n"

''''''''''''''''''''' End of Functions '''''''''''''''''''''

if __name__ == '__main__': main()
