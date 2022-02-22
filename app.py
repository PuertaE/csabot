from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://puerta:puerta@cluster0.coyqn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster["csa"]
users = db["users"]
# orders = db["orders"]

app = Flask(__name__)


@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("message")
    number = request.form.get("sender")
    res = {"reply": ""}
    user = users.find_one({"number": number})
    if bool(user) == False:
        res["reply"] += '\n' + ("*Colegio San Agustín de la Laguna* \n ¡Hola! Bienvenido a nuestra institución 🐻. \n ¿En qué nivel educativo estás interesado?"
                    "\n\n*Favor de elegir una opción con número*\n\n 1️⃣ INICIAL \n 2️⃣ PREESCOLAR  \n 3️⃣ PRIMARIA \n 4️⃣ SECUNDARIA \n 5️⃣ BACHILLERATO" )
        users.insert_one({"number": number, "status": "main", "messages": []})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res["reply"] += '\n' + ("Selecciona una opción con número")
            return str(res)

        if option == 1:
            res["reply"] += '\n' + (
                "*Colegio San Agustín de la Laguna* \n Gracias por tú respuesta. \n Nos podrías ayudar con la siguiente información para darte una atención personalizada: \n"
                "✅Nombre del alumno. \n ✅Grado y nivel al que va. \n ✅Escuela de procedencia. \n ✅¿Cómo te enteraste de nuestra institución? \n ✅Correo electrónico. \n\n"
                  "*En un momento un asesor le dará la información solicitada.*")
        elif option == 2:
            res["reply"] += '\n' + (
                "*Colegio San Agustín de la Laguna* \n Gracias por tú respuesta. \n Nos podrías ayudar con la siguiente información para darte una atención personalizada: \n"
                "✅Nombre del alumno. \n ✅Grado y nivel al que va. \n ✅Escuela de procedencia. \n ✅¿Cómo te enteraste de nuestra institución? \n ✅Correo electrónico. \n\n"
                "*En un momento un asesor le dará la información solicitada.*")
        elif option == 3:
            res["reply"] += '\n' + (
                "*Colegio San Agustín de la Laguna* \n Gracias por tú respuesta. \n Nos podrías ayudar con la siguiente información para darte una atención personalizada: \n"
                "✅Nombre del alumno. \n ✅Grado y nivel al que va. \n ✅Escuela de procedencia. \n ✅¿Cómo te enteraste de nuestra institución? \n ✅Correo electrónico. \n\n"
                "*En un momento un asesor le dará la información solicitada.*")

        elif option == 4:
            res["reply"] += '\n' + (
                "*Colegio San Agustín de la Laguna* \n Gracias por tú respuesta. \n Nos podrías ayudar con la siguiente información para darte una atención personalizada: \n"
                "✅Nombre del alumno. \n ✅Grado y nivel al que va. \n ✅Escuela de procedencia. \n ✅¿Cómo te enteraste de nuestra institución? \n ✅Correo electrónico. \n\n"
                "*En un momento un asesor le dará la información solicitada.*")
        elif option == 5:
            res["reply"] += '\n' + (
                "*Colegio San Agustín de la Laguna* \n Gracias por tú respuesta. \n Nos podrías ayudar con la siguiente información para darte una atención personalizada: \n"
                "✅Nombre del alumno. \n ✅Grado y nivel al que va. \n ✅Escuela de procedencia. \n ✅¿Cómo te enteraste de nuestra institución? \n ✅Correo electrónico. \n\n"
                "*En un momento un asesor le dará la información solicitada.*")
        else:
            res["reply"] += '\n' + ("Selecciona una opción con número")
   
   
if __name__ == "__main__":
    app.run()
    
