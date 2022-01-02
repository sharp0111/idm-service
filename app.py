from flask import Flask, request

from api.route import VendorService

app = Flask(__name__)

vendorService = VendorService()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/search", methods=["GET"])
def search():
    return vendorService.search(request.args)
