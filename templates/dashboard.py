from flask import Blueprint, render_template
import sqlite3

dashboard_blueprint = Blueprint('dashboard', __name__, template_folder='templates', static_folder='static')

@dashboard_blueprint.route('/dashboard')
def show_dashboard():
    # ดึงข้อมูลจากฐานข้อมูลมาแสดงในแดชบอร์ด
    conn = sqlite3.connect('database/db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM machine_data ORDER BY timestamp DESC LIMIT 200")
    data = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', data=data)
