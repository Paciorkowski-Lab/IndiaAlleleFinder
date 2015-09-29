# IndiaAlleleFinder
Tool for annotation of next generation sequencing data with allele frequencies of populations from India.

#How to set up on RedHat:
==Install pip==
1. Follow these instructions: https://pip.pypa.io/en/latest/installing/

aska download the following: https://bootstrap.pypa.io/get-pip.py

and run python get-pip.py

==Install Flask and Packages==
2. Now, pip install flask. http://flask.pocoo.org/docs/0.10/installation/#installation

2.5 make sure you have mysql56-server or its equivalent installed. for example on a mac this would be: sudo port install mysql56-server

3. pip install MySQL-python

4. pip install flask-mysqldb

==Run It==
5. python main.py &

==MySQL Database==

mysql --user app-user --password appdata < mysql-dump.sql
