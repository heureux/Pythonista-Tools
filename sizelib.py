#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Size (object):
    _SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    }
    
    def __init__(self, digit = 1, is_human_readable = True):
        self.digit = '{0:.' + str(digit) + 'f} {1}'
        self.is_human_readable = is_human_readable
    
    
    def calc(self, size, is_human_readable = True):
        if size < 0: return 0
        suf = 1000 if self.is_human_readable and is_human_readable else 1024
        for suffix in self._SUFFIXES[suf]:
            size /= suf
            if size < suf:
                return self.digit.format(size, suffix)
        b = '2^80' if self.is_human_readable and is_human_readable else '10^24'
        raise ValueError(size + ' is size over')
