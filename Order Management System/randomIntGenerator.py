import urllib.request
import time
import json
import random

while True:
    rnd = random.randint(1, 100)
    print(int(rnd))

    data ={"value":int(rnd)}
    json_data = json.dumps(data).encode("utf-8")

    request = urllib.request.Request("http://localhost:8081/randomInt")
    request.add_header("Content-Type","application/json")

    urllib.request.urlopen(request,json_data).read()

    time.sleep(0.5)