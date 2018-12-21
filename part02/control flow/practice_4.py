items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>\n"
print(html_str)

'''
<ul>
<li>first string</li>
<li>second string</li>
</ul>
'''