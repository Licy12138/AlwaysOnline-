# -*- coding: utf-8 -*-

import asyncio
import logging
import socks
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.functions.messages import ReadHistoryRequest
from telethon.tl.types import InputPeerChat
from data import delay

# 配置日志记录，关闭调试信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 设置 Telethon 的日志级别为 WARNING，关闭 DEBUG 信息
logging.getLogger('telethon').setLevel(logging.WARNING)

proxy = (socks.SOCKS5, '127.0.0.1', 7890)

async def main():
    logging.info("Trying to Login to Telegram... 正在尝试登录...")
    
    try:
        await client.connect()  # 确保连接到 Telegram
    except Exception as e:
        logging.error(f"连接失败: {e}")
        return

    if await client.is_user_authorized():
        logging.info("You are now AlwaysOnline™, Yah! | 状态已更新为在线。")
        try:
            # 群组 ID 列表
            chat_ids = [123456789,123456789]  # 添加多个群组 ID，如果你不知道怎么获取，请运行hash.py

            while True:
                await client(UpdateStatusRequest(offline=False))
                logging.info("状态已更新为在线。")
                
                for chat_id in chat_ids:
                    # 获取群聊实体
                    chat_entity = InputPeerChat(chat_id)
                    
                    # 获取对话信息
                    dialog = await client.get_dialogs()
                    
                    # 查找特定对话
                    for d in dialog:
                        if d.id == chat_id:
                            unread_count = d.unread_count
                            break
                    else:
                        unread_count = 0
                    
                    # 标记未读消息为已读
                    await client(ReadHistoryRequest(peer=chat_entity, max_id=0))
                    logging.info(f"群组 {chat_id} 的 {unread_count} 条未读消息已标记为已读。")
                
                await asyncio.sleep(delay)
        except Exception as e:
            logging.error(f"更新状态或标记消息失败: {e}")
    else:
        logging.fatal("Login Fails, please retry... | 失败，请重试！")

if __name__ == '__main__':
    asyncio.run(main())
