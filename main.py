import discord

client = discord.Client()
token = "MTE1OTg0NDEwNzAzMjczNTc0NQ.GmtM2x.2JCzoW9bwcnbptbMydzsV5clInQvMWQo1azg6k"  # Токен


@client.event
async def on_ready():
    print(f'Залогинился под именем {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:  # Чтобы не реагировать на сообщения бота
        return  # Ничего не делаем

    if message.content == 'ping':
        await message.channel.send('pong')

    if message.content.startswith('$Привет'):
        await message.channel.send('Привет, друг!')

    if check_caps(message.content):
        reason = 'Злоупотребление CAPS LOCK'
        # await message.channel.purge(limit=1)  # Удаляем последнее сообщение
        await message.author.send(f'Вы были выгнаны по причине: {reason}')
        # await message.author.ban(reason='reason')  # Баним пользователя
        emb = make_ban_embed(message.author, reason)  # Получаем рамку
        await message.channel.send(embed=emb)  # Выводим на экран рамку


def check_caps(text):  # Функция определения CAPS LOCK
    if len(text) < 6:  # Если длина текста меньше 6 символов
        return False  # то ничего не делаем.
    count = 0  # Счетчик количества больших букв
    for i in text:  # Цикл перебора букв в сообщении
        if i.isupper():  # Если найдена большая буква
            count += 1  # Увеличиваем счетчик на 1
    return count > len(text) // 4 * 3  # Если букв больше, чем 75% текста


def make_ban_embed(author, reason):
    emb = discord.Embed(title='Нарушение правил чата', colour=discord.Color.red())
    emb.set_author(name=author.name, icon_url=author.avatar_url)
    emb.add_field(name='Бан пользователя', value=f'Пользователь {author.mention} был забанен')
    emb.set_footer(text=f'Причина бана: {reason}')
    return emb


client.run(token)
