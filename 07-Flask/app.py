from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route("/postone",methods=['GET','POST'])
def postOne():
    if(request.method=='POST'):
        # print(request['name'])
        return render_template("Post.html")

    return render_template("get.html")



if __name__ == '__main__':
    app.run(debug=True)