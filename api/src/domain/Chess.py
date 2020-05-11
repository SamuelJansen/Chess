import Application, Header, ItemDto

import exitChess, newMatch

class Chess(Application.Application):

    def __init__(self,globals):

        Application.Application.__init__(self,globals,floor=True)

        headerPosition = [0,0]
        headerSize = ['100%',22]
        headerFather = self
        headerPadding = [2,2]

        Header.Header(headerPosition,headerSize,headerFather,
            items = [
                ItemDto.ItemDto('exitChess',onLeftClick=exitChess.exitChess),
                ItemDto.ItemDto('newMatch',onLeftClick=newMatch.newMatch)
            ],
            itemSize = ['square','100%'],
            itemsImagePath = None,
            itemsAudioPath = None,
            text = None,
            textPosition = None,
            fontSize = None,
            padding = headerPadding
        )
