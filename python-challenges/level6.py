import pickle
import requests 

response = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")

file = "pickle.p"
with (open(file, "wb")) as openfile:
    openfile.write(response.content)
    
with (open(file, "rb")) as openfile:
    cont = pickle.load(openfile)

for parent_list in cont:
    for ele in parent_list:
        print(ele[0] * ele[1])
