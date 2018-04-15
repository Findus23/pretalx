import random
from abc import ABCMeta

from django.utils.translation import ugettext as _

_phrase_book = dict()


class PhrasesMetaClass(ABCMeta):

    def __new__(mcls, class_name, bases, namespace, app):
        new = super().__new__(mcls, class_name, bases, namespace)
        _phrase_book[app] = new()
        return new

    def __init__(self, *args, app, **kwargs):
        super().__init__(*args, **kwargs)


class Phrases(metaclass=PhrasesMetaClass, app=''):

    def __getattribute__(self, attribute):
        ret = super().__getattribute__(attribute)
        if isinstance(ret, (list, tuple)):
            return random.choice(ret)
        return ret


class PhraseBook:

    def __getattribute__(self, attribute):
        return _phrase_book.get(attribute)


phrases = PhraseBook()


class BasePhrases(Phrases, app='base'):
    """
    This class contains base phrases that are guaranteed to remain the same (i.e., are not
    randomly chosen). They are still provided as a list to make it possible to combine them
    with new phrases in other classes.
    """
    send = [_('Send')]
    save = [_('Save')]
    cancel = [_('Cancel')]
    edit = [_('Edit')]

    saved = [_('Your changes have been saved.')]

    error_sending_mail = [_('There was an error sending the mail. Please try again later.')]
    error_saving_changes = [_('Huh. We had trouble saving your input – Please see below for details. 🠯')]
    error_permissions_action = [_('You do not have permission to perform this action.')]

    permission_denied = [
        _('Permission denied.'),
        _('Sorry, you do not have the required permissions to access this page.'),
        _('Access denied.'),
    ]
    not_found = [
        _('Page not found.'),
        _('This page does not exist.'),
        _('Huh, I could have sworn there was something here.'),
        _(''),
        _('This page is no more.'),
        _('This page has ceased to be.'),
        _('Huh.'),
    ]
    internal_error = [
        _('Internal server error.'),
        _('Internal error, sorry.'),
        _('Internal server error, we\'ve informed the maintenance robot.'),
        _(''),
        _('Ouch, this page is broken.'),
        _('This shouldn\'t happen, sorry. We\'re looking into it.'),
        _('Huh. This seems broken. Please try again later.'),
        _('This seems broken. We\'re looking into it, please give us a bit.'),
        _('It\'s a bug, not a feature. We\'re looking into it.'),
    ]
