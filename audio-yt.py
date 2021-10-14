#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import pafy

print("Write URL video:")
url = input()

v = pafy.new(url=url)
v_title = v.title

best_audio = v.getbestaudio()
best_audio.download()

print(v.title)
