import confing as cf
import aiogram as aio
token = cf.token
tgbot = aio.Bot(token)
dp = aio.Dispatcher(tgbot)

@dp.message_handler(commands = ['bb'])
async def send_welcome(message: aio.types.Message):
    await message.reply("Hello")

# @dp.message_handler(comands = [''])
# async def send_welcome(message = aio.types.Message):
#     await message.reply("Hello")
#
@dp.message_handler(commands = ['start'])
async def send_welcome(message: aio.types.Message):
    await message.reply("Hello")




if __name__ == '__main__':
    aio.executor.start_polling(dp, skip_updates = True)


























