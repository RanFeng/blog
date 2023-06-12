# 常用Mac命令

### 图片转化命令

```
sips可以转换一个或多个图片文件的文件格式
sips -s format [格式名称] "[文件名]" --out "[输出文件的名称]"
sips -s format png "goswift.jpg" --out "goswift.png"

要想批量转换图片文件，我们需要使用下面命令格式
for i in [文件名]; do sips -s format "[格式名称]" $i --out "[终点]/$i.[格式名称]";done
for i in *.jpeg; do sips -s format png $i --out Doc/$i.png;done

按比例缩放
sips -Z 600 goswift.png
sips -z 300 600 goswift.png

查看图片信息
file go-swift.png //文件信息
mdls go-swift.png //可以获取到图片详细信息

```

sips除了能转换图片格式以外，还可以对图片进行调整大小(resize)，旋转(rotate)和翻转(flip)等。

* 拿一个原size是1200x896的house.jpg为例:
  * **限定范围缩放命令**: `sips -Z pixelsWH [file]`
    * 例子: `sips -Z 300 house.jpg`
    * 将原图缩放到300x300像素的方框内，保持图片的长宽比不变
  * **调整大小命令**: `sips -z height width [file]`
    * 例子: `sips -z 400 400 house.jpg`
    * 图片会被缩小拉伸到400x400，原图片的长宽比会改变
  * **旋转图片命令**: `sips -r degreesCW [file]`
    * 例子: `sips -r 90 house.jpg`
    * 图片会顺时针旋转90度
  * **翻转图片命令**: `sips -f horizontal|vertical [file]`
    * 例子: `sips -f horizontal house.jpg`
    * 图片会水平翻转。如果使用vertical, 则会垂直翻转
  * **注意，上述命令会直接修改原图片，如果要保留原图片，则可以加上–out 参数指定输出的文件名。比如`sips -f horizontal house.jpg --out house_horizontal.jpg`**

convert也是[ImageMagic](https://www.imagemagick.org/script/index.php)的组件之一。简单的转换格式用法非常的简单\
convert会根据文件后缀自动转换为想要的格式

```
convert [源文件] [目标文件]
$ convert kulipa.jpg kulipa.png # 转换为png文件
$ convert kulipa.jpg kulipa.bmp # 转换为bmp文件
```

### 重定向至剪贴板

```
pbcopy
与之对应都是pbpaste，前面有人提到了。我另外在.zshrc加了一个函数：
function copy() { cat $1 | pbcopy }
另外也在.vimrc中加了调用这个命令的快捷键。
```

### 高亮文件语法输出

```
可以让你的cat文件时候高亮代码，ccat文件可以让你的代码高亮
ccat 效果如下
```

![](<.gitbook/assets/image (7).png>)

### 配置 Launchpad

在大家安装好应用去 Launchpad 里寻找的时候，时常会发现原生的配置让 Launchpad 看的稍许拥挤，但是在系统偏好设置里我们是无法修改的。为了让我们的 Launchpad 识别度更高并且更加美观，可以通过终端对排列方式进行修改，复制以下代码至终端即可：

```
defaults write com.apple.dock springboard-columns -int 8; defaults write com.apple.dock springboard-rows -int 7; defaults write com.apple.dock ResetLaunchPad -bool TRUE; killall Dock
```

命令中有两个数字 8 和 7，它们分别代表的是布局中的列数和行数，如果想更清除的了解该段命令，可以参考[《通过终端命令改变 Launchpad 中应用图标的大小》](https://sspai.com/post/33299)。

![](<.gitbook/assets/image (5).png>)

除了可以对 Launchpad 的布局进行更改，还可以根据自己的喜好对北背景的模糊程度进行更改，复制以下代码至终端即可：

```
defaults write com.apple.dock springboard-blur-radius -int 100; killall Dock
```

命令中有一个数字 100，它代表的背景模糊的程度，你可以在 0 \~ 255 的范围内选择。

### 终端开启允许安装任何来源App

系统有一个保护叫做 [Gatekeeper](https://support.apple.com/zh-cn/HT202491) , 这个是防止第三方应用访问你的隐私信息的。如果你想关掉或者开启在终端里输入

```
# 开启
sudo spctl --master-disable

# 关闭
sudo spctl --master-enable
```

### 禁止生成 DS\_Store 文件

`.DS_Store` 是 macOS 保存文件夹的自定义属性的隐藏文件，如文件的图标位置或背景色，相当于 Windows 的 `desktop.ini`

```
# 禁止.DS_store生成，执行以下命令
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE2

# 恢复.DS_store生成，执行
defaults delete com.apple.desktopservices DSDontWriteNetworkStores
```

### 重置被遗忘的管理员密码

如果你忘记了登陆密码，可以使用此方式更改管理员密码。首先，在系统开机还未进入登录界面时按下`command+S`进入单用户模式。然后输入

```
mount -rw /
```

以读写方式挂载文件系统；接着重置管理员 json 的密码，回车后会要求你输入新的密码

```
passwd json
```

完成后，输入指令重启

```
reboot
```

### 输入苹果图标

在需要输入的地方同时按`shift + option + k`键

### 调出 emoji 表情

在需要输入的地方同时按`control + command + space(空格)`键













