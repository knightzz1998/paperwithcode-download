#! /usr/bin/env python
# -*-coding:utf-8-*-

import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import time


async def main():
    cookies = json.loads(open("cookie.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies, proxy="http://localhost:4780")

    prompt = "please help me summarize this article, the address is " \
             "https://arxiv.org/pdf/2306.08967v1.pdf, and summarize according to the following ideas: " \
             "what method is proposed in this article, what technology is used (please combine the specific tasks in " \
             "the method part, describe the information flow, and on what task, it is realized What performance (" \
             "please combine the experimental part, list the key and specific performance indicators, do not make " \
             "up), what are the advantages of their solution compared with the previous solution, what problems can " \
             "not be solved by the previous method, and what problems still exist in this method ? Answer me in Chinese"
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative,
                             simplify_response=True, locale='zh-CN')
    print(json.dumps(response, indent=2))
    time.sleep(5)
    await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
