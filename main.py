from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route GET
@app.route("/get")
def hello_get():
    return "Hello, orang cantik (GET)"

# Route POST
@app.route("/post")
def hello_post():
    return "Hello, orang cantik (POST)"

# Route DELETE
@app.route("/delete")
def hello_delete():
    return "Hello, orang cantik (DELETE)"

# Route dengan parameter dinamis
@app.route("/detail/<nama>")
def hello_detail(nama):
    return f"Halo {nama}, ini halaman detail kamu!"

# Jalankan server Flask
if __name__ == "__main__":
    app.run(debug=True)
