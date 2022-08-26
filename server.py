from flask import Flask, render_template 
app = Flask(__name__)

#routes to my landing page
@app.route('/')
def home():
    return render_template("hello.html")

#routes to /play with an autofilled value of /3/blue
@app.route('/play')
def play():
    return render_template("index.html",num=3,color="blue")

#routes to /play/ user assigned box count with an autofilled color value of blue
@app.route('/play/<int:num>')
def add_int(num):
    return render_template("index.html", num=num, color="blue") 

#routes to /play/ user assigned box count / user assigned box color
@app.route('/play/<int:num>/<string:color>')
def add_color(num,color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
