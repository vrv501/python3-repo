import requests

start_code = "12345"
stop_code_1 = "16044"
ans = ""
while True:
    response = requests.get(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={start_code}", timeout=60, allow_redirects=True)
    content = response.content.decode().split()
    for num in content:
        if num.isnumeric():
            start_code = num 
        if num.__contains__("html"):
            ans = num
            break
    
    if ans != "":
        break

    if start_code == stop_code_1:
        start_code = int(start_code) // 2

print(ans)
    