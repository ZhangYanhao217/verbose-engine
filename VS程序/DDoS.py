import concurrent.futures
import aiohttp
import asyncio

URL = input("URL:")
S = int(input("S:"))
N = int(input("N:"))  # 每次发送的信息量（以字符数或字节数为单位）

async def run(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}) as response:
            # 处理请求结果，例如获取状态码
            # print('状态码:', response.status)

async def main():
    # 使用线程池来管理线程
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 创建协程任务列表
        coroutines = []
        for _ in range(S):
            # 构造每次发送的信息
            data = {
                'key1': 'value1',
                'key2': 'value2',
                # ...
            }
            # 将信息添加到协程任务列表
            coroutines.append(run(URL, data))
        # 执行协程任务
        results = await asyncio.gather(*coroutines)

# 运行主函数
asyncio.run(main())
