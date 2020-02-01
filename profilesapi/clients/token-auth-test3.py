import requests

def client():
    token_h = "Token 07a6d46506fe0e153921fd17fcfd109a7b3b4138"
    # data = {"username":"puttipong",
    #                "password1":"puttipong1#",
    #                "password2":"puttipong1#",
    #                "email":"test@rest.com"}
    
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                          data = data)
    
    headers = {"Authorization" : token_h}
    
    response = requests.get("http://127.0.0.1:8000/api/profiles/" , 
                            headers=headers)
    
    print("status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    client()
    