#!/usr/bin/env python
""""
File             : messaging.py
Author           : ian
Created          : 07-08-2016

Last Modified By : ian
Last Modified On : 07-08-2016
***********************************************************************
The MIT License (MIT)
Copyright © 2016 Ian Cooper <ian_hammond_cooper@yahoo.co.uk>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
***********************************************************************
"""

import uuid
from abc import ABCMeta, abstractmethod


class Message:
    def __init__(self) -> None:
        self._id = uuid.uuid4()

    @property
    def id(self) -> uuid:
        return self._id


class MessageMapper:
    pass


class MessageStore(metaclass=ABCMeta):
    @abstractmethod
    def add(self, message: Message):
        pass

    @abstractmethod
    def get_message(self, key: uuid):
        pass


class Producer(metaclass=ABCMeta):
    @abstractmethod
    def send(self, message: Message):
        pass

