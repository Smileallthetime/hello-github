#学习日志
---

## 2026-09-11 · 第一次用 Git 和 GitHub

**今天做了什么**

- 注册了 GitHub 账号

- 配置好了 Git 的身份，学会了第一次 `commit`

- 把练习仓库推到了 GitHub 上


**卡住的地方**

- 网络报错，github.com连不上，是DNS给的IP被阻断，让deepseek harness换个IP就通了

- 第一次上传git add后面没有加 . 

- git commit -m 说明  这条后面应该用""把说明括起来


**搞懂了什么**

-工作区 你改的文件→git add .→暂存区 待提交篮子→git commit -m "说明"→本地仓库 在自己电脑中→git push→GitHub 云端网站
                                                                                                                                                                           ←git pull  ←

-`cd 文件夹路径`   进入某个文件夹 —— 每个新窗口的第一步

-`git add .`   把改动放进待提交的篮子 —— 准备存档之前

-`git commit -m "说明"`   在你电脑上存一个版本快照 —— 写完一段能跑的代码

-`git push`   把快照上传到 GitHub —— 一天结束时

-`git status`   看完现在改了什么、什么状态 —— 迷茫可以敲一下

-add 后面必须有空格，再跟 .

-commit -m 后面用英文双引号把说明包起来。养成习惯，以后说明里有空格也不会出问题

-还有一些

git pull	把 GitHub 上的最新版拉回本地	换电脑、和别人协作前

git log --oneline	列出所有存档点	回顾历史、准备回退

git restore 文件名	把文件恢复到上次存档的状态	改坏了要救命时

git clone 网址	把别人的项目整个复制到本地	下载别人的代码来学习

git init	把普通文件夹变成 Git 仓库	自己从零开一个新项目

git config --global	配置你的名字和邮箱	一台新电脑只做一次


**下次想搞明白**

- 分支（branch）到底是干嘛的，什么时候需要它（deepseek生成的）
