# -*- coding: utf-8 -*-

import logging
import uvclight
from fanstatic import Library, Resource
from nva.psyquizz.models.interfaces import IQuizzSecurity
from grokcore.component import context, Subscription
from zope.interface import Interface, implementer


library = Library('psyquizz.bgetem', 'static')
bgetemcss = Resource(library, 'bgetem.css')


def get_template(name):
    return uvclight.get_template(name, __file__)


@implementer(IQuizzSecurity)
class SecurityCheck(Subscription):
    context(Interface)

    def check(self, name, quizz, context):
        return True
