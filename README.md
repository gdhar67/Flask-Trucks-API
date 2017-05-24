# Flask-Trucks-API
## **A basic API - Truck booking for parcel service


### SERVER USED

- Flask (A Python Microframework)
- Version 0.12.2

-----------------------------------------------------------------------------------

### SERVER ROUTES

#### /guest/postregister
- A Post request.
- Used to create a user.
- Takes 5 parameters namely
	- username
	- name
	- email
	- password
	- type

-----------------------------------------------------------------------------------

#### /user/postlogin
- A Post request.
- Used to log In user.
- Takes 2 parameters namely
	- username
	- password

-----------------------------------------------------------------------------------

#### /user/logout
- A Get request.
- Used to log out user.

-----------------------------------------------------------------------------------

#### /user/ownerhomepage
- A Post request.
- Used to display booking request in "owner" homepage.
- Takes 1 parameter namely
	- id (user id)

-----------------------------------------------------------------------------------

##### /inputdata
- A Post request.
- Used to enter default truck details.
- Takes 4 parameters namely
	- Number of truck details you wish to enter
	- truck name
	- max weight
	- max volume

		- Input Post Request Format :
			- maxno : 2
			- data[0][truck_name] : xxxx
			- data[0][max_weight] : xxx
			- data[0][max_volume] : xxx
			- data[1][truck_name] : xxxx
			- data[1][max_weight] : xxx
			- data[1][max_volume] : xxx

-----------------------------------------------------------------------------------

##### /input/ownertrucks
- A Post request.
- Used to enter user(owner) truck details.
- Takes 6 parameters namely
	- Number of truck details you wish to enter
	- truck name
	- max weight
	- max volume
	- Number plate
	- Current city

		- Input Post Request Format :
			- maxno : 2
			- data[0][truck_name]   : xxxx
			- data[0][max_weight]   : xxx
			- data[0][max_volume]   : xxx
			- data[0][numberplate]  : xxx
			- data[0][current_city] : xxx
			- data[1][truck_name]   : xxxx
			- data[1][max_weight]   : xxx
			- data[1][max_volume]   : xxx
			- data[1][numberplate]  : xxx
			- data[1][current_city] : xxx

-----------------------------------------------------------------------------------

##### /customer/postbookingrequest
- A Post request.
- Used to enter a Booking Request by customer.
- Takes 14 parameters namely
	- user id
	- booking request id
	- source
	- destination
	- pickup date
	- pickup time
	- dropoff date
	- dropoff time
	- no of items
	- item name
	- item weight
	- item height
	- item length
	- item breadth

		- Input Post Request Format :
			- id           : xx (user id)
			- id1          : xx (booking request id)
			- source       : xxx
			- destination  : xxx
			- pickup_date  : yyyy-mm-dd
			- pickup_time  : hh-mm-ss
			- dropOff_date : yyyy-mm-dd
			- dropoff_time : hh-mm-ss
			- no_of_items  : 2 
			- item[0][name]    : xxxx
			- item[0][weight]  : xxx
			- item[0][height]  : xxx
			- item[0][length]  : xxx
			- item[0][breadth] : xxx
			- item[1][name]    : xxxx
			- item[1][weight]  : xxx
			- item[1][height]  : xxx
			- item[1][length]  : xxx
			- item[1][breadth] : xxx

-----------------------------------------------------------------------------------

##### /owner/postjourneyplan
- A Post request.
- Used to enter a Jurney plan by owner.
- Takes 10 parameters namely
	- user id
	- booking request id
	- user truck id (the truck which is going to be used)
	- source
	- destination
	- pickup date
	- pickup time
	- dropoff date
	- dropoff time
	- truck fare

		- Input Post Request Format :
			- id           : xx (user id)
			- id1          : xx (booking request id)
			- id2          : xx (user truck id)
			- space_alloc  : xx (Filled by owner - FULL/PARTIAL)
			- end_to_end   : xx (Filled by owner - YES/NO)
			- source       : xxx
			- destination  : xxx
			- pickup_date  : yyyy-mm-dd
			- pickup_time  : hh-mm-ss
			- dropOff_date : yyyy-mm-dd
			- dropoff_time : hh-mm-ss
			- truck_fare   : xxxxx

-----------------------------------------------------------------------------------
			
##### /customeracceptrequest
- A Post request.
- Used to accept a journey plan proposed by a owner.
- Takes 2 parameters namely
	- user id
	- journey plan id

		- Input Post Request Format :
			- id           : xx (user id)
			- id1          : xx (journey plan id)

-----------------------------------------------------------------------------------

##### /customerrejectrequest
- A Post request.
- Used to reject a journey plan proposed by a owner.
- Takes 2 parameters namely
	- user id
	- journey plan id

		- Input Post Request Format :
			- id           : xx (user id)
			- id1          : xx (journey plan id)

-----------------------------------------------------------------------------------

##### /customer/view/bookingRequest
- A Post request.
- Used to view booking request submitted by the user.
- Takes 2 parameters namely
	- user id

		- Input Post Request Format :
			- id           : xx (user id)

-----------------------------------------------------------------------------------

##### /customer/view/journeyplan
- A Post request.
- Used to reject a journey plan proposed by a owner.
- Takes 2 parameters namely
	- user id
	- Booking request id

		- Input Post Request Format :
			- id           : xx (user id)
			- id1          : xx (booking request id)

-----------------------------------------------------------------------------------

##### /owner/currentcity
- A Post request.
- Used to get the current of a truck by a owner.
- Takes 2 parameters namely
	- date
	- truck id

		- Input Post Request Format :
			- date         : yyyy-mm-dd (present date)
			- id           : xx (truck id)

-----------------------------------------------------------------------------------


### DATABASES/TABLES 


#### Database : truck
=================================================================================
##### Table : user
##### Fields
* id
* name
* username
* email
* password
* account_type



=================================================================================

##### Table : user_trucks
##### Fields
* id
* users_id
* truck_name
* max_weight
* max_volume
* number_plate
* percent_volume_left
* percent_weight_left
* current_city


=================================================================================

##### Table : truck_details
##### Fields
* id
* truck_name
* max_weight
* max_volume


=================================================================================

##### Table : booking_requests
##### Fields
* id
* users_id
* source
* destination
* no_of_items
* total_weight
* total_volume
* pickup_date
* pickup_time
* dropoff_date
* dropoff_time


=================================================================================

##### Table : items 
##### Fields
* id
* booking_request_id
* item_name
* weight
* height
* length
* breadth
* volume


=================================================================================

##### Table : journey_plans 
##### Fields
* id
* users_id
* booking_request_id
* truck_id
* space_allocation
* end_to_end
* source
* destination
* pickup_date
* pickup_time
* dropoff_date
* dropoff_time
* journey_fare
* status


-----------------------------------------------------------------------------------


### BUILD INSTRUCTIONS

* Clone the repository into a local folder in your computer.
* Use `git pull` to pull the code from Github.
* Go to the Flask-Truck-API Directory from console and use the command `pip install virtualenv` to set up your virtual environment.
* To activate the virtual environment use the command `venv\scripts\activate`.
* Install all the requirements using command `pip install --requirement` , read the requirements.txt.
* Create a database named `truck`.
* Launch the server using `python app.py`
* We are good to go.

			
-----------------------------------------------------------------------------------

#### Truck API . 