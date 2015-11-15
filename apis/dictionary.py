from xml.etree import ElementTree
import urllib2, urllib, warnings

warnings.filterwarnings("ignore",
    message="The behavior of this method will change in future versions.")

def query(term):
    if not term:
        return
    response = ElementTree.fromstring(
        urllib2.urlopen(
            urllib2.Request(
                "http://services.aonaware.com/DictService/DictService.asmx/Define?word={}".format(
                    urllib.quote(term.encode('utf8'))
                ))).read())
    return format_response(response)

def format_response(root):
    out = {'term': root[0].text, 'definitions': []}
    for definition in root[1]:
        out['definitions'].append({
            'term': definition[0].text,
            'dictionary': definition[1][1].text,
            'definition': definition[2].text.split('\n')
        })
    return out