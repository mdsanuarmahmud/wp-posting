import base64
import requests



#Website information
user = 'Your User Name'  # the user in which the auth. token is given
website_url = 'https://example.com' #Your website url
wp_title = 'Your Post Tittle' # Your Post Title 
content = 'Post Body Text' # Your Post content here
slug = 'post-url' #Your Post URL
pythonapp = 'Authentication Token Genereted from Wp'  # paste here your auth. token

url = website_url +'/wp-json/wp/v2'  # the url of the wp access location
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8')) # we have to encode the usr and pw
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

post = {'title': wp_title,
        'slug': slug,
        'status': 'draft',
        'content': content,
        'categories':'1',
        'author': '1',
        'format': 'standard',
        }

r = requests.post(url + '/posts', headers=headers, json=post)
print( website_url +'/'+ slug + ' Has Been Posted')
