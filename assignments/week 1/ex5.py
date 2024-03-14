web_address = input("enter the web address\n")
if web_address[len(web_address)-1] and ("http://" or "https://") in web_address == "/":
    pass
else:
    ask = input("do you have SSL [y/n]\n")
    if ask.lower() == "y":
        web_address =  "https://"+web_address
    elif ask.lower() == "n":
        web_address =  "http://"+web_address
    else:
        print("Wrong Input")
    web_address += "/"

print(web_address)
topic_name = input("Enter the topic name\n")
topic_name = topic_name.lower()
topic_name=topic_name.replace(" ", "-") #replace a substring
url = web_address+topic_name 
print(url)        
