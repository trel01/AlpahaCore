from myapp import db  # นำเข้า db จากฟังก์ชัน create_app
from datetime import datetime

class MachineData(db.Model):
    __tablename__ = 'machine_data'
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(50), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, machine_id, temperature):
        self.machine_id = machine_id
        self.temperature = temperature
