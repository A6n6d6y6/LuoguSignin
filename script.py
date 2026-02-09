# coding=utf-8

import requests,json,sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def punch(cookie):
	res=requests.get('https://www.luogu.com.cn/index/ajax_punch',headers={
		'accept':'*/*',
		'accept-encoding':'gzip,deflate,br',
		'accept-language':'zh-CN,zh;q=0.9',
		'content-length':'0',
		'cookie':cookie,
		'origin':'https://www.luogu.com.cn',
		'referer':'https://www.luogu.com.cn/',
		'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
		'x-csrf-token':'1530786066:F3dU7fTlJSTWKNA9XMdI76gdJGRdkxQqxafCS4PgGw8=',
		'x-requested-with':'XMLHttpRequest'
	})
	res.encoding=res.apparent_encoding
	return res.text

if __name__=="__main__":
	for i in range(1,len(sys.argv)):
		print(f"Cookie:{sys.argv[i]}")
		response=punch(sys.argv[i])
		print(response)
		try:
			tmp=json.loads(response)
			if tmp['code']==200:
				print('code=',tmp['code'],'message =',tmp['more']['html'])
			else:
				print('code=',tmp['code'],'message =',tmp['message'])
		except Exception as err:
			print(f"<{err}>")
