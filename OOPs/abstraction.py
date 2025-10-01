#Abstraction

#Reduce complexity by hiding unneccessary details

class EmailServer:

    def _connect(self):
        print("Connecting to email sever")

    def _aunthenticate(self,username,password):
        print(f"Authenticating user:{username}")

    def send_email(self,username,password):
         # User only sees send_email, not the inner details
        self._connect()
        self._aunthenticate(username,password)
        print("Sending email....")
        self._disconnet()

    def _disconnet(self):
        print("disconnecting from email server..")

# Client code (user doesn't worry about connection, authentication, etc.)
email = EmailServer()
email.send_email("danny@gmaill.com","mypass")