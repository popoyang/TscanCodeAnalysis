#-*- coding: utf-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import re
import json
import time

class AnalysisXml:
    def __init__(self):
        self.testResult=[];
        self.infoCount=0;
        self.warnCount=0;
        self.criticalCount=0;
        self.seriousCount=0;
        self.total=0;
        self.beginTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def parse(self,xmlPath):
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(xmlPath)
        collection = DOMTree.documentElement

        # 在集合中获取所有电影


        errors = collection.getElementsByTagName("error")
        for error in errors:
            filename=error.getAttribute("file")

            paraDict = {
                'file': filename[filename.index("cmap"):],
                'func_info': error.getAttribute("func_info"),
                'content': [],
                'id': error.getAttribute("id"),
                'line': error.getAttribute("line"),
                'msg': error.getAttribute("msg"),
                'severity': error.getAttribute("severity"),
                'subid': error.getAttribute("subid"),
                'web_identify': error.getAttribute("web_identify")
            }
            if (error.getAttribute("severity") == "Information"):
                self.infoCount = self.infoCount + 1;
            elif (error.getAttribute("severity") == "Warning"):
                self.warnCount = self.warnCount + 1;
            elif (error.getAttribute("severity") == "Critical"):
                self.criticalCount = self.criticalCount + 1;
            elif (error.getAttribute("severity") == "Serious"):
                self.seriousCount = self.seriousCount + 1;

            paraDict['content'].append('subid: '+ error.getAttribute("subid"));
            paraDict['content'].append('func_info: '+ error.getAttribute("func_info"));
            paraDict['content'].append('msg: '+ error.getAttribute("msg"));


            content=error.getAttribute("content");
            contentstr=re.sub(r"([1-9][0-9]*:)", "\n   ", content);
            contentlist=contentstr.split("\n")
            lines=re.findall(r"([1-9][0-9]*:)", content)
            for i in range(len(lines)):
                paraDict['content'].append(lines[i]+contentlist[i]);


            self.testResult.append(paraDict);

        self.total=len(self.testResult)



if __name__ == '__main__':
    # analysisXml= AnalysisXml();
    # analysisXml.parse("./data/cmap.xml")
    str="/Users/yangbo7/Code/MT/cmap/map/base/mlp/tensorflow-1.10.1/tensorflow/compiler/jit/xla_device_context.cc"
    str2="cmap"
    print(str[str.index(str2):])





