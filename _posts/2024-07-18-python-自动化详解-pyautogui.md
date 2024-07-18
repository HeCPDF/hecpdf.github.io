---
layout: post
title: Python 自动化详解（pyautogui）
date: 2023-10-27 10:44:04 +0800
categories: 技术 Python
tags: [python, 自动化, 开发语言]
author: csdn-qq_34745941
---

## 1 概述

### 1.1 第三方库：pyautogui

```bash
$ pip install pyautogui
```

### 1.2 坐标说明

![](/images/img-blog.csdnimg.cn/cf47278a6a7b4c1bb70f6c76ccf23340.png)

## 2 操作对象

### 2.1 鼠标

#### 2.1.1 定位

```python
import pyautogui

# 鼠标定位：鼠标的 x，y 坐标
position = pyautogui.position()
print(f'x = {position.x}, y = {position.y}')
```

#### 2.1.2 移动

```python
import pyautogui

# 移动鼠标：两种方式
# 常用属性：x=横坐标，y=纵坐标，duration=持续时间（默认 0）
pyautogui.moveTo(x=100, y=200, duration=1)  # 方式1：移动至
pyautogui.moveRel(x=10, y=20)  # 方式2：按方向移动 x: 正右负左、y：正上负下
```

#### 2.1.3 拖动

```python
import pyautogui

# 移动拖动：两种方式
# 常用属性：x=横坐标，y=纵坐标，duration=持续时间（默认 0）
pyautogui.dragTo(x=100, y=200, duration=1)  # 方式1：移动至
pyautogui.dragRel(xOffset=10, yOffset=20)  # 方式2：按方向移动 x: 正右负左、y：正上负下
```

#### 2.1.4 滚动

```python
import pyautogui

# 移动滚动
pyautogui.scroll(20)
```

#### 2.1.5 点击

```python
import pyautogui

# 单击鼠标
pyautogui.click(10, 20)  # 鼠标点击指定位置，默认左键
pyautogui.click(x=10, y=20, button='left')  # 左键
pyautogui.click(x=10, y=20, button='right')  # 右键
pyautogui.click(x=10, y=20, button='middle')  # 中间

# 双击鼠标
pyautogui.doubleClick(10, 10)  # 左键
pyautogui.rightClick(10, 10)  # 右键
pyautogui.middleClick(10, 10)  # 中间

# 点击 & 释放
pyautogui.mouseDown()  # 鼠标按下
pyautogui.mouseUp()  # 鼠标释放
```

### 2.2 键盘

#### 2.2.1 输入

```python
import pyautogui


pyautogui.write('Hello World')  # 立即输出
pyautogui.write('Hello World', interval=0.5)  # 间隔0.5s输出
```

#### 2.2.2 按键

```python
import pyautogui

pyautogui.keyDown('enter')  # 按下指定键
pyautogui.keyUp('enter')  # 松开指定键

# 效果同上
pyautogui.press('enter')  # 按一次指定键
```

> 注：暂不支持中文
{: .prompt-warning }

| 键盘字符串            | 说明    |
| --------------------- | ------- |
| enter                 | 回车键  |
| tab                   | TAB 键  |
| space                 | 空格键  |
| up, down, left, right | 方向键  |
| ctrl                  | Ctrl 键 |
| …                     | …       |
  
#### 2.2.3 快捷键
```python
pyautogui.hotkey('ctrl', 'a')  # 选中
pyautogui.hotkey('ctrl', 'c')  # 复制
pyautogui.hotkey('ctrl', 'v')  # 粘贴


pyautogui.hotkey('ctrl', 'alt', 'a')
```

### 2.3 屏幕

#### 2.3.1 截图

```python
import pyautogui


img = pyautogui.screenshot()
img.save('屏幕截图.jpg')
```

#### 2.3.2 分辨率

```python
import pyautogui

size = pyautogui.size()
print(size)  # Size(width=1366, height=768)

# 坐标原点(0, 0), 坐标终点(width-1, height-1)
print(pyautogui.onScreen(1366, 768))  # False
print(pyautogui.onScreen(1365, 767))  # True
```

### 2.4 信息提示

#### 2.4.1 提示框

```python
import pyautogui

text = pyautogui.alert(text="这是一个提示框", title='提示')
print(text)
```

![](/images/img-blog.csdnimg.cn/b5cc65e9db0d48d4ad99e03011480471.png)

#### 2.4.2 选择框

```python
import pyautogui

text = pyautogui.confirm('请选择一项', buttons=['选项 A', '选项 B', '选项 C'])
print(text)  # buttons 中的取值
```

![](/images/img-blog.csdnimg.cn/ecbb9a3f99804e979cffff957e6b75e3.png)

#### 2.4.3 密码输入

```python
import pyautogui

text = pyautogui.password('请输入密码：')
print(text)
```

![](/images/img-blog.csdnimg.cn/0b147b055b184fada8e828d66c3b4188.png)

#### 2.4.4 普通输入

```python
import pyautogui

text = pyautogui.prompt('请输入：')
print(text)
```

![](/images/img-blog.csdnimg.cn/010c3dfd845d4d218c633883c1b590ca.png)


## 版权声明

版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。
本文链接：https://blog.csdn.net/qq_34745941/article/details/134062466