from typing import Any, Iterable, List, Optional, Set, Tuple
from load import load_words
import math
import vectors as v
from vectors import Vector
from word import Word
import time
import ftfy as fx
def CoSineSim(left_vector: Vector,right_vector: Vector) -> float:
    """Finds cosine similarity to a given word"""
    distance = (v.cosine_similarity_normalized(left_vector, right_vector))
    # We want cosine similarity to be as large as possible (close to 1)
    #sorted_by_distance = sorted(words_with_distance, key=lambda t: t[0], reverse=True)
    return distance

def find_word(text: str, words: List[Word]) -> Optional[Word]:
    try:
        return next(w for w in words if text == w.text)
    except StopIteration:
        return None
def cosin_similarities(words: List[Word], text1: str, text2: str):
    left_word = find_word(text1, words)
    right_word = find_word(text2, words)
    print(left_word)
    print(right_word)
    if not left_word or not right_word:
        print(f"Uknown word: {text1} or {text2}")
        return
    print(f"Words related to {left_word.text}:")
    Cos = CoSineSim(left_word.vector, right_word.vector)

    return Cos
if __name__ == "__main__":
    t0 = time.time()
    words = load_words('data\\final_de-en_wiki_full_25kL4_Vector_Cleaned.vec')
    print("######################## Analogies ##################")
    t1 = time.time()
    print("loading the model takes %f seconds" % (t1 - t0))

    with open("datasets\\GUR65.txt", 'r', encoding='utf8') as f, open("testresults\\GUR65_de_25kV0N.txt", 'w', encoding='utf8') as fw:

        line = f.readline()
        while line:
            wds = line.strip().split(':')
            orgw = str(fx.fix_text(wds[0].strip())).lower()
            trgw = str(fx.fix_text(wds[1].strip())).lower()
            val = fx.fix_text(wds[2].strip())
            cos = cosin_similarities(words, orgw, trgw)
            fw.write('{0} : {1}\n'.format(val, cos))
            line = f.readline()
