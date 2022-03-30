import csv
import requests
import xml.etree.ElementTree as ET


def loadRSS():
    # url of rss feed
    url = 'https://vnexpress.net/rss/the-thao.rss'
  
    # creating HTTP response object from given url
    resp = requests.get(url)
  
    # saving the xml file
    with open('thethao.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    list_url = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
            if child.tag == 'link':
                list_url.append(child.text)
      
    # return news items list
    return list_url


def main():
    # # load rss from web to update existing xml file
    # loadRSS()
  
    # parse xml file
    list_url = parseXML('thethao.xml')

      
if __name__ == "__main__":
    # calling main function
    main()