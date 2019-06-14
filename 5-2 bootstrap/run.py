from my_app import app
from my_app import moment
from my_app import momentjs
from datetime import datetime



#set jinja template global


#print("Static folder: ", app.static_folder)

app.run(host = '0.0.0.0', debug = True)

timestamp = moment.create(datetime.utcnow()).calendar() 
#jinja_environ = app.create_jinja_environment()
app.jinja_env.globals['momentjs'] = momentjs
app.jinja_env.globals['timestamp'] = timestamp






