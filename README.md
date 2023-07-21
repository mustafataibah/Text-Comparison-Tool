# Text Comparison Tool

The Text Comparison Tool is a Python-based application that models and compares bodies of text from different sources. It measures the similarity between two text bodies based on different factors such as the frequency of words, word lengths, word stems, sentence lengths, and adjective usage.

## Introduction

The purpose of this project is to provide an easy-to-use tool that can identify patterns and structures in written text and use these to compare different bodies of text. This tool might be useful in fields such as linguistics, literature, and data science, where the need to compare and analyze different text bodies is common.

## Usage

The main function run_tests() demonstrates how to use the tool. It creates a few models from different sources of text and uses them to classify other pieces of text. The models are based on the frequency of words, word lengths, word stems, sentence lengths, and adjective usage in the source text.

## Collaboration

I believe that my text classification program, while functional, is not fully accurate and there is a lot of room for improvement. Here are a couple of areas where enhancements could be made:

1. Stem Function Improvement: The current implementation of the stem function could be made more comprehensive by including additional case scenarios. This would increase the number of words it can accurately stem and reduce the number of words left "unstemmed".

2. Expand Adjective Words Database: The adjective_words feature in the add_string method could benefit from a larger database. A comprehensive collection of adjectives would improve the accuracy of the adjective-based text comparison. This could be implemented using various data structures such as lists or dictionaries.

Overall, the program functions effectively by using a combination of multiple helper functions, methods, and test functions. However, with the suggested improvements, the accuracy and overall performance of the text comparison tool could be significantly enhanced.

Your contribution to these enhancements would be highly appreciated. Feel free to fork the repository, implement your improvements, and open a pull request. Your input and collaboration are most welcome!
