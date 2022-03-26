import base64
import requests


#Authenticate to Web
user = 'Your User Name'  # the user in which the auth. token is given
pythonapp = 'Authentication Token Genereted from Wp'  # paste here your auth. token
url = 'https://Your Sitename./wp-json/wp/v2'  # the url of the wp access location
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))  # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}


    post = {'title': 'Wordpress Title ',
           'slug': 'slug',
           'status': 'draft',
           'content':'This is my content',
           'categories':'1',
           'author': '1',
           'format': 'standard',
           }


r = requests.post(url + '/posts', headers=headers, json=post)
