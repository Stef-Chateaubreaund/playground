from flask import Flask, render_template


app = Flask(__name__)


#@app.route('/')
#def index():
    #return "ola mundooo"

@app.route('/play')
def play():
    return render_template( "playground.html" )
    

#@app.route('/say/<name>')
#def say_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/play/<int:num>')
def play(num):
    return render_template("playground.html", num=num, color="pink")
    #output = ''

   # for i in range(0,num):
     #   output += f"<p>{word}</p>"

    #return output
@app.route('/play/<int:num>/<string:color>')#?
def last(num, color):
    return render_template("playground.html", num=num, color=color)

if __name__== "__main__":
    app.run(debug=True)
