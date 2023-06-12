# 系统初始设置

## mac

### **在iTerm2中添加以下配置文件快捷键**

```
FOR  ACTION         SEND
⌘←  "SEND HEX CODE" 0x01 
⌘→  "SEND HEX CODE" 0x05
⌥←  "SEND ESC SEQ"  b
⌥→  "SEND ESC SEQ"  f
⌘z  "SEND HEX CODE" 0x1f
```

### 安装 brew&#x20;

参考链接：程序员 Homebrew 使用指北 [https://sspai.com/post/56009](https://sspai.com/post/56009)

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### **使用中科大的镜像**

执行如下命令，即可切换为中科大的镜像

```
cd "$(brew --repo)"
git remote set-url origin git://mirrors.ustc.edu.cn/brew.git
cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin git://mirrors.ustc.edu.cn/homebrew-core.git
```

#### **使用清华大学的镜像**

执行如下命令，即可切换为清华大学的镜像

```
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
```

#### 使用 Brewfile 完成环境迁移

设备永久了，我们的电脑中会有大量的软件，如果你需要迁移环境，重新安装会是一个大麻烦，好在 Homebrew 本身为我们提供了一个非常好用的环境迁移的工具 —— Homebrew Bundle

你首先需要在之前的电脑中执行 `brew bundle dump` 来完成当前环境的导出,导出完成后，你会得到一个 _Brewfile_。

![](<.gitbook/assets/image (2).png>)

然后将 _Brewfile_ 复制到新的电脑中，并执行 `brew bundle` 来开始安装的过程。

![](https://postimg.aliavv.com/mbp/zeq1d.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

#### 安装 GNU 命令工具

所需的 GNU 命令工具，通过`Homebrew`安装，常用命令安装如下:

```
brew install coreutils
brew install findutils
brew install gnu-sed
brew install gnu-indent
brew install gnu-tar
brew install gnu-which
brew install gnutls
brew install grep
brew install gzip
brew install screen
brew install watch
brew install wdiff --with-gettext
brew install wget
brew install less
brew install unzip
```

若要搜索所有 GNU 工具，可以通过以下命令搜索：

```
brew search gnu
```

### 覆盖系统自带命令 <a href="#fu-gai-xi-tong-zi-dai-ming-ling" id="fu-gai-xi-tong-zi-dai-ming-ling"></a>

通过`Homebrew`安装的命令工具，默认安装在`/usr/local/opt/`，而系统自带 BSD 工具路径为`/usr/bin/`。当安装的 GNU 命令与系统自带命令重复时，用前缀`g`可以指定使用 GNU 版本，如：

```
gsed # GNU 版本(gnu-sed)
sed  # 系统 BSD 版
```

如果想省去`g`前缀，在环境变量`PATH`中把 GNU 工具的执行路径放置于`/usr/bin`之前即可，原理就是在系统扫描可执行路径时，会使用第一个符合条件的值。在`~/.bash_profile`添加对应路径到环境变量`PATH`（其实在`$ brew install`的时候，输出日志就有指示）：

```
export PATH="/usr/local/opt/<PACKAGE>/libexec/gnubin:$PATH"
```

其中`PACKAGE`为工具包名称。在前文“[安装 GNU 命令工具](https://blog.cotes.info/posts/use-gnu-utilities-in-mac/#%E5%AE%89%E8%A3%85-gnu-%E5%91%BD%E4%BB%A4%E5%B7%A5%E5%85%B7)”安装的命令行工具，可添加如下环境变量实现对系统自带工具的覆盖:

```
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-sed/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/binutils/bin:$PATH"
export PATH="/usr/local/opt/ed/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/findutils/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-indent/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-tar/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/gnu-which/libexec/gnubin:$PATH"
export PATH="/usr/local/opt/grep/libexec/gnubin:$PATH"
```

刷新使其生效：

```
source ~/.zshrc
```

### 安装git

```
brew install git
```

### oh my zsh

参考 [https://zhuanlan.zhihu.com/p/35283688](https://zhuanlan.zhihu.com/p/35283688)

```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## file

{% file src=".gitbook/assets/robbyrussell.txt" %}
robbyrussell.zsh-theme
{% endfile %}

