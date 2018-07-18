# -*- coding: utf-8 -*-

from main.core.api.main import Main

def test_main():
	m = Main("handled")
	print(m.sprint())
	assert 2 == 2
	assert m.sprint() == "handled"
	
