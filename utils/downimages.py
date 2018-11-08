import json, requests

with open('../static/elementos/TablaPeriodica.json') as file:
  elem=json.load(file)

for elemento in elem:
   symbol=elem[elemento]['symbol']
   filename=symbol+'.gif'
   url="http://chemistry.bd.psu.edu/jircitano/"+filename
   
   response=requests.get(url)
   if response.status_code==200:
     with open (filename,'wb') as foto:
       foto.write(response.content)
   else:
    print ('Fallo con el :'+elemento+' : '+symbol)

