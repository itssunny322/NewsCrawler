# NewsCrawler

It's a very basic new crawler application ,where the script will crawl through
the news website times of india everyday at morning 9am, and store the headline
the date of headline and other info in our database , whenever you want you can 
retrive the headline , used cronjobs for job scheduler as well.

Here is how to run the code:
<br>
1.Create directory named assesment using command:   mkdir assigment 
<br>
2.Navigate to the directory using the command : cd assigment
<br>
3.Clone the project using command : git clone https://github.com/itssunny322/NewsCrawler.git
<br>
4.Navigate to the directory where requrements.txt
<br>
5.Create virtual environment using the command:
    ->  python3 -m venv env
<br>
6.Activate virtual environment using the command :
    -> source env/bin/activate
<br>
7.Create database using the command :
    -> mysql -u root -p 
    -> enter password
    -> create database newsdb;
<br>
8.Navigate to the directory where manage.py is present

<br>
9. add task schedular to crawl after every 24 hour using the command 
    -> python manage.py crontab add

<br>
10.Run the server using the command:
    -> python manage.py runserver
