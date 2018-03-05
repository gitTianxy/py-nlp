# encoding=utf-8
"""
chap.1, p4-7
---
* concordance
    - shows every occurrence of a given word, together with some context.
* similar
    - words appear in a similar range of contexts--synonyms
* common context
    - the contexts that are shared by two or more words
* dispersion plot
    - the location of a word in the text
* generate: generating some random text based on the text given
    - it reuses common words and phrases from the source text,
    - and gives us a sense of its style and content.
"""
from nltk.book import *

print("*** concordance")
# text1.concordance("monstrous")

print("*** similar")
# text1.similar("monstrous")

print("*** common contexts")
# text2.common_contexts(["monstrous", "very"])

print("*** dispersion plot")
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

print("*** generate(diff from instance in 'book'")
text4.generate(["citizens", "democracy", "freedom", "duties", "America"])
