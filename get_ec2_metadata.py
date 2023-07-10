# Please run this script on any EC2 instance for result
import requests

#IPv4 instance metadata service address: 169.254.169.254

url = "https://169.254.169.254/latest/meta-data"

r = requests.get('url')

print (r.json())

ec2_metadata_object = input('Please enter any metadata from above output you want a value of  ')


new_url = "http://169.254.169.254/latest/meta-data/%s" % ec2_metadata_object
response = requests.get('new_url')

print (response.json())

#I have not done the error handling in this script.
#please use the best case for the output



