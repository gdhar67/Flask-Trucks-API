from flask import Flask, jsonify, request, url_for
from model import db, user, user_trucks, truck_details, booking_requests, journey_plans, items
from schemas import ma, user_schema, usertruck_schema , truck_detail_schema, booking_request_schema, items_schema, journey_plan_schema, booking_requests_schema, journey_plans_schema
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/truck'    # 'Name of database manager://username:password@host_name/database_name'
db.init_app(app)
ma.init_app(app)
# login_manager = LoginManager()
# login_manager.init_app(app)


# Decorators - API routes defined below


@app.route('/guest/postregister', methods=['POST'])
def postRegister():
	User, errors = user_schema.load(request.form)
	if errors:
	    resp = jsonify(errors)
	    resp.status_code = 400
	    return resp
	User.password         = sha256_crypt.hash(User.password)
	db.session.add(User)
	db.session.commit()

	#login_user(user)    <---- Commented for testing purpose  ---->
	resp = jsonify({"message": "Data entered successfully"})
	resp.status_code = 201
	return resp



@app.route('/user/postlogin', methods=['POST'])
def postLogin():
	username = request.form.get("username")
	password = request.form.get("password")
	if not username:
		resp = jsonify({"message": "Please enter your username"})
		resp.status_code = 400
		return resp

	if not password:
		resp = jsonify({"message": "Please enter your password"})
		resp.status_code = 400
		return resp

	User = user.query.filter(user.username==username).first_or_404()
	true = sha256_crypt.verify(password, User.password)
	if not true:
		resp = jsonify({"message": "Please your password"})
		resp.status_code = 400
		return resp

	#login_user(user)   <---- Commented for testing purpose  ---->
	
	if User.account_type=='Owner':
		resp = jsonify({"message": "Successfully logged into Owner page"})
		resp.status_code = 201
		return resp

	resp = jsonify({"message": "Successfully logged into Customer page"})
	resp.status_code = 201
	return resp



@app.route('/user/logout')
#@login_required    <---- Commented for testing purpose  ---->
def logout():
    #logout_user()    <---- Commented for testing purpose  ---->
    return 'You are now logged out!'



