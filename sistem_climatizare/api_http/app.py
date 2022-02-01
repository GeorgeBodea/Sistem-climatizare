import __init__
import cgi
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import sistem_climatizare.setari_utilizator.adauga_setare as adauga_setare
import sistem_climatizare.setari_utilizator.alegere_setare as alegere_setare
import sistem_climatizare.setari_utilizator.stergere_setare as stergere_setare
import sistem_climatizare.setari_utilizator.variables as variables

from sistem_climatizare.firebase_backup.firebase_api import download_all_settings as download_all_settings

from sistem_climatizare.firebase_backup.firebase_api import upload_all_settings as upload_all_settings

PORT = 8088

path_setari_custom_abs = variables.path_setari_custom_abs


def extrage_fisier(nume_fisier):
    with open(path_setari_custom_abs + nume_fisier + ".json", "r") as fisier_setare:
        setare = json.loads(fisier_setare.read())
        return setare


def parsare_informatii_fisier(continut):
    return "<html><body><h1> Informatii setare</h1>" + \
           "<p>Nume setare: " + continut["Nume_Setare"] + "</p>" + \
           "<p>Temperatura dorita: " + str(continut["Temperatura"]) + "</p>" + \
           "<p>Numar persoane: " + str(continut["Numar_Persoane"]) + "</p>" + \
           "<p>Data creere: " + continut["Data_Creare"] + "</p>" + \
           "</body></html>"


def parsare_informatii_setari(continut):
    return "<html><body><h1> Setari disponibile </h1><p>" + str(continut).replace(',', ';</p>\n<p>')[1:-1] + "</p></body></html>"


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
                except Exception as e:
                    print(e)
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

                output += '<br><p> ' + str(variables.get_lista_nume_setari()).replace(',', ';</p>\n<p>')[1:-1] + '</p>'

                output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/stergere_setare">'

                output += '<input name="nume_setare" type="text" placeholder="Nume setare"><br><br>'

                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'

                self.wfile.write(bytes(output, "utf-8"))

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

                self.wfile.write(bytes(output, "utf-8"))

            if path_web_entry == 'adaugare_setare':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += '<html><body>'
                output += '<h1> Adauga setare noua</h1>'

                output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/adaugare_setare">'

                output += '<input name="nume_setare" type="text" placeholder="Nume setare"><br><br>'
                output += '<input name="numar_persoane" type="text" placeholder="Numar persoane"><br><br>'
                output += '<input name="temperatura" type="text" placeholder="Temperatura"><br><br>'

                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'

                self.wfile.write(bytes(output, "utf-8"))
            if path_web_entry == "backup_upload":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += '<html><body>'
                output += '<h1> Autentificati-va pentru a face upload la backup </h1>'

                output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/backup_upload">'

                output += '<input name="email" type="text" placeholder="Email"><br><br>'
                output += '<input name="password" type="text" placeholder="Password"><br><br>'

                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'

                self.wfile.write(bytes(output, "utf-8"))
            if path_web_entry == "backup_download":
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = ""
                output += '<html><body>'
                output += '<h1> Autentificati-va pentru a face download la backup </h1>'

                output += '<form method="POST" enctype="application/x-www-form-urlencoded" action="/backup_download">'

                output += '<input name="email" type="text" placeholder="Email"><br><br>'
                output += '<input name="password" type="text" placeholder="Password"><br><br>'

                output += '<input type="submit" value="Submit">'
                output += '</form>'
                output += '</body></html>'

                self.wfile.write(bytes(output, "utf-8"))

        if len(path_web) == 3:
            path_web_entry = path_web[1]
            path_web_nume_fisier = path_web[2]

            if path_web_entry == 'fisiere_custom':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                try:
                    continut_fisier = extrage_fisier(path_web_nume_fisier)
                except Exception as e:
                    print(e)
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
                dictionar_setari[cheie] = urllib.parse.unquote(valoare)

            try:
                print(dictionar_setari)
                adauga_setare.adaugare_setare_fct(
                    nume_setare_custom=dictionar_setari["nume_setare"],
                    temperatura_dorita=dictionar_setari["temperatura"],
                    numar_persoane=dictionar_setari["numar_persoane"],
                )
            except Exception as e:
                print(e)
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
                dictionar_setari[cheie] = urllib.parse.unquote(valoare)

            print(str(dictionar_setari))

            try:
                stergere_setare.stergere_setare_fct(nume_setare_custom=dictionar_setari["nume_setare"])
            except Exception as e:
                print(e)
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
                dictionar_setari[cheie] = urllib.parse.unquote(valoare)

            print(str(dictionar_setari))

            try:
                alegere_setare.alegere_setare_fct(dictionar_setari["nume_setare"])
            except Exception as e:
                print(e)
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                return
            else:
                self.send_response(301)
                self.send_header("Content-type", "text/html")
                self.send_header("Location", "/fisiere_custom")
                self.end_headers()
        elif self.path.endswith('/backup_download'):
            length = int(self.headers.get('content-length'))
            message = self.rfile.read(length)
            message = message.decode("utf-8")
            message = message.split('&')

            dictionar_setari = dict()
            for element in message:
                cheie, valoare = element.split('=')
                dictionar_setari[cheie] = urllib.parse.unquote(valoare)

            print(str(dictionar_setari))

            try:
                # alegere_setare.alegere_setare_fct(dictionar_setari["nume_setare"])
                download_all_settings(dictionar_setari["email"], dictionar_setari["password"])  # aici apelam functia dintr-un script de background_download.py
            except Exception as e:
                print(e)
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                return
            else:
                self.send_response(301)
                self.send_header("Content-type", "text/html")
                self.send_header("Location", "/fisiere_custom")
                self.end_headers()
        elif self.path.endswith('/backup_upload'):
            length = int(self.headers.get('content-length'))
            message = self.rfile.read(length)
            message = message.decode("utf-8")
            message = message.split('&')

            dictionar_setari = dict()
            for element in message:
                cheie, valoare = element.split('=')
                dictionar_setari[cheie] = urllib.parse.unquote(valoare)

            print(str(dictionar_setari))

            try:
                upload_all_settings(dictionar_setari["email"], dictionar_setari["password"])
            except Exception as e:
                print(e)
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
try:
    print("Server now running...")
    httpd.serve_forever()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("Good Bye!")
finally:
    httpd.server_close()
