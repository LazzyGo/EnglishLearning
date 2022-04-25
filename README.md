# EnglishLearning

# Basis

## Beginner's things

https://learnthesewordsfirst.com/LearnTheseWordsFirst.html

http://learnthesewordsfirst.com/about/how-to-use-this-dictionary.html

## Defining Vocabulary

Longman: https://learnthesewordsfirst.com/LearnTheseWordsFirst.html

Longman:https://www.pu-kumamoto.ac.jp/users_site/rlavin/resources/wordlists/LDV.html

Macmillan: https://www.macmillandictionary.com/learn/clear-definitions/

Oxford: https://www.oxfordlearnersdictionaries.com/wordlist/american_english/oxford3000/

Cambridge:

Collins:

# Dictionary

https://dictionary.cambridge.org/


## Tools

word finding tool: https://learnthesewordsfirst.com/WordFindingTool.html

Oxford checker: https://www.oxfordlearnersdictionaries.com/text-checker/

# Termux

排序
```
sort file
```
去除重复行
```
uniq file
# 或者组合上面
sort file | uniq
```
转换csv
```
sed -i "s/\(.*\)/\1,\1/g" file
```
去除已学过的单词
```
cat a.txt b.txt b.txt |sort |uniq -u
```
