from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sistem_climatizare.setari_utilizator.variables as variables

PORT = 8088

path_setari_custom_abs = variables.path_setari_custom_abs
lista_nume_setari = variables.lista_nume_setari


def extrage_fisier(nume_fisier):
    with open(path_setari_custom_abs + "/" + nume_fisier + ".json", "r") as fisier_setare:
        setare = json.loads(fisier_setare.read())
        return setare


def parsare_informatii_fisier(continut):
    return "<html><body><h1> Informatii setare</h1><p>" + \
           continut["Nume_Setare"] + " " + \
           continut["Data_Creare"] + " " + \
           str(continut["Temperatura"]) + " " + \
           str(continut["Numar_Persoane"]) + " " + \
           "</p></body></html>"


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
                    continut_fisier = lista_nume_setari
                except:
                    self.wfile.write(bytes(not_found(), "utf-8"))
                else:
                    self.wfile.write(bytes(parsare_informatii_setari(continut_fisier), "utf-8"))

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


httpd = HTTPServer(("", PORT), NucleumHTTP)

print("Server now running...")
httpd.serve_forever()
httpd.server_close()
