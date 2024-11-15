# ใช้ Python 3 image
FROM python:3

# ตั้ง working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt (ถ้ามี)
COPY requirements.txt ./

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์ python script
COPY mqtt_subscribe.py ./

# รันสคริปต์เมื่อ container เริ่มทำงาน
CMD ["python", "mqtt_subscribe.py"]
