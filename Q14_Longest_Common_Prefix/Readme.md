## Longest Common Prefix

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

**示例 1：**

> **输入**：strs = ["flower","flow","flight"]
> **输出：**"fl":

**示例2**：

> **输入**：strs = ["dog","racecar","car"]
> **输出：**""
> **解释：**输入不存在公共前缀。



**提示：**

- 0 <= strs.length <= 200

- 0 <= strs[i].length <= 200

- strs[i] 仅由小写英文字母组成

  


My Solution:

以字符串数组第一个字符串为prefix模板，开始匹配后面所有字符串，如果当前prefix != str[0:len(prefix)]（**不能写成prefix not in str，注意代码准确性，是前缀不是子串**）。则prefix去掉最后一位字符，并**更新prefix长度**，如果匹配成功则遍历下一个字符串，当prefix=""输出结果或者匹配完所有字符串。

**注意：输入字符串数组可能为空**

Good Solution：

将字符串数组按照各个字符串首字母大小排序（首字母相同时比较第二位字母，以此类推），取出排序后第一位和最后一位字符串，python中可直接使用min(strs),max()实现。这两个字符串是从第一位开始最不相同的。然后从第一位开始，将最小的每一位i和最大的进行比较，遇见不同时就停止比较，输出最小字符串[0:i]。

**注：时间复杂度都是o(mn)只是写起来更方便酷炫。**