# login.py
# -*- coding: utf-8 -*-

from telethon import TelegramClient
from data import api_id, api_hash
import logging
import asyncio

# 配置日志记录
logging.basicConfig(level=logging.DEBUG)

if api_id == '' or api_hash == '':
    logging.fatal("你必须填入你的API，请在data.py配置")
    exit(1)

# 初始化客户端
client = TelegramClient('session_file', api_id, api_hash)

async def main():
    logging.info("尝试登录Telegram Web...")

    try:
        await client.connect()
    except Exception as e:
        logging.error(f"连接失败: {e}")
        return

    if not await client.is_user_authorized():
        logging.info('您还没有登录，正在尝试登录…')

        # 要求输入手机号码
        phone_number = input("请输入您的手机号码（包括国家代码，如 +8613800138000）: ")
        
        try:
            await client.send_code_request(phone_number)
            code = input("请输入您收到的验证码: ")
            
            await client.sign_in(phone_number, code)
            logging.info("登录成功！")
        except Exception as e:
            logging.error(f"登录失败: {e}")
    else:
        logging.info("您已经登录！")

if __name__ == '__main__':
    asyncio.run(main())
