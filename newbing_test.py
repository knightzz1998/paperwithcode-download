#! /usr/bin/env python
# -*-coding:utf-8-*-

import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import time

prompt2 = "请帮我总结这篇文章 {}，按照下面的思路总结：这篇文章提出了什么方法，利用了什么技术（请结合method" \
          "部分的具体任务，描述信息流，在什么任务上，实现了什么性能（请结合实验部分，列举出关键且具体的性能指标，不要编造），" \
          "他们的方案相比过去的方案有哪些优势，解决了什么过去的方法解决不了的问题，这个方法还存在什么问题？**用中文回答我**"
prompt = "please help me summarize this article {}, i will send my paper url, and summarize according to the " \
         "following ideas: what method is proposed in this article, what technology is used (please combine the " \
         "specific tasks in the method part, describe the information flow, and on what task, it is realized What " \
         "performance (please combine the experimental part, list the key and specific performance indicators, " \
         "do not make up), what are the advantages of their solution compared with the previous solution, " \
         "what problems can not be solved by the previous method, and what problems still exist in this method ? " \
         "Answer me in Chinese"


async def init():
    global bot
    cookies = json.loads(open("cookie.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies, proxy="http://localhost:4780")
    print("create GPT success !")


async def get_ask(url):
    question = prompt.format(url)
    response = await bot.ask(prompt=question, conversation_style=ConversationStyle.creative,
                             simplify_response=True, locale='zh-CN')
    print(response['text'])
    return response['text']


async def close():
    await bot.close()


if __name__ == '__main__':
    # asyncio.run(main())
    urls = ['https://arxiv.org/pdf/2305.17310v1.pdf', 'https://arxiv.org/pdf/2305.13656v1.pdf']
    for url in urls:
        print(prompt.format(url))
        asyncio.run(init())
        result = asyncio.run(get_ask(url))
        print(result)

    asyncio.run(close())
