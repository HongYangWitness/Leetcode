## Implement strStr()

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  **-1**。



**示例 1:**

> **输入**: haystack = "hello", needle = "ll"
> **输出**: 2

**示例 2:**

> **输入:** haystack = "aaaaa", needle = "bba"
> **输出:** -1



**说明:**

当 needle 是**空字符串**时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当**返回 0** 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。




My Solution:

思路很简单，如果needle是haystack子串，那么其第一次出现的位置应符合1.haystack[i]==needle[0],haystack[i:i+len(needle)]==needle. 这里注意i+len(needle)如果大于len(haystack)可以直接跳过判断从而节省时间。



Good Solution

**利用栈的思想，**从最后一个开始遍历，如果nums[i]==nums[i-1]，咋把nums[i]弹出。

**注意：python中 list.pop(index)可以把指定位置的元素直接剔除（不一定非要是栈顶）。**


