#!/usr/bin/env python3
# Copyright (C) 2021 ArjanCodes <https://github.com/ArjanCodes>
# Copyright (C) 2018 Endemoniada <https://github.com/Endemoniada>
#
# SPDX-License-Identifier: MIT

from abc import ABC, abstractmethod

from hand import Hand


class Rule(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def points(self, hand: Hand):
        pass

class SameValueRule(Rule):
    def __init__(self, value: int, name: str):
        self.__value = value
        self.__name = name

    def name(self):
        return self.__name

    def points(self, hand: Hand):
        return hand.count(self.__value) * self.__value

