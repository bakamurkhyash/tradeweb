import requests
def send_request(data, webhook_url:str, timeout:int):
    import requests
    resp = requests.post("webhook_url",
                             json = data,
                             headers = {"Content-type": "application/json"},
                              timeout = 10)
    resp.raise_for_status()
    responses = resp.json()
    try: 
        return {"status": resp.status_code, "json": resp.json(), "text": resp.text}
            #in above line the 'resp.json()' contains the response from the 'respond to webhook' node
    except ValueError:
        return {"status": resp.status_code, "json": None, "text": resp.text}