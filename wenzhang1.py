import urllib.request
import re

url = 'http://www.cnblogs.com/over140/p/4440137.html'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html_page = resp.read().decode('utf-8')

title_pattern = r'(<a.*id="cb_post_title_url".*>)(.*)(</a>)'
title_match = re.search(title_pattern,html_page)
title = title_match.group(2)
print(title)
