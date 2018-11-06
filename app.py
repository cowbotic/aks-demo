from flask import Flask, render_template, url_for, request
import os, socket, sys, random, time, math, functools, requests, jsonify, json

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

app = Flask(__name__)

@app.route('/')
def hello():
  params={}
  params['ip']=request.remote_addr
  
  datos_ip=requests.get('http://ip-api.com/json/'+params['ip'])
  
  if len(set(['country','region','isp']).intersection(datos_ip.json().keys())) == 3:
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

@app.route('/datos')
def datos():
  resp=app.make_response('{"Hostname": "'+socket.gethostname()+'"}')
  return resp

@app.route('/tetraedro')
def tetraedro():
  return render_template('tetraedro.html')

@app.route('/particulas')
def particulas():
  return render_template('particulas.html')

@app.route('/particularandom')
def particularandom():
  particulas={"BosonW+":{"nombre":"BosonW+","masa":"80.39 GeV/c^2","carga":"1","spin":"1","tipo":"Bosones","descubierto":"1983 @CERN"},
"BosonW-":{"nombre":"BosonW-","masa":"80.39 GeV/c^2","carga":"-1","spin":"1","tipo":"Bosones","descubierto":"1983 @CERN"},
"BosonZ0":{"nombre":"BosonZ0","masa":"91.19 GeV/c^2","carga":"0","spin":"1","tipo":"Bosones","descubierto":"1983 @CERN"},
"Electron":{"nombre":"Electron","masa":"0.51 MeV/c^2","carga":"-1","spin":"1/2","tipo":"Leptones","descubierto":"1897 @Cavendish Lab"},
"Foton":{"nombre":"Foton","masa":"0","carga":"0","spin":"1","tipo":"Bosones","descubierto":"1923 @Washington Univ."},
"Gluon":{"nombre":"Gluon","masa":"0","carga":"0","spin":"1","tipo":"Bosones","descubierto":"1979 @DESY"},
"Graviton":{"nombre":"Graviton","masa":"0","carga":"0","spin":"2","tipo":"Bosones (Teorico)","descubierto":"Aun no..."},
"Higss":{"nombre":"Higss","masa":"125.09 GeV/c^2","carga":"0","spin":"0","tipo":"Bosones","descubierto":"2012 @CERN"},
"Muon":{"nombre":"Muon","masa":"105.66 MeV/c^2","carga":"-1","spin":"1/2","tipo":"Leptones","descubierto":"1927 @Caltech & Harvard"},
"Neutrino-Muon":{"nombre":"Neutrino-Muon","masa":"<1.7 MeV/c^2","carga":"0","spin":"1/2","tipo":"Leptones","descubierto":"1962 @Brookhaven"},
"Neutrino-Tau":{"nombre":"Neutrino-Tau","masa":"<15.5 MeV/c^2","carga":"0","spin":"1/2","tipo":"Leptones","descubierto":"2000 @Fermilab"},
"Neutrino":{"nombre":"Neutrino","masa":"<2.2 eV/c^2","carga":"0","spin":"1/2","tipo":"Leptones","descubierto":"1956 @Shavannah River plant"},
"Quark-Beauty":{"nombre":"Quark-Beauty","masa":"4.18 GeV/c^2","carga":"-1/3","spin":"1/2","tipo":"Quarks","descubierto":"1977 @Fermilab"},
"Quark-Charm":{"nombre":"Quark-Charm","masa":"1.28 GeV/c^2","carga":"2/3","spin":"1/2","tipo":"Quarks","descubierto":"1974 @Brookhaven & SLAC"},
"Quark-Down":{"nombre":"Quark-Down","masa":"4.7 MeV/c^2","carga":"-1/3","spin":"1/2","tipo":"Quarks","descubierto":"1968 @SLAC"},
"Quark-Strange":{"nombre":"Quark-Strange","masa":"96 MeV/c^2","carga":"-1/3","spin":"1/2","tipo":"Quarks","descubierto":"1947 @Manchester Univ."},
"Quark-Top":{"nombre":"Quark-Top","masa":"173.1 GeV/c^2","carga":"2/3","spin":"1/2","tipo":"Quarks","descubierto":"1995 @Fermilab"},
"Quark-Up":{"nombre":"Quark-Up","masa":"2.2 MeV/c^2","carga":"2/3","spin":"1/2","tipo":"Quarks","descubierto":"1968 @SLAC"},
"Tau.jpg":{"nombre":"Tau","masa":"1.7768 GeV/c^2","carga":"-1","spin":"1/2","tipo":"Leptones","descubierto":"1976 @SLAC"}}
  particula=random.choice(list(particulas.keys()))
  props=particulas[particula]
  return render_template('particularandom.html', params=props)

@app.route('/elementos')
def elementos():
  return render_template('elementos.html')

@app.route('/elementorandom')
def elementorandom():
  with open('static/particulas/TablaPeriodica.json') as elementos_data:
    elementos=json.load(elementos_data)

  elemento=random.choice(list(elementos.keys()))
  props=elementos[elemento]
  return render_template('elementorandom.html', params=props)



if __name__ == '__main__':
  app.run()


