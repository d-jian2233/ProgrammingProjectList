import re


def count_words(text):
    # 使用正则表达式移除文本中的标点符号，并转换为小写，然后分割成单词列表
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)


# 示例文本
sample_text = "Hello, this is a sample text to demonstrate word counting in Python. It includes punctuation!"

# 调用函数并打印结果
word_count = count_words(sample_text)
print(f"The number of words in the sample text, excluding punctuation, is: {word_count}")
