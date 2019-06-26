import discord
import asyncio
import ditto_backend

class Ditto:

    def __init__(self, client):
        self._client = client
        self.blurple = 0x7289DA

    def check_file_type(self, message):
        """
        Usage: Determines if a message includes a file

        Parameters:
            message (Discord.py message object)

        Returns:
            True if message includes a file; False otherwise
        """

        return len(message.attachments)>0

    def check_for_ditto_react(self, reaction):
        """
        Usage: Checks if the reaction to a post with an attachment is :ditto:

        Parameters:
            reaction (Discord.py reaction object)

        Returns:
            True if the reaction is :ditto:; False otherwise
        """

        ditto_emoji = discord.utils.get(reaction.message.server.emojis, name="ditto")
        ditto_emoji=(str(ditto_emoji)[1:8])
        return ditto_emoji == ':ditto:'

    def start_query(self, command, author_id, file_url):
        ''' Placeholder method for Drey code '''

        pass

    async def on_ditto_react(self, message):
        """
        Usage: When a user reacts to a file with :ditto:, get (or create) the user's directory path,
        and save file to a library or create a new library based on user response

        Parameters:
            message (Discord.py message object)
        """

        user_path = ditto_backend.get_user_dir_path(message.author.id)
        libs = ditto_backend.get_user_libs(message.author.id)
        title = message.author.display_name + '\'s Libraries'
        desc = ''
        for index, lib in enumerate(libs):
            desc += '{}. {}\n'.format(index+1, lib)
        desc += '**$newLibrary** <library name>'
        em = discord.Embed(description=desc, title = title, color = self.blurple)

        await self._client.send_message(message.channel, ('`{}`, what library do you want to save this photo in?'.format(message.author.display_name)))
        await self._client.send_message(message.channel, embed = em)
        response = await self._client.wait_for_message(author=message.author)
        if '$newLibrary' in response.content:
            await self.new_library(response)
        elif response.content in libs:
            lib = response.content.strip()
            await self.add_to_library(message, lib)
        else:
            await self._client.send_message(message.channel, 'That library doesn\'t exist. Use `$newLibrary <library name>` to create a new library.')
            response = await self._client.wait_for_message(author=message.author)
            lib = response.content.strip()
            if lib in libs:
                await self.add_to_library(message, lib)
            else:
                await self.new_library(response)


    async def new_library(self, message):
        """
        Usage: Upon user command `$newLibrary`, checks if user has supplied a name for new library;
        Creates a library if so, otherwise prompts for a library name

        Parameters:
            message (Discord.py message object)
        """

        if message.content.startswith('$newLibrary'):
            if len(message.content.split()) > 1:
                new_lib = message.content.split(' ', 1)[1]
                ditto_backend.create_lib(message.author.id, new_lib)
                await self._client.send_message(message.channel, ('New library `' + new_lib +'` has been created for `{}`'.format(message.author.display_name)))
            else:
                await self._client.send_message(message.channel, ('Please provide a name for your new library using `$newLibrary <library name>`'))
                response = await self._client.wait_for_message(author=message.author)
                await self.new_library(response)
        else:
            await self._client.send_message(message.channel, ('Please provide a name for your new library using `$newLibrary <library name>`'))
            response = await self._client.wait_for_message(author=message.author)
            await self.new_library(response)

    async def delete_library(self, message):
        """
        Usage: Upon user command `$deleteLibrary` and confirmation, deletes an entire library

        Parameters:
            message (Discord.py message object)
        """

        if len(message.content.split()) > 1:
            lib_to_del = message.content.split(' ', 1)[1]
            if self.check_for_library(message.author.id, lib_to_del):
                await self._client.send_message(message.channel, ('Are you sure you want to delete the entire library `{}`? Type `yes` to delete'.format(lib_to_del)))
                response = await self._client.wait_for_message(author=message.author)
                if response.content.lower().strip() == 'yes':
                    self.start_query('delete_lib', message.author.id, lib_to_del)
                    await self._client.send_message(message.channel, ('Library `{}` has been deleted.'.format(lib_to_del)))
            else:
                await self._client.send_message(message.channel, 'That library does not exist.')

        else:
            await self._client.send_message(message.channel, ('Please provide a name for the library you want to delete using `$deleteLibrary <library name>`.'))

    async def add_to_library(self, message, lib):
        """
        Usage: Adds the file the user reacted to to an existing library

        Parameters:
            message (Discord.py message object): the message that contains the file
            lib (str): library name to add file to
        """
        self.start_query('add_to_lib', message.author.id, message.attachments[0].get("url")) # send lib here too
        await self._client.send_message(message.channel, 'File added to library `' + lib +'`!')

    def check_for_library(self, user, lib):
        """
        Usage: Checks if a provided library name exists for that user

        Parameters:
            user (int or str): the unique token for the user provided by Discord.py
            lib (str): the name of the library to look for

        Returns:
            True if library exists; False otherwise
        """

        user_libs = ditto_backend.get_user_libs(user)
        return lib in user_libs

    async def share_library(self, message):
        """
        Usage: Upon user command `$Library <library name>`, returns a library to message channel;
        Left and right arrow reactions allow the user to flip through files

        Parameters:
            message (Discord.py message object)
        """

        if len(message.content.split()) > 1:
            lib = message.content.split(' ', 1)[1]
            self.start_query('get_lib', message.author.id, lib)
            await self._client.send_message(message.channel, 'Here is a placeholder that will be your library')
        else:
            await self._client.send_message(message.channel, ('Please provide a library name using `$Library <library name>`'))
            message = await self._client.wait_for_message(author=message.author)
            if message.content.startswith('$Library'):
                await self.share_library(message)

    async def list_libraries(self, message):
        """
        Usage: Upon user command `$myLibraries`, returns a list of the users current libraries to message channel

        Parameters:
            message (Discord.py message object)
        """

        libs = ditto_backend.get_user_libs(message.author.id)

        title = message.author.display_name + '\'s Libraries'
        desc = ''
        for index, lib in enumerate(libs):
            desc += '{}. {}\n'.format(index+1, lib)
        em = discord.Embed(description=desc, title = title, color = self.blurple)

        await self._client.send_message(message.channel, embed = em)

    def surprise(self, message):
        """
        Usage: Upon user command `$surpriseMe`, returns a randomly chosen photo from any of the user's libraries to message channel

        Parameters:
            message (Discord.py message object)
        """
        pass

    async def help_msg(self, message):
        """
        Usage: Upon user command `$help`, returns a help message with bot functionality to message channel

        Parameters: message (Discord.py message object)
        """

        await self._client.send_message(message.channel, 'Hey I\'m Ditto, your media squire for Discord! Here\'s some things I can do for you:')
        em = discord.Embed(color = self.blurple)
        em.add_field(name = ':ditto:', value = 'React to a file with `:ditto:` to save it to a library', inline=False)
        em.add_field(name = '$myLibraries', value = 'View a list of your current libraries', inline=False)
        em.add_field(name = '$Library <library name>', value = 'View a library', inline=False)
        em.add_field(name = '$deleteLibrary <library name>', value = 'Delete a library', inline=False)
        em.add_field(name = '$surpriseMe', value = 'Pick a photo at random', inline=False)
        await self._client.send_message(message.channel, embed=em)






