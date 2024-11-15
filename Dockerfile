# เริ่มจาก base image python:3
FROM python:3

# กำหนด working directory
WORKDIR /app



# Copy ไฟล์ requirement.txt
COPY mqtt/requirement.txt .

# Copy app.py จากโฟลเดอร์ mqtt
COPY mqtt/app.py .


# ติดตั้ง dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirement.txt



# Adjust the CMD command
CMD ["python", "app.py"]
