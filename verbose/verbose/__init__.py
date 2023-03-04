class get_logger:
    def __init__(self, strict: bool = True):
        self.level = 0
        self.start = True
        self.strict = strict

    def next(self, text: str = '', end: str = '\n', by: int = 1, toprint: bool = True):
        self.level += by
        start = False
        if self.start:
            start = True
            if toprint:
                print(
                    f"{'|'+'____'*(self.level-by)+'____________________________________________________'}")
            self.start = False
        else:
            if toprint:
                print(
                    f"{'____'*(self.level-by)+'|'+'____________________________________________________'}")
        message = f"{self.level*'    '}|{text}" + end
        if toprint:
            print(f"{self.level*'    '}|{text}", end=end)
        if start:
            return f"{'|'+'____'*(self.level-by)+'____________________________________________________'}\n" + message
        else:
            return message

    def prev(self, text: str = '', end: str = '\n', by: int = 1, toprint: bool = True):
        if self.level == 0:
            if self.strict:
                raise RuntimeError('Can not go under the current level')
            else:
                return 'Can not go under the current level'
        self.level -= by
        if toprint:
            print(
                f"{'____'*(self.level+by)+'|'+'____________________________________________________'}")
        if self.level == 0:
            self.start = True
            message = f"|{self.level*'    '}{text}"
            if toprint:
                print(f"|{self.level*'    '}{text}", end=end)
            return message + end
        else:
            message = f"{self.level*'    '}|{text}"
            if toprint:
                print(f"{self.level*'    '}|{text}", end=end)
            return message + end

    def stay(self, text: str = '', end: str = '\n', toprint: bool = True):
        if toprint:
            print(f"{self.level*'    '}|{text}", end=end)
        return f"{self.level*'    '}|{text}" + end
