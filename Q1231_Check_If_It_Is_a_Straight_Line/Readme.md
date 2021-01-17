## Roman to Integer

在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。

请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

**示例 1**：

> **输入**：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
> **输出**：true

**示例 2**：

> **输入**：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
> **输出**：false

**提示：**

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates 中不含重复的点




My Solution:

先算出前两个点的斜率，如果有第三个点，则从第三个点开始，算当前点i和i-1的斜率与i-1和i-2的斜率是否相同，相同就继续遍历，不同就输出false。对于直线平行于y轴的情况,使用try except进行捕捉，并**设斜率等于float('inf')**

Good Solution：

思路比较简单，三点A(x1,y1),B(x2, y2),C(x3,y3)如果处于同一条直线上，

那么一定满足公式 (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)（这里的/是指常规除法，不是计算机里的求商）

由于除法不好计算，所以转换为相乘，即(x2 - x1) * (y3 - y2) == (y2 - y1) * (x3 - x2)
