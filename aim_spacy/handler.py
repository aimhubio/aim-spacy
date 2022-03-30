class Handler:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Handler.__instance == None:
            Handler()
        return Handler.__instance

    def set_attr(self, **kwargs):
        print(type(kwargs))
        print('html_handeler' in kwargs)
        if 'html_handeler' in kwargs:
            self.html_handeler = kwargs['html_handeler']
        if 'svg_handeler' in kwargs:
            self.svg_handeler = kwargs['svg_handeler']
        if 'aim_handeler' in kwargs:
            self.aim_handeler = kwargs['aim_handeler']
        if 'aim_run' in kwargs:
            self.aim_run = kwargs['aim_run']
        self.__instance = self

    def __init__(self,):
        """ Virtually private constructor. """
        if Handler.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Handler.__instance = self
