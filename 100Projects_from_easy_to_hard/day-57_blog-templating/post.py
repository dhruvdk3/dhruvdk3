import requests
class Post:
    def __init__(self, id) -> None:
        self.id = id
        self.x = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
    
    def get(self):
        for i in self.x:
            print(i)
            if i[ "id"] == int(self.id):
                return i

