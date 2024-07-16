from flask import Flask, request  
app = Flask(__name__)  
  
@app.route('/chat', methods=['GET'])  
def chat():  
    message = request.args.get('message')  
    if message.lower() == "hello":  
        return "Hi"  
    elif message.lower() == "how are you":  
        return "I am fine"  
    else:  
        return "I didn't understand that"  
  
if __name__ == '__main__':  
    app.run(port=5000)  
