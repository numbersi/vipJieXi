from  werkzeug.routing import BaseConverter

class ReConverter(BaseConverter):
    ''''''
    def __init__(self,url_map,regex):
        # 调用父类初始化方法
        super(ReConverter,self).__init__(url_map)
        # 保存正则表达式
        self.regex = regex
