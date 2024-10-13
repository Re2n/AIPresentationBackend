from enum import Enum


class ActionModel(str, Enum):
    actionStart = 'actionStart'
    actionPayment = 'actionPayment'
    actionGeneration = 'actionGeneration'
    actionLowGeneration = 'actionLowGeneration'
    actionHighGeneration = 'actionHighGeneration'
    actionSendUrl = 'actionSendUrl'
    actionSendPictures = 'actionSendPictures'
    actionSendDescription = 'actionSendDescription'
    actionSendType = 'actionSendType'
    actionCheckBalance = 'actionCheckBalance'
    actionSuccessGeneration = 'actionSuccessGeneration'
    actionSuccessPayment = 'actionSuccessPayment'