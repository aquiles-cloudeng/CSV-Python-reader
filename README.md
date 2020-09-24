# CSV-Python-reader
 This is a Simple Python project I created to read a CSV, I made it to automate a task but I think is cool for anybody that needs it.

It's a lambda function so you have to deploy it in AWS, it reads a bucket and when an object is uplodad it triggers the function. It scans de CSV and sends an API request to post the information (in my case I needed to get a key previously).