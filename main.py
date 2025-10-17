from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    """Main page"""
    return render_template("main.html")


@app.route("/history")
def history_page():
    return render_template("history.html")


@app.route("/memory")
def memory():
    return render_template("memory.html")

if __name__ == "__main__":
    app.run(debug=True)
