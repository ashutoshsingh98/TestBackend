Technoloogies Used:
	We built this project with Python, Django and Django rest Framework.Here we used the djangos rest framework. 
	It provides an API view for displaying data,a response module for getting data. 
	 

About:
    1.This Project provides a Django Customized User Model Which creates a User and Super User with Some Permissions.
    2.We have two Models,Activity and M_users,First for User Creation And Another For creating user activities.
    3.We created two Custom Django management commands(create_users.py,create_activity.py), for populating the data inot tables M_user and Activity.
	4.create_users takes 5 aruments eid, real_name, tz, start_time and end_time and populate the data in both the tables as i linked the table
	  with forign key.
    5.while create activity is only for creating actvity for the existing real_name in the M_user table. it takes three argument real_name, star_time 
      and end_time. Make sure that real_name is an instance of M_user.	
	6.Model Activity is reffered to M_user model using the member_id which has Foriegnkey set to M_user Model.
	7.We created a MemberSerializer in our serializers.py which converts all data passed into Json format.
	8.At the same time ActivitySerilizer comes in action(nesting) which converts the activiy of that user in JSON.
	9.So in our views we had used restframework`s modules to get our data and Display it to the API.
	10.So, Finally after adding the required datas we can view them at localhost:8000/activity.
	11.If a user desires to view only his data he can go to localhost:8000/details/(his id)
	
    I created this project in a simple and much Readable way.Hope You will Like it.
	Thank you For giving me this apportunity.  
	
	
		
	    
	 	 	 						

	