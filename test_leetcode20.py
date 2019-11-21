"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:
输入: "()"
输出: true
示例 2:
输入: "()[]{}"
输出: true
示例 3:
输入: "(]"
输出: false
示例 4:
输入: "([)]"
输出: false
示例 5:
输入: "{[]}"
输出: true
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def isValid(s: str) -> bool:
    left = '([{'
    right = ')]}'
    import re
    n = len(s)
    temp_s = ''
    if n % 2:
        return False
    x = len(re.findall(r'\(\)', s))
    y = len(re.findall(r'\[\]', s))
    z = len(re.findall(r'{\}', s))
    if x + y + z == n // 2:
        return True
    for i in s:
        if i in left:
            temp_s += i
            continue
        if (len(temp_s) == 0) and (i in right):
            return False
        if (i in right) and (ok(temp_s[len(temp_s)-1],i)):
            temp_s = temp_s[:len(temp_s)-1]
        else:
            return False
    if len(temp_s) == 0:
        return True
    else:
        return False

def ok(a,b):
    c = False
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        c = True
    return c

if __name__ == '__main__':
    x = "(("
    print(isValid(x))
