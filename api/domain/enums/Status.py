from enum import Enum, unique

@unique
class Status(Enum):
    NORMAL= 'NORMAL'
    FAULT = 'FAULT'
    INOPERATIVE = 'INOPERATIVE'
    