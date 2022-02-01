from distutils.log import error
from http.server import HTTPServer, BaseHTTPRequestHandler
from importlib.resources import path
import json
import sys
import cgi

sys.path.append("../setari_utilizator")
import variables
import adauga_setare
import stergere_setare
import alegere_setare

PORT = 8088

path_setari_custom_abs = variables.path_setari_custom_abs

def extrage_fisier(nume_fisier):
      with open(path_setari_custom_abs + "/" + nume_fisier + ".json", "r") as fisier_setare:
        setare = json.loads(fisier_setare.read())
        return setare

def parsare_informatii_fisier(continut):
    return "<html><body><h1> Informatii setare</h1><p>" + continut["Nume_Setare"] + " " + continut["Data_Creare"] + " " + str(continut["Temperatura"]) + " " +str(continut["Numar_Persoane"]) + " " + "</p></body></html>"

def parsare_informatii_setari(continut):
    return "<html><body><h1> Informatii setari </h1><p>" + str(continut) + "</p></body></html>"

def not_found():
    return "<html><body><h1> Informatiile cerute nu exista </h1><p>" + "</p></body></html>"

class NucleumHTTP(BaseHTTPRequestHandler):

  def do_GET(self):
    path_web = self.path.split("/")
    # /info/ -> split -> [ [], [info], [] ]?
    print(path_web)

    if len(path_web) == 2:
      path_web_entry = path_web[1]
      if path_web_entry == 'fisiere_custom':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            try:
              continut_fisier = variables.get_lista_nume_setari()
            except:
              self.wfile.write(bytes(not_found(), "utf-8"))
            else:
              self.wfile.write(bytes(parsare_informatii_setari(continut_fisier), "utf-8"))
      if path_web_entry == 'stergere_setare':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            output = ""
            output += '<html><body>'
            output += '<h1> Stergere setare</h1>'
 
            output += '<br><p> ' + str(variables.get_lista_nume_setari()) + '</p>'

            output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/stergere_setare">'

            output += '<input name="nume_setare" type="text" placeholder="Nume setare"><br><br>'

            output += '<input type="submit" value="Submit">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(bytes( output , "utf-8"))
      
      if path_web_entry == 'alegere_setare':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            output = ""
            output += '<html><body>'
            output += '<h1> Alegere setare </h1>'
 
            output += '<br><p> ' + str(variables.get_lista_nume_setari()) + '</p>'

            output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/alegere_setare">'

            output += '<input name="nume_setare" type="text" placeholder="Nume setare"><br><br>'

            output += '<input type="submit" value="Submit">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(bytes( output , "utf-8"))

      if path_web_entry == 'adaugare_setare':
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        output = ""
        output += '<html><body>'
        output += '<h1> Adauga setare noua</h1>'

        output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/adaugare_setare">'

        output += '<input name="nume_setare" type="text" placeholder="Nume setare"><br>'
        output += '<input name="numar_persoane" type="text" placeholder="Numar persoane"><br>'
        output += '<input name="temperatura" type="text" placeholder="Temperatura"><br><br>'

        output += '<input type="submit" value="Submit">'
        output += '</form>'
        output += '</body></html>'

        self.wfile.write(bytes( output , "utf-8"))

    if len(path_web) == 3:
      path_web_entry = path_web[1]
      path_web_nume_fisier = path_web[2] 

      if path_web_entry == 'fisiere_custom':
          self.send_response(200)
          self.send_header("Content-type", "text/html")
          self.end_headers()
          
          try:
            continut_fisier = extrage_fisier(path_web_nume_fisier)
          except:
            self.wfile.write(bytes(not_found(), "utf-8"))
          else:
            self.wfile.write(bytes(parsare_informatii_fisier(continut_fisier), "utf-8"))
    
  def do_POST(self):
     if self.path.endswith('/adaugare_setare'):
        ctype = cgi.parse_header(self.headers.get('Content-type'))
  
        length = int(self.headers.get('content-length'))
        message = self.rfile.read(length)
        message = message.decode("utf-8")
        message = message.split('&')

        dictionar_setari = dict()
        for element in message:
          cheie, valoare = element.split('=')
          dictionar_setari[cheie] = valoare

        try:
          adauga_setare.adaugare_setare_fct(dictionar_setari["nume_setare"], dictionar_setari["numar_persoane"], dictionar_setari["temperatura"])
          print(dictionar_setari)
        except:
          self.send_response(400)
          self.send_header("Content-type", "text/html")
          self.end_headers()
          return
        else:
          self.send_response(301)
          self.send_header("Content-type", "text/html")
          self.send_header("Location", "/fisiere_custom")
          self.end_headers()
     elif self.path.endswith('/stergere_setare'):
          length = int(self.headers.get('content-length'))
          message = self.rfile.read(length)
          message = message.decode("utf-8")
          message = message.split('&')

          dictionar_setari = dict()
          for element in message:
            cheie, valoare = element.split('=')
            dictionar_setari[cheie] = valoare

          print(str(dictionar_setari))

          try:
            stergere_setare.stergere_setare_fct(dictionar_setari["nume_setare"])
          except:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            return
          else:
            self.send_response(301)
            self.send_header("Content-type", "text/html")
            self.send_header("Location", "/fisiere_custom")
            self.end_headers()
     elif self.path.endswith('/alegere_setare'):
          length = int(self.headers.get('content-length'))
          message = self.rfile.read(length)
          message = message.decode("utf-8")
          message = message.split('&')

          dictionar_setari = dict()
          for element in message:
            cheie, valoare = element.split('=')
            dictionar_setari[cheie] = valoare

          print(str(dictionar_setari))

          try:
            alegere_setare.alegere_setare_fct(dictionar_setari["nume_setare"])
          except:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            return
          else:
            self.send_response(301)
            self.send_header("Content-type", "text/html")
            self.send_header("Location", "/fisiere_custom")
            self.end_headers()



httpd = HTTPServer(("", PORT), NucleumHTTP)

print("Server now running...")
httpd.serve_forever()
httpd.server_close()