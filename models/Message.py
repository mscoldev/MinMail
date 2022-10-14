class Message:
    def __init__(self, to, subject, message):
        self.to = to
        self.subject = subject
        self.message = message
        
            
    def serialize(self):
        return{
            "to":self.to,
            "subject":self.subject,
            "message":self.message
        }