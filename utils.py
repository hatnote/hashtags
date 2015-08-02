# -*- coding: utf-8 -*-

import re

# TODO: add allowed starting punctuation
# From boltons
HASHTAG_RE = re.compile(r"(?:^|\s)[＃#]{1}(\w+)", re.UNICODE)
MENTION_RE = re.compile(r"(?:^|\s)[＠@]{1}([^\s#<>[\]|{}]+)", re.UNICODE)


def find_hashtags(string):
    """Finds and returns all hashtags in a string, with the hashmark
    removed. Supports full-width hashmarks for Asian languages and
    does not false-positive on URL anchors.
    >>> find_hashtags('#atag http://asite/#ananchor')
    ['atag']
    ``find_hashtags`` also works with unicode hashtags.
    """

    # the following works, doctest just struggles with it
    # >>> find_hashtags(u"can't get enough of that dignity chicken #肯德基 woo")
    # [u'\u80af\u5fb7\u57fa']
    return HASHTAG_RE.findall(string)


def find_mentions(string):
    return MENTION_RE.findall(string)
