import subprocess
import pandas as pd
import time
import os
from datetime import datetime
import win32com.client

# === CONFIGURATION ===
IP_LIST = ['192.168.0.1', '192.168.0.2']
EXCEL_FILE = 'ip_status_log.xlsx'
CHECK_INTERVAL = 10  # seconds

# === Function to ping an IP ===
def is_ip_alive(ip):
    try:
        output = subprocess.check_output(['ping', '-n', '1', ip], universal_newlines=True)
        return "TTL=" in output
    except subprocess.CalledProcessError:
        return False

# === Function to send email if IP is down ===
def send_email(ip):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = "infrateam@example.com"
    mail.Subject = f"[ALERT] IP Down - {ip}"
    mail.Body = f"The IP address {ip} is DOWN as of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    mail.Send()

# === Function to update Excel ===
def update_excel(data):
    df_new = pd.DataFrame(data, columns=['Timestamp', 'IP Address', 'Status'])

    if os.path.exists(EXCEL_FILE):
        df_existing = pd.read_excel(EXCEL_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(EXCEL_FILE, index=False)

# === MAIN LOOP ===
print("Starting IP monitor... Press Ctrl+C to stop.")

try:
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        records = []

        for ip in IP_LIST:
            status = "UP" if is_ip_alive(ip) else "DOWN"
            print(f"{timestamp} | {ip} --> {status}")

            if status == "DOWN":
                send_email(ip)

            records.append([timestamp, ip, status])

        update_excel(records)
        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
