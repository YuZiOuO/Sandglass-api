from enum import Enum

import mongoengine as me
from mongoengine import ReferenceField, EnumField, EmbeddedDocumentListField

from sandglass_api.models.user import User


# TODO:暂时不使用

class Permission(Enum):
    NO_ACCESS = 0
    READ = 1
    WRITE = 2


class AccessControlEntry(me.EmbeddedDocument):
    user = ReferenceField(User, required=True)
    permissions = EnumField(Permission, required=True, default=Permission.NO_ACCESS)


class AccessControlList(me.Document):
    ACEs = EmbeddedDocumentListField(AccessControlEntry)  # 这里不用Reference,因为希望ACE失效时从数据库中删除.
