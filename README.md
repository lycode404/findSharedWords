# findSharedWords
基于python做的一个小实验，找出中文字符集(GB2312)和日语字符集(Shift-JIS)共有的汉字。  
按照A,B,C,D的顺序执行py文件，最后会输出四个excel文档，xxxTable是字符集编码表，SharedWordsInxxx展示了共有的汉字（标蓝）在xxx编码表的位置。  
（也许你会发现代码中部分变量名写了GBK，其实我原本想比较GBK和JIS字符集，但是比较后发现GBK已经把所有JIS汉字都收录进去了，所以就改成了GB2312与JIS比较。）
