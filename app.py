from flask import Flask

from datadog import initialize, statsd
import time
import random

app = Flask(__name__)

@app.route('/')
def bubble_tea():
	#send some dogstatsd metrics 
	options = {
    	'statsd_host':'127.0.0.1',
    	'statsd_port':8125
	}
	initialize(**options)
  
	topping = ["pearl","pudding","grass_jelly","coconut_jelly","aloe_vera","red_bean","sago","rainbow_jelly","lychee_jelly","cheese_foam"]
	drink_type = ["milk_tea","fresh_tea","fruit_tea","yogurt","smoothie"]
	ice_level = ["full","half_ice","no_ice"]
	sugar_level = ["full","half_sugar","less_sugar","no_sugar"]

	get_topping = random.choice(topping)
	get_drink_type = random.choice(drink_type)
	get_ice_level = random.choice(ice_level)
	get_sugar_level = random.choice(sugar_level)

	statsd.increment("bubble_tea.count", tags=["submission_method:dogstatsd","submission_from:heroku","topping:"+get_topping,"drink_type:"+get_drink_type])
	statsd.gauge("bubble_tea.gauge", random.randint(100, 999), tags=["submission:dogstatsd","submission_from:heroku","topping:"+get_topping,"drink_type:"+get_drink_type])
	statsd.histogram('bubble_tea.histogram', random.randint(10, 99),tags=["submission:dogstatsd","submission_from:heroku","topping:"+get_topping,"drink_type:"+get_drink_type])
	statsd.distribution('bubble_tea.distribution', random.randint(1, 9),tags=["submission:dogstatsd","submission_from:heroku","topping:"+get_topping,"drink_type:"+get_drink_type])
	return "hello world"
    
if __name__ == '__main__':
  app.run()
