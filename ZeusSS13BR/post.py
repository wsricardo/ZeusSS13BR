class Post:
    def __init__(self, postTitle, postAuthor ):
        self.postTitle = postTitle
        self.postAuthor = postAuthor
        self.contentPost = ""
        self.datePost = ""
        self.description = ""
        self.postFile = str.lower( self.postTitle )

    def __str__(self):
        return f"""Post: {self.postTitle} 
                Author: {self.postAuthor} 
                Date: {self.datePost} 
                Description: {self.description}
        """
    
    
    @property
    def post(self):
        return { "postTitle": self.postTitle, "postDesc": self.description, "postFile": self.postFile }
    