with open('/var/log/auth.log', 'r') as file:
    lines = file.readlines()

failed_attempts = [line for line in lines if "Failed password" in line]

if len(failed_attempts) > 5:
    print("⚠️ ALERT: Possible brute-force attack detected!")
else:
    print("No suspicious activity detected.")
