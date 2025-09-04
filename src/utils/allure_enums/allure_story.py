from enum import Enum


class AllureStory(str, Enum):
    CREATE_ENTITY = 'Create Entity'
    UPDATE_ENTITY = 'Update Entity'
    DELETE_ENTITY = 'Delete Entity'
    GET_ENTITY = 'Get Entity'
