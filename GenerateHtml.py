#-*- coding: utf-8 -*-

import parser
import re
from AnalysisXml import AnalysisXml
import json
class GenarateHtml:
    def __init__(self):
        self.content="";

    def readTempate(self,filename):
        fp = open(filename, 'r')
        self.content = fp.read()
        fp.close()

    def writeResult(self,filename):
        fp = open(filename,'w+')
        fp.write(self.content)
        print("write down")
        fp.close()

    def addResultData(self,readFilename,writeFilename,xmlJson):
        fp = open(writeFilename, 'w+')
        with open(readFilename, 'r') as file:
            for line in file:
                if(line.find("var resultData")>=0):

                    fp.write("var resultData = ")
                    fp.write(xmlJson);
                    fp.write(";\n")
                else:
                    fp.write(line)
            fp.close();


if __name__ == '__main__':
    analysisXml= AnalysisXml();
    analysisXml.parse("./data/cmap.xml")
    xmlJson = json.dumps(analysisXml.__dict__)

    ghtml=GenarateHtml();
    ghtml.addResultData("./data/template.html","./data/result.html",xmlJson);




    # re.findall(r'resultData = [{](.*?)[}]',ghtml.content);






