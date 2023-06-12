# 卷积核计算

&#x20;卷积中的特征图大小计算方式有两种，分别是‘VALID’和‘SAME’，卷积和池化都适用，**除不尽的结果都向上取整**。

{% hint style="info" %}
如果计算方式采用 '**VALID**'，则：

&#x20;$$w_{o u t}=\frac{w_{i n}-F}{s t r i d e}+1$$&#x20;

&#x20;其中 $$w_{o u t}$$ 为输出特征图的大小， $$w_{in}$$ 为输入特征图的大小， $$F$$ 为卷积核大小， $$stride$$ 为卷积步长。
{% endhint %}

{% hint style="info" %}
如果计算方式采用'**SAME**'，输出特征图的大小与输入特征图的大小保持不变，

$$w_{o u t}=\frac{w_{i n}+2 * p a d d i n g-F}{s t r i d e}+1$$&#x20;

其中 $$padding$$ 为特征图填充的圈数。

若采用'**SAME**'方式：

kernel\_size=1时，padding=0；

kernel\_size=3时，padding=1；

kernel\_size=5时，padding=3，以此类推。
{% endhint %}

















