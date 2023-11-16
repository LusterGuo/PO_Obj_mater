import yaml
import os

class Excel_Data:
    def __init__(self,filename):
        self.filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "Data" + os.sep + filename + ".yml"
        print("数据文件路径 :"+self.filepath)

    def excel_data(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            data=yaml.full_load(f)
            return data