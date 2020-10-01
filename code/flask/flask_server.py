from flask import Flask, render_template



#Define a porta do servidor
#app.run(host ='numero do host', port=porta)


#Cria o objeto flask
server = Flask(__name__)

@server.route('/')
def home():
    return render_template('main.html',titulo='Teste')


server.run(debug= True) 
