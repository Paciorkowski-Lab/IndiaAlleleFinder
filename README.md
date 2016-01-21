
# IndiaAlleleFinder
A tool for annotation of next generation sequencing data with allele frequencies of populations from India.

#How to set up on RedHat:
##Perl Version -- Current Implementation At URMC
Before anything happens, make sure you have the latest version of Perl. 

1. Now, install Catalyst, the Perl MVC from which the website is hosted. To quote the installation instructions from BrainBase:

> I'm really sorry about this. Perl Catalyst is fantastic and amazing.
> But installation can sometimes be a route to no happiness. The most
> certain way to have a bad time installing Perl Catalyst is to try to
> install it on an old Linux system. By "old" I mean anything that is
> not running the most up-to-date kernel. I have the best experience
> installing Perl Catalyst right on top of a fresh Linux install.

    perl -MCPAN -e 'install Catalyst::Runtime'
    perl -MCPAN -e 'install Catalyst::Devel'
2. You will need the following Catalyst Plugins from CPAN:
    Catalyst::Plugin::Authentication
    Catalyst::Authentication::Realm::SimpleDB
    Catalyst::Plugin::Session
    Catalyst::Plugin::Session::Store::File
    Catalyst::Plugin::Session::State::Cookie
    Catalyst::Helper::Model::DBIC::Schema
    Catalyst::Controller::FormBuilder
    Catalyst::View::TT
    MooseX::MarkAsMethods
    MooseX::NonMoose
    DBIx::Class::Schema::Loader
    DBIx::Class::TimeStamp
    DBIx::Class::PassphraseColumn
    HTML::FormHandler::Model::DBIC
There is a way to get MCPAN to auto install all these modules without the prompt asking you for yes / no inputs. 

To do this, simply bring up a CPAN shell:

    perl -MCPAN -e shell

Run these two commands in the CPAN shell:

    o conf prerequisites_policy follow
    o conf commit

Now, exit the CPAN shell, start the CPAN shell, and try to install a module that you need. All dependencies will be automatically confirmed, downloaded and installed. (from https://major.io/2009/01/01/cpan-automatically-install-dependencies-without-confirmation/)
3. put this code into a directory from where you normally host websites.
4. Configure MySQL / MariaDB for your Linux System. For Slackware 14.1 I follow the directions here: http://docs.slackware.com/howtos:databases:install_mysql_on_slackware 
If you follow the directions closely you should have no problem.
6. Once MySQL is configured log in as root:
$ mysql -u root -p
..
MariaDB>
Check that InnoDB is supported.
MariaDB> SHOW VARIABLES LIKE 'have_innodb';
If mysql returns the value as YES it is supported.
7. Create a database called IndiaAlleleFinderDB

    MariaDB> CREATE DATABASE IndiaAlleleFinderDB;
    MariaDB> GRANT ALL PRIVILEGES ON IndiaAlleleFinderDB.* TO [username] IDENTIFIED BY '[PASSWORD]';
    MariaDB> FLUSH PRIVILEGES;
    MariaDB> exit
    Bye
8. Configure mysql: 

    mysql --u root --p IndiaAlleleFinderDB < mysql-dump.sql
9. Generate your Catalyst model (maybe optional):

    $ script/brainbase_create.pl model DB DBIC::Schema IndiaAlleleFinderDB::Schema create=static \ components=TimeStamp,PassphraseColumn dbi:mysql:indiaallelefinderdb '[username]' '[password]' '{ AutoCommit => 1 }'

10. Open terminal and go to the /IndiaAlleleFinder folder & start the server:

    $ script/indiaallelefinder_server.pl -rp 3000

Or whatever port you might wish to run it on.

##Python Version (In Progress)
First, Install pip:
1. Follow these instructions: https://pip.pypa.io/en/latest/installing/
Download the following: https://bootstrap.pypa.io/get-pip.py
and run python get-pip.py

Next, Install Flask and and its Associated Packages
2. Now, pip install flask. http://flask.pocoo.org/docs/0.10/installation/#installation
*Make sure you have mysql56-server or its equivalent installed. for example on a mac this would be: sudo port install mysql56-server
3. sudo pip install MySQL-python
4. sudo pip install flask-mysqldb
5. sudo pip install flask-SQLAlchemy
Go to the directory where you've downloaded India Allele Finder, and Run It:
6. python main.py &

###Flask MySQL Database Configuration

mysql --u root --p IndiaAlleleFinderDB < mysql-dump.sql

then edit the corresponding line in main.py: 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/indiaAlleleFinderDB'

> Written with [StackEdit](https://stackedit.io/).

