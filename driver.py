
from flask import Blueprint, request, jsonify

driver_bp = Blueprint('driver', __name__)

drivers = []
ride_requests = []
ride_history = []

@driver_bp.route('/register/', methods=['POST'])
def register():
    data = request.json
    drivers.append(data)
    return jsonify({'message': 'Driver registered successfully'}), 201

@driver_bp.route('/login/', methods=['POST'])
def login():
    data = request.json
    for driver in drivers:
        if driver['phone'] == data['phone']:
            return jsonify({'token': 'dummy-token'})
    return jsonify({'error': 'Driver not found'}), 404

@driver_bp.route('/update-location/', methods=['POST'])
def update_location():
    return jsonify({'message': 'Location updated'})

@driver_bp.route('/status/', methods=['POST'])
def set_status():
    return jsonify({'message': 'Status updated'})

@driver_bp.route('/ride-requests/', methods=['GET'])
def get_ride_requests():
    return jsonify(ride_requests)

@driver_bp.route('/accept-ride/', methods=['POST'])
def accept_ride():
    return jsonify({'message': 'Ride accepted'})

@driver_bp.route('/reject-ride/', methods=['POST'])
def reject_ride():
    return jsonify({'message': 'Ride rejected'})

@driver_bp.route('/rides/', methods=['GET'])
def ride_history_view():
    return jsonify(ride_history)

@driver_bp.route('/earnings/', methods=['GET'])
def earnings():
    return jsonify({'earnings': 1200})
