#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import builtins
except ImportError:
    import __builtin__ as builtins
import public
import values


def _isdict(obj):
    return isinstance(obj, dict)


@public.add
class dict(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def get(self, key=None, default=None, i=False):
        result = builtins.dict.get(self, key, default)
        if result is None and i is True:  # insensitive
            for k in self.keys():
                if str(key).lower() == str(k).lower():
                    return self[k]
        return result

    def update(self, *args, **kwargs):
        builtins.dict.update(self, *args, **kwargs)
        return self

    def remove(self, v):
        """remove element(s) by key"""
        for key in values.get(v):
            if key in self:
                self.pop(key)
        return self

    def __getattribute__(self, name):
        if hasattr(type(self), name):
            return object.__getattribute__(self, name)
        if name in self:
            if isinstance(self[name], dict):  # dict
                return dict(self[name])
            return self[name]

    def __getitem__(self, key):
        if key in self:
            v = builtins.dict.__getitem__(self, key)
            if _isdict(v):  # recirsive
                return type(self)(v)
            return v

    def __setattr__(self, name, value):
        if hasattr(type(self), name):
            object.__setattr__(self, name, value)
        else:
            self[name] = value
