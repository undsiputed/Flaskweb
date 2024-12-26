import smtplib

# Replace these with your credentials
EMAIL = 'deb458746@gmail.com'
APP_PASSWORD = 'gkmm nkvb ziqh kcrl'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Initiates TLS encryption
    server.login(EMAIL, APP_PASSWORD)  # Pass email and password as strings
    print("Login successful")
    server.quit()
except Exception as e:
    print(f"Error during SMTP connection: {e}")
