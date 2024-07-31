import ZeusSS13BR.post

class Blog:
    def __init__(self, blogName="", author="", urlBase="", numPostPerPage=5 ):
        self.blogName = blogName
        self.author = author
        self.urlBase = urlBase
        self.numPostPerPage = numPostPerPage
        self.posts = [] # load json list of posts from file
        self.input = "inputs/" # Folder of posts in markdown format
        self.output = "output/" # Folder for "output" blog html files

        self.confsDict = {}

    def __str__(self):
        return "Blog: {}\nAuthor: {}\nNumber Posts Per Page: {}\n".format(self.blogName, self.author, self.numPostPerPage)
    
    def __repr__(self):
        return "{}\n{}\n{}\n".format(self.blogName, self.author, self.numPostPerPage)

    def loadConfs( self ):
        import json
        cjson = ""

        with open("configs.json", "r" ) as fl:
            cjson = fl.read()

        self.confsDict = json.loads( cjson )


        return self

    def createPost(self, title ):
        """Create post and insert reference in json with status None (non published)."""
        import json
        import datetime

        postContent = ZeusSS13BR.post.Post("Meu Primeiro POst", "Wandeson")

        self.posts.append( postContent.post )
        
        with open( "inputs/"+postContent.post["postTitle"]+".md", "w" ) as fl:
            fl.write()

        with open( "posts.json", "w+") as fl:
            text = fl.read()
            jsoncontent = json.loads( text )
        
        