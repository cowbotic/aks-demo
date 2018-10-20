from flask import Flask, render_template, url_for, request
import os, socket, sys, random, time, math, functools, requests, jsonify

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

app = Flask(__name__)

@app.route('/')
def hello():
  params={}
  #params['ip']=request.remote_addr
  params['ip']='47.60.32.181'
  
  datos_ip=requests.get('http://ip-api.com/json/'+params['ip'])
  
  if len(set(['country','region','isp']).intersection(datos_ip.json().keys())) == 3:
  #if 'country' in datos_ip.json().keys() and 'region' in datos_ip.json().keys() and 'isp' in datos_ip.json().keys():
    params['country']=datos_ip.json()['country']
    params['region']=datos_ip.json()['regionName']
    params['isp']=datos_ip.json()['isp']

  else:
    params['country']='desconocido'
    params['region']='desconocido'
    params['isp']='desconocido'

  params['cont_ip']=get_ip_address()
  params['pub_cont_ip']=requests.get('http://ident.me').text
  params['hostname']=socket.gethostname()
  return render_template('hello.html', params=params)


if __name__ == '__main__':
  app.run()


