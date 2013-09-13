import os
import urllib
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('hello2.html')
		self.response.write(template.render())

class EventOp(webapp2.RequestHandler):
	def create(eventObj):
		

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
