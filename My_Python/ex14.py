from sys import argv

script, user_name = argv
prompt = '>'

print ("Hi %s, this is %s script", user_name, script)
print ("I would like to ask you a few questions;")

print ("Do you like me %s", user_name)
likes = input(prompt)

print ("May i know where do you live?", lives)
lives = input(prompt)

print ("May I know what kind of / type of a computer you are using?")
computer = input(prompt)

print ("""Alright, so you have told that %r about liking me
	you live in %r. Not sure where that is.
	And you have a %r computer. Nice""", %likes, %lives,computer)
