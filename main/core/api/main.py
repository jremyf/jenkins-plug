# -*- coding: utf-8 -*-

from expiringdict import ExpiringDict
import six

class Main:

	def __init__(self, toprint):
		self.value=toprint

	def sprint(self):
		return self.value
