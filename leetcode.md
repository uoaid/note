

###### 求众数	

```java
//给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素 (摩尔投票法)

List<Integer> majorityElement(int[] nums) {
     List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
         
        int cand1 = nums[0], count1 = 0;           //选俩潜力股
        int cand2 = nums[0], count2 = 0;

         for (int num : nums)
        {
            if (cand1 == num) { count1++;  continue; }  //相同加票
            if (cand2 == num) { count2++;  continue; }

            if (count1 == 0) { cand1 = num;  count1++; continue;  } //票为0 重选
            if (count2 == 0) { cand2 = num;  count2++; continue;  }

            count1--;  count2--;
        }

         count1 = 0;     count2 = 0;
        for (int num : nums)                           //验证
        {
            if (cand1 == num) count1++;
            else if (cand2 == num) count2++;
        }

        if (count1 > nums.length / 3) res.add(cand1);
        if (count2 > nums.length / 3) res.add(cand2);

        return res;
    }

```

###### 洗牌算法

```java
//前n-1张牌洗好的情况下，第n张牌随机与前n-1张牌的其中一张牌交换，或者不换

```

###### 反转链表

```java
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

ListNode reverseList(ListNode head) {     //迭代

  ListNode prev = null;
  ListNode curr = head;
        while (curr != null)
        {
            ListNode nextTemp = curr.next;   //保存下个结点，防止断掉找不到
            curr.next = prev;    //当前节点指向     
            prev = curr;         //更新之前节点
            curr = nextTemp;     //更新当前节点
        }
         return prev;
}

```

```java

ListNode reverseList(ListNode head) {      //递归
    
    if (head == null || head.next == null)  return head;
  
    ListNode p = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return p;
}

```

###### 单调栈

- 「 对于找最近一个比当前值大/小」的问题，都可以使用单调栈来解决。⌟
- 栈可以很好的保存原始位置，`最近`影射`栈顶`。题目要求`更大`，因此`更大`即解--出栈，`更小`则入栈
- 「 栈内存放的永远是还没更新答案的下标。⌟

```java
  
//给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。如不存在输出 -1。
//单调栈（被动更新）比暴力（主动更新）快                                    初值赋-1，解决最大值老无所依。

  public int[] nextGreaterElements(int[] nums)
    {
        int n = nums.length;   int[] ret = new int[n];
        Arrays.fill(ret, -1);

        Deque<Integer> stack = new LinkedList<Integer>(); // 栈放索引
        for (int i = 0; i < n * 2 - 1; i++)
        {                   //比栈顶大，索引出栈并返回值
        while(!stack.isEmpty() && nums[stack.peek()]<nums[i%n]) {
                ret [stack.pop()]    = nums[i%n];
            }
                stack.push(i%n);             //储存当前下标
        }              return ret;
    }
    
```

######  优先队列

请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 `limit` *。*

```java

    int longestSubarray(int[] nums, int limit)
    {                                  
        PriorityQueue<Integer> minQueue = new PriorityQueue<>(Comparator.naturalOrder());
        PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Comparator.reverseOrder());
      
        int left = 0, right = 0;        int ans = 0;
        while (right < nums.length && left < nums.length) 
        {
            minQueue.add(nums[right]);
            maxQueue.add(nums[right]);

            if (maxQueue.peek() - minQueue.peek() <= limit)
            {
                ans = Math.max(ans, right - left + 1);
                right++;       continue;
            }

            maxQueue.remove((Integer) nums[left]);
            minQueue.remove((Integer) nums[left]);
            left++;        right++;
        }
                return ans;
    }
    

```



```java
       /**
     * @param nums 一组非负整数
     * @return - String.compareTo() 是按照 lexicographically, 字典顺序排列的
     * - 利用compareTo, 来倒序排列 string, 刚好就得到我们要的结果.
     */
      
      //重写排序规则 12-14ms
       // Arrays.sort(strArr, new Comparator<String>() {
       //     @Override
       //     public int compare(String o1, String o2) {
       //         //继承此方法的时候，要自定义比较器，conpareTo方法返回值为1(升序),0，-1(降序)。
       //         //返回正值 交换；负值不交换
       //         return (o2 + o1).compareTo((o1 + o2));
       //     }
       // });
        //Lambda表达式 重写排序规则 速度慢了5倍 72-82ms
        Arrays.sort(strArr, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));
```

