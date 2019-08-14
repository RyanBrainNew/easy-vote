练习使用python脚本重复刷票的脚本
对应投票网站地址如下http://jiayin.v.vote8.cn/m?OptionSearchTopicID=2890797&OptionSearchKeyword=90&from=timeline

1.新建的项目
git init

2.git add .
git commit -m 'first commit' //''中是备注信息

3.提交完成后，需要将远程仓库与本地仓库同步连接，还记得在GitHub创建仓库时让你注意的链接吗？那就是远程仓库的地址，复制它。（这一步只需要在你第一次提交项目的时候进行，后面如果你还是使用这个仓库提交到同一个远程仓库的话，就不需再进行一次同步连接了）

git remote add origin 粘贴你自己的链接

4.最后一步将本地仓库的内容推送到远程仓库：

git push -u origin master