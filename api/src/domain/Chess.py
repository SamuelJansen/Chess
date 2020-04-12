import Application, Header, ItemDto

import settingFunction, exitChess

class Chess(Application.Application):

    def __init__(self,pathMannanger):

        Application.Application.__init__(self,pathMannanger,floor=True)
