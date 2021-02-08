import os
site=open('text.html','w')
site.write("<html>")
site.write("<body>")
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".jpg"):
           site.write("<img src=\""+file+"\"width=\"400\"/>")
           site.write("<p>"+file+"</p>")
           site.write("<hr/>")  
site.write("</body>")
site.write("</html>")
site.close()
           
