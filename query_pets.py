#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Query Pets script"""

import sqlite3 as lite
import sys

con = None


try:
    con = lite.connect('pets.db')
    con.row_factory = lite.Row

    while True:
        pickPerson = raw_input('Please select an ID number: ')

        if pickPerson == '-1':
            sys.exit()
        else:
            try:
                pickPerson = int(pickPerson)
            except:
                print "Error, please input a number"
                continue

        cur = con.cursor()
        cur.execute("SELECT * FROM person WHERE id =?", [(pickPerson)])
        row = cur.fetchone()

        if row == None:
            print 'Not a valid ID number. Pick again.'
            continue

        print row['first_name'] + ' ' + row['last_name'] + ' is ' + str(
            row['age']) + ' years old.'


        for row in con.execute(
            "SELECT * FROM person_pet WHERE person_id =?", [(pickPerson)]):

            for name in con.execute(
                "SELECT * FROM person WHERE id =?", [(pickPerson)]):
                owner = name['first_name'] + ' ' + name['last_name']

            for petrow in con.execute(
                "SELECT * FROM pet WHERE id =?", [(row['pet_id'])]):

                if petrow['dead'] == 0:
                    print ('- ' + owner + ' owns ' + petrow[
                        'name'] + ', a ' + petrow['breed'] + ' who is ' + str(
                            petrow['age']) + ' years old.')
                else:
                    print ('- ' + owner + ' owned ' + petrow[
                        'name'] + ', a ' + petrow['breed'] + ' who was ' + str(
                            petrow['age']) + ' years old.')


except lite.Error as e:
    print "Closing."
    print "Error: %s " % e.args[0]
    sys.exit(1)

finally:
    if con:
        con.close()
