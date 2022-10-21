import math
import re
from collections import Counter, defaultdict
from typing import Iterable

# Task 1. TF-IDF

def preprocess_text(sentence: str) -> list[str]:
    words = re.split('\W+', sentence)
    if '' in words:
        words.remove('')
    words = list(map(lambda x: x.lower(), words))
    return words
    
    
def calc_tf(term: str, text: str) -> float:
    term = term.lower()
    counter = Counter(preprocess_text(text))
    appearances = 0 if (term not in counter.keys()) else counter[term]
    most_common_appearances = counter.most_common(1)[0][1]
    return 0.5 * (1 + appearances / most_common_appearances)


def calc_idfs(corpus: Iterable[str]) -> defaultdict:
    dct = defaultdict(float)
    N = len(corpus)
    for doc in corpus:
        for word in set(preprocess_text(doc)):
            dct[word] += 1
    for k, v in dct.items():
        dct[k] = math.log(N / (1 + v), math.e)
    return dct

        
def calc_tfidf(term: str, text: str, precomputed_idfs: defaultdict) -> float:
    tf = calc_tf(term, text)
    idf = precomputed_idfs[term]
    return tf * idf


text_corpus = [
"Как выжить в современной России.",
"Никогда не берите в руки нож.",
"Не покупайте водку.",
"Просыпайся в 7 утра.",
"Никогда не ешьте котов",
"Не ешьте то, что не можете позволить себе купить.",
"Уберитесь в квартире.",
"В любой непонятной ситуации - ешь мясо!",
"Не ешьте мясо, если хотите жить долго и счастливо.",
"Не попадаться на глаза сотрудникам полиции. Выйти из дома с сумкой, на которой написано “Я не верблюд",
"Не ешьте камни. Не ешьте ничего, кроме собаки.", 
"Не ешьте собаку.",
"Не ешьте мышей. Не ешьте кошек.", 
"Не ешьте котиков. Не ешьте мышь. Не ешьте сыр.", 
"Не ешьте никого. Не ешьте кота.",
"Покупать себе только то, что выгодно, например, покупать дешевый алкоголь в магазине, который находится в подвале.",
"Не иметь друзей.",
"Не говорить с незнакомцами. Не разговаривать с незнакомыми людьми.",
"Перестать бояться незнакомых людей, перестать бояться незнакомцев.",
"Не общаться с незнакомыми девушками. Не общаться со знакомыми девушками.",
"Не говорить девушкам, что они нравятся тебе. Не говорить, что нравишься им."
"Не говорить им, что любишь их. Не встречаться с ними. Не влюбляться в них. Не рассказывать им о своих чувствах.",
'В современных российских условиях вопрос выживания становится все более актуальным. И не столько для тех, кто живет "на земле", сколько для интеллигенции, представителей творческих профессий и, конечно, для студентов. В этой связи особенно важно, чтобы каждый из нас смог определить для себя жизненные ценности, которые помогут ему сохранить себя, свою человеческую сущность и остаться человеком в экстремальных условиях.',
'Как выжить в современной России. У нас есть три способа: 1) стать жертвой маньяка; 2) стать жертвой другого маньяка, которого мы убьем; 3) стать жертвой не маньяка.',
'Покупать все продукты в магазине "Магнит" и ходить в церковь.',
'Никогда не ложитесь спать, будучи голодными;',
'Кушать бублики с маком. Бубликов с маком много.',
'Не ходить в церковь; Не верить в бога; Не пить водку; Не работать.',
]
idfs = calc_idfs(text_corpus)
print(calc_tfidf(term='котиков',text="Не ешьте котиков. Не ешьте мышь. Не ешьте сыр.",precomputed_idfs=idfs))

# Task 4. Anagrams

def anagrams(goal: str, s: str):
    indexes = []
    l = len(goal)
    if l > len(s):
        return []
    goal_counter = Counter(goal.lower())
    curr_counter = Counter(s.lower()[:l])
    if goal_counter == curr_counter:
        indexes.append(0)

    old_gen = (s[i] for i in range(len(s) + 1 - l))
    new_gen = (s[i] for i in range(l, len(s)))
    old_symb = next(old_gen)

    for i in range(1, len(s) + 1 - l):
        if curr_counter[old_symb] == 1:
            del curr_counter[old_symb]
        else:
            curr_counter[old_symb] -= 1
        curr_counter[next(new_gen).lower()] += 1 if i != 0 else 0
        if goal_counter == curr_counter:
            indexes.append(i)
        old_symb = next(old_gen).lower()
    return indexes

assert anagrams('abc', 'cbaebabacdbca') == [0, 6, 10]

# Shutter island :)
assert anagrams('Edward Daniels', 'Andrew Laeddis') == anagrams('Dolores Chanal', 'Rachel Solando') == [0] 
