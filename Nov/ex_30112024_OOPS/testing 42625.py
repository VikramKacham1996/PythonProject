import smtplib

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)

# Start TLS for security
server.starttls()

# Login to your Gmail account using App Password
server.login('vikky.kacham@gmail.com', '995724648@v')

# Send email
server.sendmail(
    'vikky.kacham@gmail.com',
    'vikky.kacham2@gmail.com',
    'Mail sent from Python'
)

# Print confirmation
print('Mail sent')

# Quit the server
server.quit()


