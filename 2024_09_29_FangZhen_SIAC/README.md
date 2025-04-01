## 模板字体控制介绍

计算机学报模板中使用`\begin{CJK*}\end{CJK*}`命令控制字体。

文件[CJC.cls](./CjC.cls)中的`\normalsize`命令控制全文字号。

### 标题

#### 一级标题

- 使用`\begin{CJK*}{UTF8}{zhhei} \end{CJK*}`命令包裹`section{}`，字体为黑体。
- 字号为5

以下是一个示例

```LaTex
\begin{CJK*}{UTF8}{zhhei}
    \zihao{5}
    \vskip 1mm
    \section{一级标题*字体为4号黑体*标题1}
    \textbf{对投稿的基本要求}：
\end{CJK*}
```



### 正文

使用`\begin{CJK*}{UTF8}{fs} \end{CJK*}`命令包裹``


## 自定义命令介绍

介绍一些计算机学报模板中使用的自定义命令

### \zihao[1]

该命令定义在[CJC.cls](./CjC.cls)中. 使用该命令时输入一个参数即可, 可选参数如下, 表示不同的字号大小：

1. 0
2. 0-
3. 1
4. 1-
5. 2
6. 2-
7. 3
8. 3-
9. 4
10. 4-
11. 5
12. 5--
13. 5-
14. 6
15. 6-
16. 7
17. 8

#### \zihao{}的变体命令

1. `\tiny`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{7-}`
2. `\scriptsize`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{7}`
3. `\fontnotesize`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{6-}`
4. `\small`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{6}`
5. `\normalsize`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{5}`
6. `\large`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{4-}`
7. `\Large`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{4}`
8. `\LARGE`
   1. 该命令定义于[CJC.cls](./CjC.cls)中.
   2. 命令作用等同于`\zihao{3}`
9. `\huge`
   1.  该命令定义于[CJC.cls](./CjC.cls)中.
   2.  命令作用等同于`\zihao{2-}`
10. `\Huge`
    1.  该命令定义于[CJC.cls](./CjC.cls)中.
    2.  命令作用等同于`\zihao{1-}`

## 使用宏包介绍