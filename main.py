from flask import Flask,redirect
app = Flask('app')

@app.route('/')
def hello_world():
  return redirect('https://www.google.com/')
  

app.run(host='0.0.0.0', port=8080)