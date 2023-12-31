# 1844. Replace All Digits with Characters

You are given a 0-indexed string s that has lowercase English </br>
letters in its even indices and digits in its odd indices. </br>

There is a function shift(c, x), where c is a character and x is a  </br>
digit, that returns the xth character after c. </br>
 
For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'. </br> 
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]). </br>

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'. </br>

## Example 1:

Input: s = "a1c1e1" </br>
Output: "abcdef" </br>
Explanation: The digits are replaced as follows: </br>
- s[1] -> shift('a',1) = 'b' </br>
- s[3] -> shift('c',1) = 'd' </br>
- s[5] -> shift('e',1) = 'f' </br>

## Example 2:

Input: s = "a1b2c3d4e" </br>
Output: "abbdcfdhe" </br>
Explanation: The digits are replaced as follows: </br>
- s[1] -> shift('a',1) = 'b' </br>
- s[3] -> shift('b',2) = 'd' </br>
- s[5] -> shift('c',3) = 'f' </br>
- s[7] -> shift('d',4) = 'h' </br>

## Constraints:

1 <= s.length <= 100 </br>
s consists only of lowercase English letters and digits. </br>
shift(s[i-1], s[i]) <= 'z' for all odd indices i. </br>