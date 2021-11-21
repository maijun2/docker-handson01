import os, flask, datetime, ssl
from flask import Flask, jsonify, request

PORT = int(os.environ['PORT'])
app = flask.Flask('app server')

@app.route('/')
def index():
    return success([{'id':1,"title":"first"},{'id':2,"title":"second"},{'id':3,"title":"Third"}])
    
@app.route('/datetime')
def gettime():
    date = datetime.datetime.now()
    value = date.strftime("%Y/%m/%d %H:%M:%S")
    return success({'date':value})    

def success(d):
    return(jsonify(d),200)


@app.errorhandler(404)
def api_not_found_error(error):
    return(jsonify({'error':"Not Found",'code':404}),404)
    
@app.errorhandler(405)
def method_not_allowed_error(error):
    return(jsonify({'error':"Not Allowed",'code':405}),405) 
    
@app.errorhandler(500)
def internal_server_error(error):
    return(jsonify({'error':"Server Error",'code':500}),500)     
    

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.crt', 'server_secret.key','password')

app.run(debug=True, host='0.0.0.0',port=PORT,ssl_context=context)