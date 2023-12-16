from flask import Flask, jsonify, request
from compatibility_manager import CompatibilityProfile
from sorting_engine import SortingEngine
from backup_manager import BackupManager
from logger import Logger
from scheduler import Scheduler
import os

app = Flask(__name__)

# Instantiate the system components
compatibility_profile = CompatibilityProfile()
sorting_engine = SortingEngine('library', 'backup')
backup_manager = BackupManager('backup')
logger = Logger('activity.log')
scheduler = Scheduler()

@app.route('/add_compatible_format', methods=['POST'])
def add_compatible_format():
    data = request.json
    file_format = data['file_format']
    sample_rate = data['sample_rate']
    compatibility_profile.add_compatible_format(file_format, sample_rate)
    logger.log_activity(f"Added compatible format: {file_format} with sample rate: {sample_rate}")
    return jsonify({'message': 'Compatible format added successfully'}), 200

@app.route('/remove_compatible_format', methods=['POST'])
def remove_compatible_format():
    data = request.json
    file_format = data['file_format']
    compatibility_profile.remove_compatible_format(file_format)
    logger.log_activity(f"Removed compatible format: {file_format}")
    return jsonify({'message': 'Compatible format removed successfully'}), 200

@app.route('/list_compatible_formats', methods=['GET'])
def list_compatible_formats():
    formats = compatibility_profile.list_compatible_formats()
    logger.log_activity("Listed compatible formats")
    return jsonify(formats), 200

@app.route('/schedule_task', methods=['POST'])
def schedule_task():
    data = request.json
    task_name = data['task_name']
    schedule_time = data['schedule_time']
    # Task scheduling logic will be added here
    logger.log_activity(f"Scheduled task: {task_name} at {schedule_time}")
    return jsonify({'message': 'Task scheduled successfully'}), 200

if __name__ == '__main__':
    app.run(debug=False)
