from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('index.html', my_string="Wheeeee!", my_list=[9,8,7,6,5,4,3,2,1,0])


#if __name__ == '__main__':
    #app.run(debug=True)
