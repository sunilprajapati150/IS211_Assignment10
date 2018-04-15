#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" pets database"""

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('pets.db')
    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS person;
        DROP TABLE IF EXISTS pet;
        DROP TABLE IF EXISTS person_pet;
        CREATE TABLE person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);
        CREATE TABLE pet (id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER, dead INTEGER);
        CREATE TABLE person_pet (person_id INTEGER, pet_id INTEGER);
        INSERT INTO person VALUES(1, 'James', 'Smith', 41);
        INSERT INTO person VALUES(2, 'Diana', 'Greene', 23);
        INSERT INTO person VALUES(3, 'Sara', 'White', 27);
        INSERT INTO person VALUES(4, 'William', 'Gibson', 23);
        INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1);
        INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0);
        INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0);
        INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0);
        INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0);
        INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1);
        INSERT INTO person_pet VALUES(1, 1);
        INSERT INTO person_pet VALUES(1, 2);
        INSERT INTO person_pet VALUES(2, 3);
        INSERT INTO person_pet VALUES(2, 4);
        INSERT INTO person_pet VALUES(3, 5);
        INSERT INTO person_pet VALUES(4, 6);
        """)
    con.commit()
    

except lite.Error, e:
    if con:
        con.rollback()
    print "Error {0}".format(e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()
