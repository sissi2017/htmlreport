html_string = '''
<html>
    <head>
       
        <style>body{ margin:0 100; background:whitesmoke; }</style>
    </head>
    <body>
        <h1>2014 technology and CPG stock prices</h1>

        <!-- *** Section 1 *** --->
        <h2>Section 1: Apple Inc. (AAPL) stock in 2014</h2>
        <iframe width=1000 height=800 src="basic-line.html">
        </iframe>
        
    </body>
</html>'''
f = open('report.html','w')
f.write(html_string)
f.close()