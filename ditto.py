import discord
import asyncio

class Ditto:

	def __init__(self, client):
		self._client = client
		#other things

	def check_reaction(self, message):
		''' Start here if user reacts :ditto: on a file '''
		pass


	def check_for_library(self):
		''' Check if user response for library option is valid'''
		pass

	def new_library(self):
		''' $newLibrary - Create new library with $newLibrary command - user inputted library name '''
		pass

	def add_to_library(self):
		''' Add file to existing library '''
		pass

	def check_file_type(self, message):
		''' Determine the file type of a message that has been reacted to (message.attachments)'''
		return len(message.attachments)>0 # returns True if message includes an attachment

	def check_for_ditto_react(self, reaction):
		ditto_emoji = discord.utils.get(reaction.message.server.emojis, name="ditto")
		ditto_emoji=(str(ditto_emoji)[1:8])
		print(ditto_emoji)
		return ditto_emoji == ':ditto:'

	def share_library(self):
		''' $Library <library name> - Returns a library to message channel where left and right arrows can flip through files'''
		pass

	def surprise(self):
		''' $surpriseMe - Returns a randomly chosen photo '''
		pass

