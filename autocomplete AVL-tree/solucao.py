import streamlit as st
from arvoreAVL import AVLTree
from corpus import Corpus

@st.cache_data
def process_corpus_tree():
    Cpath = "static/corpusPlatao.pdf"
    corpus = Corpus(Cpath)
    corpus.process_text(lower_text=True, remove_punctuation=True, remove_digits=True, remove_roman_numerals=True)

    avl = AVLTree()
    for word in corpus.get_words():
        avl.add(word)
    return corpus, avl


def main():
    corpus, avl = process_corpus_tree()

    user_input = st.text_input("Digite o prefixo de busca:")
    if user_input:
        words = avl.words_found_prefix(user_input)
        if words:
            st.write("Palavras encontradas:")
            for word in words:
                st.write("- " + word)
        else:
            st.write(
                "Nenhuma palavra encontrada com o prefixo '{}'.".format(user_input)
            )


if __name__ == "__main__":
    main()