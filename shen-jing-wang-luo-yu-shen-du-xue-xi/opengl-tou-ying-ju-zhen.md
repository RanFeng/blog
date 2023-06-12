# 投影矩阵

相机投影过程中，设计基本的参数有内参$$K$$ 和外参$$Rt$$ 。

## 内参矩阵$$K$$&#x20;

在真实投影过程中，内参矩阵 $$K$$ 可表示如下：

$$
K=\left[\begin{array}{ccc}{f_{x}} & {s} & {x_{0}} \\ {0} & {f_{y}} & {y_{0}} \\ {0} & {0} & {1}\end{array}\right]
$$

其中：

* 表示焦距的参数: $$f_x,f_y$$&#x20;
  * 焦距就是真空与图像平面(投影屏幕)的距离，类似于人眼和视网膜，焦距的度量是针对像素的。针孔相机的 $$f_x,f_y$$ 有相同的值。上图中红线部分就是焦距。但是在实际中， $$f_x$$ 和 $$f_y$$ 一般不同，因为:
    * 数码相机传感器的缺陷
    * 后处理中图像被非均匀缩放&#x20;
    * 相机透镜导致的无意的失真&#x20;
    * 相机使用了失真的格式，透镜将宽屏场景压缩到标准大小的传感器中&#x20;
    * 相机校准的误差&#x20;
* 主点偏移 $$x_0,y_0$$&#x20;
  * 相机的主轴是与图像平面垂直且穿过真空的线，它与图像平面的焦点称为主点。主点偏移就是主点位置相对于图像平面(投影面)的位置。下图中，增加 $$x_0$$ 的值相当于把针孔向右移动，等价将投影面向左移动同时保持针孔位置不变。

![相机主点](<../.gitbook/assets/image (1).png>)

* &#x20;轴倾斜 $$s$$&#x20;
  * 轴倾斜会导致投影图像的形变。

将内参矩阵分解为切变(_shear_,类似于将长方形压成平行四边形的变形方式)、缩放，平移变换，分别对应轴倾斜、焦距、主点偏移:

$$
\begin{aligned} K &=\left[\begin{array}{ccc}{f_{x}} & {s} & {x_{0}} \\ {0} & {f_{y}} & {y_{0}} \\ {0} & {0} & {1}\end{array}\right] \\ &=\left[\begin{array}{ccc}{1} & {0} & {x_{0}} \\ {0} & {1} & {y_{0}} \\ {0} & {0} & {1}\end{array}\right] \times\left[\begin{array}{ccc}{f_{x}} & {0} & {0} \\ {0} & {f_{y}} & {0} \\ {0} & {0} & {1}\end{array}\right] \times\left[\begin{array}{ccc}{1} & {\frac{s}{f_{x}}} & {0} \\ {0} & {1} & {0} \\ {0} & {0} & {1}\end{array}\right] \end{aligned}
$$

第二个等式右边三个矩阵依次是：2D平移、2D缩放、2D切变

另一种等价的分解是将切变放在缩放前面:

$$
K=\left[\begin{array}{ccc}{1} & {0} & {x_{0}} \\ {0} & {1} & {y_{0}} \\ {0} & {0} & {1}\end{array}\right] \times\left[\begin{array}{ccc}{1} & {\frac{s}{f_{x}}} & {0} \\ {0} & {1} & {0} \\ {0} & {0} & {1}\end{array}\right] \times\left[\begin{array}{ccc}{f_{x}} & {0} & {0} \\ {0} & {f_{y}} & {0} \\ {0} & {0} & {1}\end{array}\right]
$$

内参矩阵的另一个角度：

{% embed url="https://blog.csdn.net/u010128736/article/details/52850444" %}
摄像机模型（内参、外参）
{% endembed %}

## OpenGL中的可视空间

对于OpenGL函数 `gluPerspective()` 创建一个可视空间，指定近平面位置和视角大小。

```
void gluPerspective(GLdouble fovy, GLdouble aspect, GLdouble near, GLdouble far);
创建一个表示一个对称透视视图的平截头体的矩阵，并把它与当前矩阵相乘。
fovy是yz平面上视野的角度，它的值必须在[0.0, 180.0]的范围之内。
aspect是这个平截头体的纵横比，也就是它的宽度除以高度。
near和far值分别是观察点与近侧裁剪平面以及远侧裁剪平面的距离(沿z轴负方向)， 这两个值都应该是正的。
```

![由glPerspective()指定的透视可视空间](<../.gitbook/assets/image (3).png>)

对于上述的平截头体的任何一个平截面，**都可以**视为像平面。

而对于内参矩阵中的焦距，指的是相机原点到成像平面的距离。















{% embed url="http://ksimek.github.io/perspective_camera_toy.html" %}

{% embed url="http://www.songho.ca/opengl/gl_projectionmatrix.html" %}

{% embed url="https://www.edmundoptics.fr/knowledge-center/application-notes/imaging/understanding-focal-length-and-field-of-view/" %}

