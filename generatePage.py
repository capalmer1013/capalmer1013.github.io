import yaml

head = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A layout example with a side menu that hides on mobile, just like the Pure website.">
    <title>Responsive Side Menu &ndash; Layout Examples &ndash; Pure</title>
    
    <link rel="stylesheet" href="https://unpkg.com/purecss@0.6.2/build/pure-min.css" integrity="sha384-UQiGfs9ICog+LwheBSRCt1o5cbyKIHbwjWscjemyBMT9YCUMZffs6UqUTd0hObXD" crossorigin="anonymous">

    
        <!--[if lte IE 8]>
            <link rel="stylesheet" href="css/layouts/side-menu-old-ie.css">
        <![endif]-->
        <!--[if gt IE 8]><!-->
            <link rel="stylesheet" href="css/layouts/side-menu.css">
        <!--<![endif]-->
    <!--[if lt IE 9]>
        <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.js"></script>
    <![endif]-->
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
    ga('create', 'UA-41480445-1', 'purecss.io');
    ga('send', 'pageview');
    </script>
</head>

"""

menu = """

<body>

<div id="layout">
    <!-- Menu toggle -->
    <a href="#menu" id="menuLink" class="menu-link">
        <!-- Hamburger icon -->
        <span></span>
    </a>

    <div id="menu">
        <div class="pure-menu">
            <a class="pure-menu-heading" href="#">Company</a>

            <ul class="pure-menu-list">
                <li class="pure-menu-item"><a href="index.html" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="about.html" class="pure-menu-link">About</a></li>

                <li class="pure-menu-item" class="menu-item-divided pure-menu-selected">
                    <a href="services.html" class="pure-menu-link">Services</a>
                </li>

                <li class="pure-menu-item"><a href="contact.html" class="pure-menu-link">Contact</a></li>
            </ul>
        </div>
    </div>
    
"""

mainBegin = """

    <div id="main">
        <div class="header">
            <h1>Christopher A. Palmer</h1>
            <h2>Software Engineer - Pittsburgh, PA</h2>
        </div>

        <div class="content">
        
"""

ending = """
        </div>
    </div>
</div>




<script src="js/ui.js"></script>

</body>
</html>
"""

def addHeaderBody(string, header, body):
    string += """
                <h2 class="content-subhead">"""+str(header)+"""</h2>
                <p>
                """+str(body)+"""
                </p>
    """
    return string
    
def addList(string, list):
    string += "<ul>"
    for item in list:
        string += """
                <ul>
                <li>
                    """+str(item)+"""
                </li>"""
    string += "</ul>"
    return string


def addListLinks(string, linkDict):
    string += "<ul>"
    for i in linkDict:
        string += """
                <ul>
                <li>
                    <a href="""+str(linkDict[i])+""">
                    """+str(i)+"""</a>
                </li>"""
    
    
    string +=  "</ul>"
    
    return string
  
fileString = head + menu + mainBegin

test = yaml.load(open("test.yaml"))
for each in test:
    if type(test[each]) is str:
        fileString += addHeaderBody(fileString, each, test[each])

    if type(test[each]) is list:
        fileString += addHeaderBody(fileString, each, addList('', test[each]))
        
    if type(test[each]) is dict:
        fileString += addHeaderBody(fileString, each, addListLinks('', test[each]))
    
fileString += ending

with open('test.html', 'w+') as outputfile:
    outputfile.write(fileString)
# add some code here to accept inputs and add some new posts
# especially if it makes the headder and stuff. need to think more about this.