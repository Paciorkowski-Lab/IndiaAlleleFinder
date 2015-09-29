# IndiaAlleleFinder
Tool for annotation of next generation sequencing data with allele frequencies of populations from India.

#How to set up on RedHat:
==Install pip==
1. Follow these instructions: https://pip.pypa.io/en/latest/installing/

aska download the following: https://bootstrap.pypa.io/get-pip.py

and run python get-pip.py

==Install Flask and Packages==
2. Now, pip install flask. http://flask.pocoo.org/docs/0.10/installation/#installation

3. sudo pip install MySQL-python

4. sudo pip install flask-mysqldb

5. sudo pip install flask-SQLAlchemy

==Run It==
6. python main.py &

==MySQL Database==

mysql --user user --password password < mysql-dump.sql

then edit the corresponding line in main.py: 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/indiaAlleleFinderDB'