#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import jinja2

# For Google App Engine DataStore Methods
from google.appengine.ext import db

# Store template directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# Set up Jinja Environment
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
                               autoescape = True);

# Helper functions
class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
  
  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))

class Post(db.Model):
  # required = True => makes field required
  # Title Field
  title = db.StringProperty(required = True)
  # Body Field (Text because it can be very long)
  body = db.TextProperty(required = True)
  # Created Field - Holds date/time when created
  # auto_now_add = True => value will be set when instance is created
  created = db.DateTimeProperty(auto_now_add = True)
  # Post_ID Field (Number) holds key/id for each post
  # post_id = db.IntegerProperty()
    
class MainPage(Handler):
    def render_front(self, title="", body="", error=""):
      """ Function to Render Front Page """
      # Modify Query to only render 10 posts
      posts = db.GqlQuery("SELECT * FROM Post "
                          "ORDER BY created DESC")
      # render page using template
      # self.render()
    
    def get(self):
        self.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
