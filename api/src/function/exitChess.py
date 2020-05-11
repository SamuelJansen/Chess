import Message, ItemDto
import textFunction

messageName = 'exitChessMessage'

def exitChess(event):

    buttonPosition = ['fill','center']
    buttonSize = [85,45]
    messageFontSize = 18
    textPosition = ['center','padded']

    cancelButtonDto = ItemDto.ItemDto('cancel',
        position = buttonPosition,
        size = buttonSize,
        text = 'Cancel',
        textPosition = textPosition,
        onLeftClick = cancel
    )
    okButtonDto = ItemDto.ItemDto('ok',
        position = buttonPosition,
        size = buttonSize,
        text = 'Ok',
        textPosition = textPosition,
        onLeftClick = ok
    )

    messageButtonsDto = [cancelButtonDto,okButtonDto]
    message = 'Do you want to exit the game?'

    Message.Message(event.object,message,
        name = messageName,
        messageButtonsDto = messageButtonsDto,
        fontSize = messageFontSize
    )

def cancel(event) :
    message = event.application.findObjectByName(messageName)
    message.close()

def ok(event) :
    message = event.application.findObjectByName(messageName)
    message.close()

    application = event.application
    application.close(event)
