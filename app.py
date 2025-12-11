from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello dari aplikasi sederhana PaaS di Render!"

if __name__ == "__main__":
    app.run()