@app.route('/user/owner/homepage', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def getOwnerHomepage():
	id = request.form.get("id")
	User = user.query.filter(user.id==id).first_or_404()
	if not User.account_type=='Owner':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp

	Booking_requests = booking_requests.query.filter().get()
	if not Booking_requests:
		resp = jsonify({"message": "No booking request found"})
		resp.status_code = 404
		return resp

	resp = jsonify({"message": Booking_requests })
	resp.status_code = 201
	return resp




@app.route('/api/inputdata', methods=['POST'])
def postInputData():
	i=0
	maxno=request.form.get("maxno")

	for i in range(int (maxno)):
		data={
		 'truck_name': request.form.get("data[%d][name]" % i),
		 'max_weight': request.form.get("data[%d][weight]" % i),
		 'max_volume':request.form.get("data[%d][volume]" % i)
		 }
		Truck_details, errors = truck_detail_schema.load(data)
		if errors:
		    resp = jsonify(errors)
		    resp.status_code = 400
		    return resp
		db.session.add(Truck_details)
		db.session.commit()
	resp = jsonify({"message": "Data successfully submitted"})
	resp.status_code = 201
	return resp




@app.route('/input/ownertrucks', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postInputOwnerTrucks():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Owner':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	i=0
	maxno=request.form.get("maxno")
	for i in range(int (maxno)):
		data={
		 'number_plate':request.form.get("data[%d][number_plate]" % i),
		 'current_city':request.form.get("data[%d][current_city]" % i),
		 'truck_name': request.form.get("data[%d][name]" % i),
		 'max_weight': request.form.get("data[%d][weight]" % i),
		 'max_volume':request.form.get("data[%d][volume]" % i)
		 }
		User_trucks, errors = usertruck_schema.load(data)
		if errors:
		    resp = jsonify(errors)
		    resp.status_code = 400
		    return resp
		User_trucks.users_id=id1
		db.session.add(User_trucks)
		db.session.commit()

	resp = jsonify({"message": "Data added successfully!"})
	resp.status_code = 201
	return resp




@app.route('/customer/postbookingrequest', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postBookingRequest():
	id1 = request.form.get("id1")
	id2 = request.form.get("id2")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Customer':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Booking_request, errors = booking_request_schema.load(request.form)
	if errors:
	    resp = jsonify(errors)
	    resp.status_code = 400
	    return resp
	id1 = request.form.get("id1")
	Booking_request.users_id=id1
	db.session.add(Booking_request)
	db.session.commit()

	i=0
	height = 0
	length = 0
	breadth = 0
	no_of_items=request.form.get("no_of_items")
	for i in range(int (no_of_items)):
		height = int (request.form.get("item[%d][height]" % i))
		breadth = int (request.form.get("item[%d][breadth]" % i))
		length = int (request.form.get("item[%d][length]" % i))
		volume = height * length * breadth
		data={
		 'item_name': request.form.get("item[%d][name]" % i),
		 'weight': request.form.get("item[%d][weight]" % i),
		 'height': request.form.get("item[%d][height]" % i),
		 'breadth': request.form.get("item[%d][breadth]" % i),
		 'length': request.form.get("item[%d][length]" % i),
		 'volume': volume
		 }
		Items, errors = items_schema.load(data)
		if errors:
		    resp = jsonify(errors)
		    resp.status_code = 400
		    return resp
		Items.users_id=id1
		Items.booking_request_id=id2
		db.session.add(Items)
		db.session.commit()
	
	weight = 0
	volume =0
	Items = items.query.filter(items.booking_request_id==id2).all()
	for item in Items:
		weight += item.weight
		volume += item.volume

	Booking_requests = booking_requests.query.filter(booking_requests.id==id2).first_or_404()
	Booking_requests.total_weight = weight
	Booking_requests.total_volume = volume
	Booking_requests, errors = booking_request_schema.load(request.form, instance=Booking_requests)
	if errors:
	    resp = jsonify(errors)
	    resp.status_code = 400
	    return resp
	db.session.add(Booking_requests)
	db.session.commit()

	resp = jsonify({"message": "Data added successfully!"})
	resp.status_code = 201
	return resp




@app.route('/owner/postjourneyplan', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postJourneyPlan():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Owner':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Journey_plan, errors = journey_plan_schema.load(request.form)
	if errors:
	    resp = jsonify(errors)
	    resp.status_code = 400
	    return resp
	id2 = request.form.get("id2")
	id3 = request.form.get("id3")
	Journey_plan.users_id=id1
	Journey_plan.booking_requests_id=id2
	Journey_plan.truck_id=id3
	db.session.add(Journey_plan)
	db.session.commit()

	resp = jsonify({"message": "Data added successfully!"})
	resp.status_code = 201
	return resp




@app.route('/customer/acceptrequest', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postCustomerAcceptRequest():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Customer':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Journey_plan = journey_plans.query.filter(journey_plans.id==id1).first_or_404()
	Journey_plan.status='Accepted'
	db.session.commit()
	resp = jsonify({"message": "Data added successfully!"})
	resp.status_code = 201
	return resp




@app.route('/customer/rejectrequest', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postCustomerRejectRequest():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Customer':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Journey_plan = journey_plans.query.filter(journey_plans.id==id1).first_or_404()
	Journey_plan.status='Rejected'
	db.session.commit()
	resp = jsonify({"message": "Data added successfully!"})
	resp.status_code = 201
	return resp





@app.route('/customer/view/bookingrequest', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postViewBookingRequest():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Customer':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Booking_requests = booking_requests.query.filter(booking_requests.users_id==id1).all()
	return booking_requests_schema.jsonify(Booking_requests)





@app.route('/customer/view/journeyplan', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postViewJourneyPlan():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Customer':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	Journey_plan = journey_plans.query.filter(journey_plans.booking_requests_id==id1).all()
	return journey_plans_schema.jsonify(Journey_plan)




@app.route('/owner/currentcity', methods=['POST'])
#@login_required    <---- Commented for testing purpose  ---->
def postCurrentCity():
	id1 = request.form.get("id1")
	User = user.query.filter(user.id==id1).first_or_404()
	if not User.account_type=='Owner':
		resp = jsonify({"message": "Access denied"})
		resp.status_code = 401
		return resp
	date = request.form.get("date")
	Journey_plan = journey_plans.query.filter(journey_plans.status=='Accepted').all()

	for jp in Journey_plan:
		if jp.pickup_date==date:
			User_trucks = user_trucks.query.filter(user_trucks.current_city==jp.truck_id).first_or_404()
			User_trucks.current_city=jp.source
			db.session.commit()
			place=jp.source
			return jsonify(place)
		elif jp.dropoff_date==date:
			User_trucks = user_trucks.query.filter(user_trucks.current_city==jp.truck_id).first_or_404()
			user_trucks.current_city=jp.destinataion
			db.session.commit()			
			place=jp.destinataion
			return jsonify(place)

	User_trucks = user_trucks.query.filter(user_trucks.current_city==id1).first_or_404()
	place = User_trucks.current_city
	return jsonify(place)





@app.errorhandler(404)
def page_not_found(error):
    resp = jsonify({"error": "not found"})
    resp.status_code = 404
    return resp


if __name__ == "__main__":
  app.run(debug = True)