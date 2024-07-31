import markdown2


def convert(textmd):
    """Convert markdown text for html file."""

    return markdown2.markdown( textmd )

def save(htmltext, namefile):
    """Save html text converted with convert function"""
    with open("output/"+namefile+".html", "w" ) as fl:
        fl.write( htmltext )
    print( "saved.")
