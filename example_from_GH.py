import json
import webbrowser
from credentials import Credentials
from shapeways.client import Client

client = Client(
    consumer_key=Credentials["Consumer_Key"],
    consumer_secret=Credentials["Consumer_Secret"],
    callback_url="http://localhost:3000/callback"
)

def application(environ, start_response):
    url = environ["PATH_INFO"]
    if url.startswith("/favicon.ico"):
        start_response("204 No Content", [])
        return [""]
    elif url.startswith("/login"):
        url = client.connect()
        start_response("302 Found", [
            ("Location", str(url)),
        ])
        return [""]
    elif url.startswith("/callback"):
        client.verify_url(environ["QUERY_STRING"])
        start_response("302 Found", [
            ("Location", "http://localhost:3000/"),
        ])

        return [""]
    else:
        #this is where steps after verification goes
        response = client.get_api_info()
        start_response("200 Ok", [
            ("Content-Type", "application/json"),
        ])
        return [json.dumps(response)]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    try:
        httpd = make_server("", 3000, application)
        print "Tracking Server Listening on Port 3000..."
        url=client.connect()
        webbrowser.open(url,new=2)

        httpd.serve_forever()
    except KeyboardInterrupt:
        print "Exiting..."
