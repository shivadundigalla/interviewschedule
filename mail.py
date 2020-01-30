import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("shiva.darwinbox@gmail.com", "Abcd@1234")
message = "Divishad"
s.sendmail("shiva.darwinbox@gmail.com", "balemivikas@gmail.com", message)
s.quit()