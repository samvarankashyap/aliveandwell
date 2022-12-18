from flask import Flask
from flask import Flask, request, jsonify
from datetime import datetime
import requests
import os
PATH = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__,static_url_path='/static')


@app.route('/')
def index():
    hello_string = "<h1> Are you alive and well ? if so click and confirm <br><h1>"
    form = """

<html>
<head>
<style>
.button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>
</head>
<body>

    <h2>
    <a href="/lookwhoisalive?fname=Pasoonamba" class="button">
        Passonamba Click here
    </a>
    </h2>
    <h2>
    <a href="/lookwhoisalive?fname=Aarna" class="button">
        Aarna Click here
    </a>
    </h2>
    <h2>
    <a href="/lookwhoisalive?fname=Budugu" class="button">
        Budugu Click here
    </a>
    </h2>
    <h2>
    <a href="/lookwhoisalive?fname=Eskay" class="button">
        Eskay Click here
    </a>
    </h2>

    <h2>
    Someone else ?
    <form action='/lookwhoisalive'>
      <label for="fname">Name:</label><br>
      <input type="text" id="fname" name="fname"><br>
      <input type="submit">
    </form>
    </h2>

</body>
</html>

    """
    return hello_string + form

@app.route('/lookwhoisalive', methods=['GET'])
def lookwhoisalive(methods=['GET']):
    now = datetime.now()
    print("now =", now)
    # dd/mm/YY H:M:S
    filemode = "a"
    filename = "usertexts.txt"
    file_size = os.path.getsize(PATH+"/"+filename)
    print("File Size is :", file_size, "bytes")
    if int(file_size) > 10240:
        filemode = "w"
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    fd = open(filename, filemode)
    fd.write(request.args["fname"]+ " alive and well at "+dt_string+"\n")
    fd.close()

    fd = open(filename, "r")
    userlists = fd.read()
    fd.close()
    form = """
    This is the alive page <br>
    """
    form= form+userlists.replace("\n", "<br>")
    return form

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
