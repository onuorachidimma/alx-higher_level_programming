#!/usr/bin/bash
word = open("sentence.txt", "w")
word.write("and that piece of art is useful - Dora Korpar, 2015-10-19\n")
word.close()
word = open("sentence.txt", "r")
