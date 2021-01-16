## Reverse Integer

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

> **输入:** 121
> **输出:** true

**示例 2:**

> **输入**: -121
> **输出**: false
> **解释:** 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

**示例 3:**

> **输入**: 10
> **输出**: false
> **解释:** 从右向左读, 为 01 。因此它不是一个回文数。



My Solution:

根据定义，小于0的数肯定不是回文，0-9的肯定是回文，剩下的数，每次提取x的整数第i+1位数和倒数第i+1位数，发现不相等就输出false。（注意是提取x，而不改变，否则100001这种情况，x去掉第一位和最后一位后只剩下0）

Good Solution：

首先判断，x<0,x以0结尾肯定不是回文数，对于剩下的数，反转后半边（直到x<rev），然后比较x与rev（偶数位数）或x与rev//10（奇数位数）