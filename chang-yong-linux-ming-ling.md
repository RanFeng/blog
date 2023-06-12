---
description: 常用Linux命令
---

# 常用Linux命令

## 挂载目录

```bash
sudo mount -t cifs -o vers=2.0,username=earisty,password=190120,file_mode=0777,dir_mode=0777,uid=1000,gid=1000 //10.214.150.98/Public 98
```

## 删除挂载点

```bash
sudo umount 98
```

## conda 与 pip

```bash
conda create -n py35 python=3.5

# conda 更换国内镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
conda config --show channels

# pip 更换阿里源
mkdir ~/.pip && cd ~/.pip && (echo "[global]
trusted-host=mirrors.aliyun.com
index-url=https://mirrors.aliyun.com/pypi/simple/" >> pip.conf) && cd -
cat ~/.pip
```

## Linux 局域网共享目录

#### samba

```bash
sudo apt-get install samba
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bak
sudo nano /etc/samba/smb.conf
# 在文件末尾添加
[my share] 
    comment = my share for pc-lint //对共享文件的描述 
    path = / //要共享的路径（此处为根目录） 
    browseable = yes //配置该路径文件可浏览 
    writable = yes //配置可读写（read only为只读） 
    guest ok = yes //配置访客可以访问（也可配置密码）
# 创建Samba用户
sudo smbpasswd -a username
# 重启Samba
sudo /etc/init.d/smbd restart 
# windows下访问 
# win+R输入“\\ip地址”即可访问
```

#### nfs

```bash
# A 机器配置：
sudo nano /etc/exports

#添加：

/home/ajl *(rw,sync,no_root_squash,no_subtree_check)

#在/etc/exports文件内添加映射权限(被映射的目录和可以允许的地址):
#/data/a 192.168.0.222 *(rw,sync,no_root_squash)
#说明：
#允许ip地址范围在192.168.0.222的计算机以读写的权限来访问/data/a 目录。
#rw：读/写权限，只读权限的参数为ro；
#sync：数据同步写入内存和硬盘，也可以使用async，此时数据会先暂存于内存中，而不立即写入硬盘。
#no_root_squash：NFS 服务器共享目录用户的属性，
# 如果用户是 root，那么对于这个共享目录来说就具有root的权限。

sudo /etc/init.d/nfs-kernel-server restart

# B 机器配置：
mkdir /data/a
mount 192.168.1.111:/data/a /data/a

# 取消挂载的命令是 

umount /data/a

# 备注:
# 1. A的相应端口需要释放，确保没有防火墙阻拦
# 2. 有问题时可以用rpcinfo -p server 检查各端口情况，确保nfs服务启动
# 3. 磁盘根目录不能做映射


```

## 后台进程

```bash
python train.py &   # 将进程放在后台执行
ctrl-z              # 暂停当前进程 并放入后台
jobs                # 查看当前后台任务
bg                  # 将任务转为后台执行
fg                  # 将任务调回前台
kill                # 杀掉任务
```

## ps -aux命令显示的状态列

* D 不可中断 Uninterruptible sleep (usually IO)&#x20;
* R 正在运行，或在队列中的进程
* S 处于休眠状态&#x20;
* T 停止或被追踪&#x20;
* Z 僵尸进程&#x20;
* W 进入内存交换（从内核2.6开始无效）&#x20;
* X 死掉的进程&#x20;
* < 高优先级&#x20;
* N 低优先级&#x20;
* L 有些页被锁进内存&#x20;
* s 包含子进程
* \+ 位于后台的进程组
* l 多线程，克隆线程 multi-threaded (using CLONE\_THREAD, like NPTL pthreads do)

## 压缩

```bash
# tar
## 解包：
tar -zxvf FileName.tar
## 打包：
tar -czvf FileName.tar DirName

# .tar.gz 和 .tgz
## 解压：
tar -zxvf FileName.tar.gz
## 压缩：
tar -zcvf FileName.tar.gz DirName
## 压缩多个文件：
tar -zcvf FileName.tar.gz DirName1 DirName2 DirName3 ...

# zip命令
## 解压：
unzip FileName.zip
## 压缩：
zip -r FileName.zip DirName
```

## 文件大小或数量计算

```bash
df -hl # 查看磁盘剩余空间
du -sh filename
# 其实我们经常用du -sh *，显示当前目录下所有的文件及其大小，如果要排序再在后面加上 | sort -n
du -sm * | sort -n # 统计当前目录大小 并按大小 排序
wc [-lmw]
# 参数说明：
# -l :多少行
# -m:多少字符
# -w:多少字
ls | wc -l # 当前文件夹下有多少文件
ls -l | grep "^-" | wc -l # 统计当前目录下文件的个数（不包括目录）
ls -lR | grep "^-" | wc -l # 统计当前目录下文件的个数（包括子目录）
ls -lR | grep "^d" | wc -l # 查看某目录下文件夹(目录)的个数（包括子目录）

```

## git 文件夹下运行命令慢的解决方案：

```bash
git config --add oh-my-zsh.hide-status 1
git config --add oh-my-zsh.hide-dirty 1
```































