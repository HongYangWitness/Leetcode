## Length of Last Word

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、**不包含任何空格字符**的 **最大子字符串**。



**示例 1：**

> **输入：**"Hello World"
> **输出**：5

My Solution:

这题主要使用暴力，从最后一个字母开始倒着遍历，在遍历中计数最后一个单词长度length遇见空格时或者到达字符串首位时停止遍历。注意这时候**有一种情况**， **一开始遇见无意义的多个空格**如:"a            "。这个字符串应该返回1。对于这种情况，我们要将空格过滤，即s[i]==" "and length ==0(说明还没遇见有效的字符)时pass，而剩下要么在遍历完后return length，要么在s[i]==" " and length !=0 return length。