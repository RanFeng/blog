# 常用git命令

## 初始操作

**Git global setup**

```
git config --global user.name "aijialei"
git config --global user.email "3287967219@zju.edu.cn"
```

**Create a new repository**

```
git clone http://10.214.150.55/aijialei/foot.git
cd foot
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

**Existing folder**

```
cd existing_folder
git init
git remote add origin http://10.214.150.55/aijialei/foot.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

**Existing Git repository**

```
cd existing_repo
git remote rename origin old-origin
git remote add origin http://10.214.150.55/aijialei/foot.git
git push -u origin --all
git push -u origin --tags
```

## 分支操作

1. git branch 创建分支
2. git branch -b 创建并切换到新建的分支上
3. git checkout 切换分支
4. git branch 查看分支列表
5. git branch -v 查看所有分支的最后一次操作
6. git branch -vv 查看当前分支
7. git brabch -b 分支名 origin/分支名 创建远程分支到本地
8. git branch --merged 查看别的分支和当前分支合并过的分支
9. git branch --no-merged 查看未与当前分支合并的分支
10. git branch -d 分支名 删除本地分支
11. git branch -D 分支名 强行删除分支
12. git branch origin :分支名 删除远处仓库分支
13. git merge 分支名 合并分支到当前分支上

## 暂存操作

1. git stash 暂存当前修改
2. git stash apply 恢复最近的一次暂存
3. git stash pop 恢复暂存并删除暂存记录
4. git stash list 查看暂存列表
5. git stash drop 暂存名(例：stash@{0}) 移除某次暂存
6. git stash clear 清除暂存

## 回退操作

1. git reset --hard HEAD^ 回退到上一个版本
2. git reset --hard ahdhs1(commit\_id) 回退到某个版本
3. git checkout -- file撤销修改的文件(如果文件加入到了暂存区，则回退到暂存区的，如果文件加入到了版本库，则还原至加入版本库之后的状态)
4. git reset HEAD file 撤回暂存区的文件修改到工作区

## 标签操作

1. git tag 标签名 添加标签(默认对当前版本)
2. git tag 标签名 commit\_id 对某一提交记录打标签
3. git tag -a 标签名 -m '描述' 创建新标签并增加备注
4. git tag 列出所有标签列表
5. git show 标签名 查看标签信息
6. git tag -d 标签名 删除本地标签
7. git push origin 标签名 推送标签到远程仓库
8. git push origin --tags 推送所有标签到远程仓库
9. git push origin :refs/tags/标签名 从远程仓库中删除标签

## 常规操作

1. git push origin test 推送本地分支到远程仓库
2. git rm -r --cached 文件/文件夹名字 取消文件被版本控制
3. git reflog 获取执行过的命令
4. git log --graph 查看分支合并图
5. git merge --no-ff -m '合并描述' 分支名 不使用Fast forward方式合并，采用这种方式合并可以看到合并记录
6. git check-ignore -v 文件名 查看忽略规则
7. git add -f 文件名 强制将文件提交

### git创建项目仓库

1. git init 初始化
2. git remote add origin url 关联远程仓库
3. git pull
4. git fetch 获取远程仓库中所有的分支到本地

### 忽略已加入到版本库中的文件

1. git update-index --assume-unchanged file 忽略单个文件
2. git rm -r --cached 文件/文件夹名字 (. 忽略全部文件)

### 取消忽略文件

1. git update-index --no-assume-unchanged file

### 拉取、上传免密码

1. git config --global credential.helper store

## gitignore

在使用git的时候我们有时候需要忽略一些文件或者文件夹。我们一般在仓库的根目录创建.gitignore文件

在提交之前，修改.gitignore文件，添加需要忽略的文件。然后再做add commit push 等

但是有时在使用过称中，需要对.gitignore文件进行再次的修改。这次我们需要清除一下缓存cache，才能是.gitignore 生效。

具体做法：

```
git rm -r --cached . # 清除缓存 
git add . # 重新trace file 
git commit -m "update .gitignore" #提交和注释 
git push origin master #可选，如果需要同步到remote上的话
```

这样就能够使修改后的.gitignore生效。
