# Remove hard coded constants (for intersection number)
# TODO implement your own deque
# Keep in mind our program is working in such a way that only the mid streets are calculated not the beging one's and not the ending one's calculated till now
from collections import deque


class Car():
	# start = ''
	# destination = ''
	score = 0 # score for car
	name = ''
	street_counter = 1 # make sure this to change this to 1 if you want to skip initial city
	pos = 0
	 # streets a car wants to pass
	travel_time = 0

	def __init__(self, street_to_travel, name):

		self.name = name
		# self.start = street_to_travel[0]
		# self.pos = street_to_travel[0].time-1
		self.current_street = street_to_travel[0]
		self.streets = street_to_travel

		if self.current_street.traffic_light:
			# self.current_street.weight_q.append(self)
			pass

	# def startDrive(self):
	# 	for s in self.streets:
	# 		self.travel_time +=s.time
	# 	print("car travelled and takes time:", self.travel_time)

	
	# for normal condition 
	def startDrive(self):
		
		# print(self.streets[-1:][0].name)
		if(self.current_street ==self.streets[-1:][0] and self.pos == 0):# and self.current_street.time-1 == self.pos): # comparing b/w objects
			# print(self)
			# print("wohoo", self.current_street.name)
			self.travelTime()
			return 
		else:
			self.travel_time +=1
		
		if(self.pos == 0):
			if(self.current_street.traffic_light): # check if street have light
				if(self.current_street.traffic_light.color):
					print("light green hai")
					# Cars get Queued when reached to 0th pos and when light is red
					self.current_street.weight_q.append(self)
					self.current_street = self.streets[self.street_counter]
					self.street_counter+=1
					self.pos = self.current_street.time-1
				else:
					if not self in self.current_street.traffic_q:
						self.current_street.traffic_q.append(self)
					pass
			else:
				self.current_street = self.streets[self.street_counter]
				# self.current_street.weight_q.append(self)
				self.street_counter+=1	
				self.pos = self.current_street.time-1
				
		else:
			# current_street.traffic_q.append(self)
			self.pos-=1

	def travelTime(self):
		print(f"{self.name} travelled and takes time:{ self.travel_time-1}")


class TrafficLight():
	color = False
	time = 3 # constant for now
	
	def __init__(self):
		self.curr_iter = 0

	def changeColor(self):
		self.curr_iter +=1
		if(self.curr_iter%self.time==0):
			if self.color:
				self.color = False
			else:
				self.color = True
		

class Intersection():
	intersection_number =0
	incoming_streets = []
	
	def updateLights(self):
		for i in incoming_streets:
			i.traffic_light.time +=1

	# outgoing_streets = []

class Street():
	def __init__(self, b, e, name, time):
		self.beginig = b
		self.ending = e
		self.name = name
		self.time = time
		self.traffic_light = 0
		self.traffic_q = []
		self.weight_q = []

		self.t_queue_pop_lock = False

	def associateLight(self, time):
		pass


# Functions
def cityBuilder(b, e, name, l):
	s = Street(b,e,name, l)
	city.append(s)


def traficLightBuilder(city):
	count_b = []
	count_e = []
	count = 0

	dick = {}
	for index, i in enumerate(city):
		for indexj, j in enumerate(city):
			if i.ending == j.ending and index !=indexj:
				if i.name in dick:
					print("if main aya")
					dick[i.name]+=1
				else:
					t_light = TrafficLight()
					t_light.time = 1
					i.traffic_light = t_light
					intersection = Intersection()
					intersection.intersection_number =1 
					intersection.incoming_streets.append(i)
					dick[i.name] = 1

	print(dick)
	print(intersection.incoming_streets)
	return city ,dick



# Driver code
if __name__ == "__main__":
	city = []

	# first line generic inputs==========================
	ip_arr = [int(x) for x in input().split(" ")]

	# mapping inputs
	d = ip_arr[0]
	i = ip_arr[1]
	s = ip_arr[2]
	v = ip_arr[3]
	f = ip_arr[4]


	# S line inputs=======================================
	for i in range(0, s):
		s_inputs = [x for x in input().split(" ")]
		b = int(s_inputs[0])
		e = int(s_inputs[1])
		street_name = str(s_inputs[2])
		l = int(s_inputs[3])
		cityBuilder(b, e, street_name, l)

	city, dick = traficLightBuilder(city)


	# ------------------------------------------------------
	# Inputs for street to travel for car===================
	ip = input().split(" ")
	ip2 = input().split(" ")
	ip3 = input().split(" ")

	street_to_travel = []
	street_to_travel2 = []
	street_to_travel3 = []

	for i in ip:
		for j in city:
			if i == j.name:
				street_to_travel.append(j)
	
	for i in ip2:
		for j in city:
			if i == j.name:
				street_to_travel2.append(j)

	for i in ip3:
		for j in city:
			if i == j.name:
				street_to_travel3.append(j)

	# for i in street_to_travel:
	# 	print(i.name, i.time)

	for i in street_to_travel3:
		print(i.name, i.time)


	# -------------------------------------------------------
	# Let's drive the car and simulation=====================
	ferrari = Car(street_to_travel, 'ferrari')
	dodge = Car(street_to_travel2, 'dodge')
	phantom = Car(street_to_travel3, 'phantom')
	I = Intersection()
	time = 0

	while(time <9):
		# I.updateLights()
		ferrari.startDrive()
		dodge.startDrive()
		phantom.startDrive()

		# for i in city:
		# 	if i.traffic_light:
		# 		i.traffic_light.changeColor()
		time+=1

	ferrari.travelTime()
	dodge.travelTime()
	phantom.travelTime()

	print('..........')

	for i in city[1].traffic_q:
		print(i.name)


	# print(city[2].weight_q)
	# Initial Queue for placing cars in right position
	# checking cars having same starting point 
	# 2 cars and 4, 3 streets
	# deque([ferrari, dodge, phantom])

# SAMPLE INPUTS
'''
6 4 5 2 1000
2 0 rue-de-londres 1
0 1 rue-d-amsterdam 1
3 1 rue-d-athenes 1
2 3 rue-de-rome 2
1 2 rue-de-moscou 3
4 rue-de-londres rue-d-amsterdam rue-de-moscou rue-de-rome
3 rue-d-athenes rue-de-moscou rue-de-londres
3 rue-de-londres rue-d-amsterdam rue-de-moscou rue-d-athenes rue-de-rome 
'''

# Initial queue for cars
# Traffic signal queue


# !!!!!!!!!!!!!!!!!!!!!!!!!testing stuff here beware!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# let's work on function for taking inputs
# def carInput(n): # n is number of cars used in sim.
# 	car_objs = []
# 	for i in range(0,n):
# 		ip = input().split(" ")
# 		street_to_travel = []

# 		for i in ip:
# 		for j in city:
# 			if i == j.name:
# 				street_to_travel.append(j)

# 		# making list of cars objects
# 		car_objs.append(Car(street_to_travel, 'tes'))

# 		for i in street_to_travel3:
# 		print(i.name, i.time)

# 	ip2 = input().split(" ")
# 	ip3 = input().split(" ")

	
# 	street_to_travel2 = []
# 	street_to_travel3 = []

	
	
# 	for i in ip2:
# 		for j in city:
# 			if i == j.name:
# 				street_to_travel2.append(j)

# 	for i in ip3:
# 		for j in city:
# 			if i == j.name:
# 				street_to_travel3.append(j)

# 	# for i in street_to_travel:
# 	# 	print(i.name, i.time)

# 	for i in street_to_travel3:
# 		print(i.name, i.time)

