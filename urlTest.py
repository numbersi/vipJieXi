import  requests


html = requests.get('http://api2.my230.com/?vid=27pan76467D748097AB78').content.decode()
print(html)