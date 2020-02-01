import requests

def client():
    token_h = "Token 9d300531367ad8e5faf5fb5b77165b4c0fa95010"
    # credentials = {"username":"admin","password":"admin"}
    
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/",
    #                          data = credentials)
    
    headers = {"Authorization" : token_h}
    
    response = requests.get("http://127.0.0.1:8000/api/profiles/" , 
                            headers=headers)
    
    print("status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()
    