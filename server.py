from flask import Flask,request 

app = Flask (__name__)

@app.route('/',methods =['POST','GET'])
def server():
    data = request.get_data(as_text=True)
    print(data)
    return "Hello from local server"



if __name__ == '__main__': 
    app.run(host="0.0.0.0",port=5000)
