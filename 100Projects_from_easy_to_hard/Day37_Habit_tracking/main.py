import requests, datetime

username = "username"
token = "token"
pixela_endpoint = "https://pixe.la/v1/users"
pixela_graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_id = "walk"
post_graph_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
headers = {
    "X-USER-TOKEN":token
}
graph_name = "walking graph"


# ------- creating account -------#

# parameters = {
#     "token":token,
#     "username":username,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response)

# ------- making a graph -------#

# graph_config = {
#     "id": "walk",
#     "name":"walking graph",
#     "unit": "km",
#     "type":"float",
#     "color":"shibafu"
# }



# x=requests.post(url=pixela_graph_endpoint, json=graph_config,headers= headers)
# print(x.text)


# -------- adding to the graph ---------#

# distance = input("Enter the distance you walked today : ")
# walk_paremeters = {
#     "date":str(datetime.datetime.now().date().strftime('%Y%m%d')),
#     "quantity": distance
# }
# response = requests.post(url=post_graph_endpoint, json=walk_paremeters, headers=headers)
# print(response.text)

# --------- wpdating graph -------------#

# put_parameters = {
#     "name":graph_name,
#     "unit":"km"
# }
# response = requests.put(url=post_graph_endpoint, json=put_parameters, headers=headers)
# print(response.text)


# ------------ updating pixels -------------#

# pixelupdate_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{str(datetime.datetime.now().date().strftime('%Y%m%d'))}"
# pixel_param = {
#     "quantity":"4"
# }

# response = requests.put(url=pixelupdate_endpoint, json=pixel_param, headers=headers)
# print(response.text)

#  --------- delete pixel ------------#

# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{str(datetime.datetime.now().date().strftime('%Y%m%d'))}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)