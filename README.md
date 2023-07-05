## 项目介绍

:sparkles: 本项目是用于批量下载 PaperWithCode 网站上的文章、代码, 并将相关内容写入到word文档

## 依赖下载

```shell
pip install openpyxl 
pip install python-docx

```

## 参考

- docx : https://python-docx.readthedocs.io/en/latest/index.html

## QA

### 关于翻译

翻译使用的是百度AI, 需要自己去申请
地址 : https://fanyi-api.baidu.com/api/trans/product/desktop?fr=pcHeader

需要 APP ID：xxxx
密钥：xxxx

## 关于文章的下载地址

默认下载到当前 main 文件的路径

需要修改 download_file.py 文件的 BASE_LOCAL 属性


### EdgeGPT

建议使用 0.10.16版本 具体原因参考以下 issue

https://github.com/acheong08/EdgeGPT/issues/584