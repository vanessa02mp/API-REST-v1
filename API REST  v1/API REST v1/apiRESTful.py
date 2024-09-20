from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL base de la API de MockAPI
BASE_URL = 'https://66eb01d455ad32cda47b4e6c.mockapi.io/IoTCarStatus'

# Obtener todos los registros (GET)
@app.route('/cars', methods=['GET'])
def get_all_cars():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'No se pudieron obtener los datos'}), response.status_code

# Obtener un registro específico (GET)
@app.route('/cars/<car_id>', methods=['GET'])
def get_car_by_id(car_id):
    response = requests.get(f"{BASE_URL}/{car_id}")
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'El coche con ID {car_id} no se encontró'}), response.status_code

# Crear un nuevo registro (POST)
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({'error': 'No se pudo crear el coche'}), response.status_code

# Actualizar un registro existente (PUT)
@app.route('/cars/<car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.get_json()
    response = requests.put(f"{BASE_URL}/{car_id}", json=data)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'No se pudo actualizar el coche con ID {car_id}'}), response.status_code

# Eliminar un registro (DELETE)
@app.route('/cars/<car_id>', methods=['DELETE'])
def delete_car(car_id):
    response = requests.delete(f"{BASE_URL}/{car_id}")
    if response.status_code == 200:
        return jsonify({'message': f'Coche con ID {car_id} eliminado'}), 200
    else:
        return jsonify({'error': f'No se pudo eliminar el coche con ID {car_id}'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
