from telethon import TelegramClient

# 替换为你的 API ID 和 API Hash
api_id = ''
api_hash = ''
phone_number = ''

# 创建客户端
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    # 获取你加入的所有对话
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group:
            group = dialog.entity
            # 检查 group 类型并获取属性
            access_hash = getattr(group, 'access_hash', '无')
            print(f'群组名称: {group.title}, 群组 ID: {group.id}, ACCESS_HASH: {access_hash}')

with client:
    client.loop.run_until_complete(main())
