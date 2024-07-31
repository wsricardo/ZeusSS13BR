import markdown2
from jinja2 import Environment
import json
import datetime
import os

import ZeusSS13BR.md2h


def createProject( title, author, urlBase = "", numberOfPostPerPage = 5 ):
      import ZeusSS13BR

      blog = ZeusSS13BR.site.Blog( title, author, urlBase, numberOfPostPerPage )
      os.mkdir( blog.output )
      os.mkdir( blog.input )

      confDict = {
                  "blogName": blog.blogName,
                  "urlBase": blog.urlBase,
                  "author": blog.author,
                  "numPostPerPage": blog.numPostPerPage,
                  "input": blog.input,
                  "output": blog.output
      }

      conf = json.dumps( confDict, indent=4 )

      with open( "configs.json", "w+" ) as fl:
            fl.write( conf )

      with open("posts.json") as fl:
            fl.write("")

      print("Created projects files. ( inputs/, output/, configs.json, posts.json)" )

def configure( blogName, author, urlBase, numPostPerPage, input="input", output="output"):
      confs = ""
      with open( "configs.json", "r") as fl:
            confs = json.loads( fl.read() )
      
      confs["blogName"] =blogName
      confs["author" ] = author
      confs["urlBase" ] = urlBase
      confs["numPostPerPage"] = numPostPerPage
      confs["input"] = input
      confs["output"] = output

      with open( "configs.json", "w") as fl:
            fl.write( json.dumps( confs, indent=4 ) )
      
      print("Configured/Update configs.json")

def cleanProject():
      import os
      import shutil

      #os.removedirs( "output")
      #os.removedirs( "input" )
      shutil.rmtree( "output" )
      shutil.rmtree( "inputs" )
      os.remove( "configs.json" )

      print("Removed dirs output, input and file configs.json")


def build( fileName ):
      import ZeusSS13BR
      import json
      content = ""

      #with open("posts.json", "r") as fl:
      #      content = json.loads( fl.read() )
      print( fileName )

      with open( "inputs/"+fileName, "r" ) as fl:
            content = fl.read()

      #postFile = content[ len( content ) - 1 ]

      ZeusSS13BR.md2h.save( ZeusSS13BR.md2h.convert( content ), fileName.split(".")[0] )

def makePost( title ):
      import ZeusSS13BR
      #post = ZeusSS13BR.post.Post( title )

      with open( "inputs/"+title +".md", "w") as fl:
            fl.write(f"# {title}")

def publish( filePost ):
      """
      1. save resgistry post info in posts.json
      2. Generate html for static page with posts.
      """

      import datetime
      import ZeusSS13BR
      
      env = Environment()
      blogConfsDict = {}
      cJsonDict = {}

      # Open configuration file.
      with open("configs.json", "r") as fl:
            blogConfs = fl.read()
            blogConfsDict = json.loads( blogConfs )


      #blog = ZeusSS13BR.site.Blog( )

      cjson = ""

      # Open jposts file json for add new post.
      with open("posts.json", "r") as fl:
            content = fl.read()
            print( "Content",  content   )

            if content == "":
                  print("Empty file. Populate base")
                  content = "[]"
                 
            cJsonDict = json.loads( content )
            date = datetime.date.today()
            print( content )

            cJsonDict.append( { "filePost":filePost, 
                               "postDate": str( date.day )+'-'+str( date.month )+'-'+str( date.year ) 
                               } )


      # Update posts.json   
      with open("posts.json", "w" ) as fl:
            fl.write( json.dumps( cJsonDict, indent=4 ) )

      # Generate static html files for blog.
      #with open("inputs/"+filePost, "r") as fl:
      #      content = fl.read()
      
      """with open("output/"+filePost.split(".")[0]+".html", "r") as fl:
            contentHTML = fl.read()

            with open("template.html", "r") as fl:
                  templateHTML = fl.read()
      

            with open("blog.html", "w") as fl:
                  template =env.from_string( templateHTML )
                  # em cJsonDict não há chave postTitle para usar no arquivo template.html. Corigir!
                  fl.write( template.render( {
                        "blogName": "wandeson Blog",
                        "posts": cJsonDict,
                        "urlBase": "output",
                        "linkOldPost": "old.html"

                        
                  } )  )"""


      print( "Published post {}".format( filePost.split(".")[0] ) )

def update():
      import json

      blogConf, posts = None, None
      template = None
      env = Environment()

      with open("configs.json", "r" ) as fl:
            blogConf = json.loads( fl.read() ) 

      with open("posts.json", "r") as fl:
            posts = json.loads( fl.read() )

      with open("template.html", "r") as fl:
            template = env.from_string( fl.read() )
      
      with open("blog.html", "w" ) as fl:

            fl.write( template.render( {
                        "blogName": "Wandeson Blog",
                        "posts": posts,
                        "urlBase": "output",
                        "linkOldPost": "old.html"            
                  } )  )
                  
   
if __name__ == "__main__":
      import sys

      print( sys.argv[0] )

      if len( sys.argv ) > 1:
            print( sys.argv[0], sys.argv[1] )

            if sys.argv[1] == "create":
                  createProject( "Wandeson Blog", "Wandeson", "/", 5 )

            elif sys.argv[1] == "post":
                  print("Create post")
                  makePost( " ".join( sys.argv[2:] ) )

            elif sys.argv[1] == "clean" :
                  cleanProject() 

            elif sys.argv[1] == "publish":
                  if len( sys.argv ) > 1:
                        print(" Add new post ")
                        publish( sys.argv[2] )
                  else:
                        print( "Specify name post file markdown for publish in blog.")

            elif sys.argv[1] == "build":
                  print("Build post blog")
                  build( sys.argv[2] )

            elif sys.argv[1] == "update":
                  print("Update blog.")
                  update()
      else:
         print("Argument comand line required!")
         print("""
            Command Line Arguments
               
               create - create Project;
               post - create posting; (not implemented)
               clean - remove dirs, files and configurations for project
               pusblish - add new post specified in command line register post in json file of posts [ Example: script.py publish <file.md> ]
               build - convert markdown file in post folder to html for folder output
            """ )
           
      """with open( str( sys.argv[1] ) , "r") as fl:
            text = fl.read()
      
      html = markdown2.markdown( text )

      with open( str( sys.argv[2] ), "w") as fl:
                  fl.write( text )
      """