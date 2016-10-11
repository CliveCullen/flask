from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def getindex():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(
        port=8000
    )

teams = [{
    'name':'The All Blacks',
    'rank':'first'},
    {
    'name':"England",
    'rank':'Second'},

    {
    'name':"Australia",
    'rank':'Third'},
    {
    'name':"South Africa",
    'rank':'Fourth'},
    {
    'name':"wales",
    'rank':'Fifith'},
    {
    'name':"Ireland",
    'rank':'Sixth'},
    {
    'name':"Scotland",
    'rank':'Seventh'},
    {
    'name':"Argentina",
    'rank':'Eight'},
    {
    'name':"France",
    'rank':'Ninth'},
    {
    'name':"Georgia",
    'rank':'Tenth'}]

@app.route('/teams')
def list_teams():
    return render_template('index.html',data=teams )