# encoding = utf-8
from config.VarConfig import pageElementLocatorPath
from configparser import ConfigParser
# 解析储存定位页面元素的定位表达式文件
class ParseConfigFile(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath,encoding='utf-8')

    def getItemsSection(self,sectionName):
        # 获取配置文件中指定section下所有option键值对
        # 并已字典类型返回给调用者
        '''注意：
        使用self.cf.items(sectionName)此种方法获取到的配置文件中options
        内容均被转换成小写，比如：loggingPage.frame被转换成loggingpage.frmae
        '''
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName,optionName):
        # 获取指定section下的指定option值
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == "__main__":
    pc = ParseConfigFile()
    print(pc.getItemsSection("163mail_addContactsPage"))
    print(pc.getOptionValue("163mail_addContactsPage","addContactsPage.createContactctsBtn"))
