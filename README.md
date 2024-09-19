# AlwaysOnline™

Keep your Telegram Always Online.
让你的 Telegram 永远"在线"

使用了开源项目 - Many Thanks to project: https://github.com/LonamiWebs/Telethon/

# 背景

Don't let others peak on your daily routine with recent online! So keep yourself always online. XD  
如果你不想被人通过在线时间判断作息规律，那就让自己一直保持在线吧！  
（这样子就算你让所有人看见你的在线时间也无所谓咯，同时你还可以看到别人的）  

# 需求 Prerequisite

`PYTHON3`  
`一台可以连接到Telegram的服务器`  

需要包：`Telethon`  `PySocks`
使用这个指令直接安装到全局 | Install package globally with ：`pip3 install telethon==0.19.1.6` `pip3 install PySocks` 

或是在命令提示符运行 | Used the Windows command prompt type: `python -m pip install telethon==0.19.1.6` `python -m pip install PySocks`  

# 如何使用？ How to use

- 首先，你需要一个 `Client Token`(这个可以在 https://my.telegram.org 申请)
- `git clone https://github.com/NeverBehave/AlwaysOnline-` 或者下载压缩包解压
- 将 `api_id` 和 `api_hash` 填入 `data.py` 适当的位置
    - Fill in your id and hash @ `data.py`
- `python3 main.py`
- 按照指引完成登录
    - Follow the instruction and you are good to go !
- 如果你不知道群组的hash，id，请使用该指令

```log
python hash.py
```

# 提示 Tips

- 不要在**不安全**的地方部署这个脚本，妥善地保管好目录下的`Session`文件，否则相当于给予**任何人访问你的账号的权限** 
    - Take good care of the `session` file under this directory, or your account will be at risk.
- 这个脚本会将特定频道，群组，聊天信息变为已读，你不会在日常使用中察觉到脚本的存在
- 要配置特定频道，请在`main.py`配置
  ```python
              # 群组 ID 列表
            chat_ids = [123456789,123456789]  # 添加多个群组 ID，如果你不知道怎么获取，请运行hash.py
  ```
    - You can still use your account normally. Nothing else will change (Message count, etc.).
     

# 原理 How it works

Send an online status message to Telegram Web periodically. Your actions are not necessary change your online status.  
间歇性的给 Telegram Web 发送你在线的信息，实际上你发送信息并不意味着你上线，只有你主动改变了你的状态  

