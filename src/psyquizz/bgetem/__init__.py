# -*- coding: utf-8 -*-

import logging
import uvclight
from grokcore.component import provider
from fanstatic import Library, Resource
from nva.psyquizz.models.interfaces import IQuizzSecurity
from grokcore.component import context, Subscription
from zope.interface import Interface, implementer
from uvclight.utils import current_principal
from nva.psyquizz.browser.forms import CreateCourse
from nva.psyquizz.models.interfaces import MySimpleTerm

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from nva.psyquizz.models.quizz.corona_set import IHomeOfficeQuestions
from uvc.themes.btwidgets import IBootstrapRequest


class IETEMTheme(IBootstrapRequest):
     pass


library = Library('psyquizz.bgetem', 'static')
bgetemcss = Resource(library, 'bgetem.css')
condition_js = Resource(library, 'conditions.js')

def get_template(name):
    return uvclight.get_template(name, __file__)


@implementer(IQuizzSecurity)
class SecurityCheck(Subscription):
    context(Interface)

    def check(self, name, quizz, context):
        if name == 'quizz3' or name == 'quizz5':
            principal = current_principal()
            if (principal.id.endswith('bgetem.de') or
                principal.id.endswith("novareto.de") or
                principal.id.endswith("sw-i.de") or
                principal.id.endswith("bayernwerk.de") or
                principal.id.endswith("neymanns.thomas@bgetem.de")):
                return True
            return False
        return True




@provider(IContextSourceBinder)
def source_fixed_extra_questions(context):
    #rc = [MySimpleTerm('1', '1', u'Corona', ICoronaQuestions), MySimpleTerm('2', '2', u'Homeoffice', IHomeOfficeQuestions)]
    rc = [MySimpleTerm('2', '2', u'Homeoffice', IHomeOfficeQuestions),]
    return SimpleVocabulary(rc)

#CreateCourse.fields['quizz_type'].source = source_fixed_extra_questions 
from nva.psyquizz.models.interfaces import ICourse, deferred_vocabularies
deferred_vocabularies['fixed_extra_questions'] = source_fixed_extra_questions
from zope.schema.vocabulary import SimpleTerm
from nva.psyquizz.models.vocabularies import make_vocabulary


FREQUENCY = make_vocabulary('frequency_corona', [
    SimpleTerm(value=u'kein Homeoffice',
               title=u'kein Homeoffice'),
    SimpleTerm(value=u'trifft gar nicht zu',
               title=u'trifft gar nicht zu'),
    SimpleTerm(value=u'trifft wenig zu',
               title=u'trifft wenig zu'),
    SimpleTerm(value=u'trifft mittelmäßig zu',
               title=u'trifft mittelmäßig zu'),
    SimpleTerm(value=u'trifft überwiegend zu',
               title=u'trifft überwiegend zu'),
    SimpleTerm(value=u'trifft völlig zu',
               title=u'trifft völlig zu'),
    ])


deferred_vocabularies['frequency_corona'] = FREQUENCY
from nva.psyquizz.browser.forms import CreateAccount
from . import condition_js

class CreateAccount(CreateAccount):
    uvclight.layer(IETEMTheme)

    def update(self):
        self.fields['accept'].title = u"Bitte bestätigen Sie, dass Ihr Unternehmen bei der BG ETEM versichert ist:"
        super(CreateAccount, self).update()
        condition_js.need()


ICourse['quizz_type'].description = u""
