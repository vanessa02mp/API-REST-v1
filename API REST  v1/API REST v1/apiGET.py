from flask import Flask

app = Flask(__name__)

# Definir la ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return "¡Hola, Tec de Pachuca!", 200

if __name__ == '__main__':
    app.run(debug=True)