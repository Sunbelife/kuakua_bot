import requests
from wxpy import *

bot = Bot()

# API 申请白名单是免费的，直接去 nmsl.shadiao.app 申请即可。
kuakua_url = "https://chp.shadiao.app/api.php?from=sunbelife"
maren_url = "https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn&from=sunbelife"

# 只有名单里的夸
def is_kua(name):
	
	kuas = ['胖鱼', "苦逼"]
	
	for i in kuas:
		if i in name:
			return True
	# 如果你想让名单生效，就把这里改成 False
	return True

# 打印所有*群聊*对象中的*文本*消息
@bot.register(Group, TEXT)
def print_group_msg(msg):
	# 如果是群聊，但没有被 @，则不回复
	if isinstance(msg.chat, Group) and not msg.is_at:
		return
	else:
		kuakua = requests.get(kuakua_url)
		mama = requests.get(maren_url)
		
		print(msg.raw)
		
		if is_kua(msg.raw['ActualNickName']):
			text = kuakua.text
		else:
			text = mama.text
			
		return '@{} {}'.format(msg.raw['ActualNickName'], text)
		
# 堵塞线程，并进入 Python 命令行
embed()