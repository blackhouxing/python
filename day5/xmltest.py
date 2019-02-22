import xml.etree.ElementTree as ET
import os,sys
import configparser
tree = ET.parse("xmltest")
root = tree.getroot()

config = configparser.ConfigParser()
import hashlib
import subprocess
import logging

# logging.warning('user [zhang] attempted wrong password more than 3 times')
# logging.critical('server 1 is down')

logging.basicConfig(format= '%(asctime)s %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    filename='example.log',level=logging.INFO)
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this ,too')

print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) )


# subprocess.run
#
# m = hashlib.md5()
# m.update(b'hello')
# print(m.hexdigest())
# config["DEFAULT"] = {'ServerAliverInterval':'45','Compression':'yes',
#                      'CompressionLevel':'9'}
# config["bitbucket.org"] = {}
# config["bitbucket.org"]["User"] = 'hg'
# config["topsecret.server.com"] = {}
#
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'
# topsecret['Forwardx11'] = 'no'
# config['DEFAULT']['Forwardx11'] = 'yes'
# with open('example.ini','w') as configfile:
#     config.write(configfile)

# print(root.tag)


# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print(i.tag,i.attrib)
#
# print(os.getcwd())
# print(os.pathsep)
# # print(os.environ)
# print(os.pardir)
# print(os.name)
# print(os.path.abspath())

# for country in root.findall('country'):
#
#     rank = int(country.find('rank').text)
#     print(rank)
#     if rank > 50:
#         root.remove(country)
# tree.write('output.xml')

# config.read('example.ini')
# print(config.sections())
