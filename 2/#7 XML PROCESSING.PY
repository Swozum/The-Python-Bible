#7 XML PROCESSING

#XML PARSER
#SAX = SIMPLE API FOR XML
#Serve para dispositivos mais leves,ele nao carrega todo o arquivo para a cpu, facilitando a utilização do programa
#em cpu mais fracas. Porem ao nao utilizar todo o recurso, a unica operação que se pode realizar com o SAX e ler o arquivo

#DOM = DOCUMENT OBJECT MODEL
#Serve para realizar quase todos as funções, e mais rapidd do que o SAX

#XML With SAX
import xml.sax

handler = xml.sax.ContentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("group.xml")

#Content Handler Class
class GroupHandler(xml.sax.ContentHandler):
	def startElement(self, name, attrs):
		print(name)

handler = xml.sax.ContentHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("group.xml")