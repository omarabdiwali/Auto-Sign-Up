# Auto-Sign-Up
A Python script that uses Selenium to automate the sign up of my CS class when available.
This program runs every 20 mins, and uses a schedule provided by the school to look at the number of available seats.
It checks between 3 classes that also include labs to have available seats, and takes the course numbers.
If available, it uses Selenium to sign in to the university account, and removes me from the conflicting classes, and signs me up for the current one.
