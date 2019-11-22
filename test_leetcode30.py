"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：
输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def findSubstring(s: str, words: list) -> list:
    if not s or not words:
        return []
    n = len(s)
    x = len(words[0])
    m = len(words)*x
    words_dict = {}
    ans = []
    for j in range(len(words)):
        if words[j] in words_dict:
            words_dict[words[j]] += 1
        else:
            words_dict[words[j]] = 1
    for i in range(0, n-m+2):
        if s[i:i+x] in words:
            if ok(s[i:i+m],x) == words_dict:
                ans.append(i)
    return ans


def ok(a:str,num:int) -> dict:
    temp_dict = {}
    for i in range(0,len(a),num):
        if a[i:i+num] in temp_dict:
            temp_dict[a[i:i+num]] += 1
        else:
            temp_dict[a[i:i+num]] = 1
    return temp_dict


if __name__ == '__main__':
    ss = "barfoofoobarthefoobarman"

    ww = ["bar","foo","the"]
    print(findSubstring(ss, ww))
