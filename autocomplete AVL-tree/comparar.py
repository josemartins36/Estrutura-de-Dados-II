import matplotlib.pyplot as plt
import time
from corpus import Corpus
from arvoreAVL import AVLTree

# Medir o tempo da busca na AVL
def timer_avl(avl, prefix):
    start_time = time.time()
    result = avl.words_found_prefix(prefix)
    end_time = time.time()
    return len(result), end_time - start_time


# Medir o tempo da busca na lista
def timer_list(list, prefix):
    start_time = time.time()
    result = [word for word in list if word.startswith(prefix)]
    end_time = time.time()
    return len(result), end_time - start_time


def main():
    Cpath = "static/corpusPlatao.pdf"
    corpus = Corpus(Cpath)
    corpus.process_text(lower_text=True, remove_punctuation=True, remove_digits=True, remove_roman_numerals=True)

    # ED's
    avl = AVLTree()
    word_list = []

    for word in corpus.get_words():
        avl.add(word)
        if word not in word_list:
            word_list.append(word)

    # Armazenar os tempos
    avl_times = []
    list_times = []

    # Prefixo para buscar
    prefix = "contempla"

    # Número de iterações
    num_iterations = 1000

    for _ in range(num_iterations):
        # Medir o tempo na AVL
        avl_result, avl_time = timer_avl(avl, prefix)
        avl_times.append(avl_time)
        # Medir o tempo na lista
        list_result, list_time = timer_list(word_list, prefix)
        list_times.append(list_time)

    # Plotar os resultados
    plt.plot(avl_times, label="AVL")
    plt.plot(list_times, label="List")
    plt.xlabel("Iteração")
    plt.ylabel("Tempo (em segundos)")
    plt.title("Comparação de busca - Prefix: {}".format(prefix))
    plt.legend()
    plt.savefig("static/contempla.png")
    plt.close()


if __name__ == "__main__":
    main()