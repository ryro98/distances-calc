#!/usr/bin/env python3
from __future__ import unicode_literals

import math
import random
import sys

import nltk
from collections import defaultdict


array_counter = []

terms = ['szachy', 'pozycja', 'taktyka', 'białe', 'czarne', 'wygrana', 'przegrana', 'błąd', 'strategia',
         'związanie', 'widełki', 'partia']

students_terms = ['apple', 'linux', 'php', 'java', 'windows', 'python',
                  'c++', 'assembler', 'książki', 'piwo', 'wino', 'spanie']


def printLine():
    line: str = ""
    for x in range(90):
        line += "="
    print(line)


def printIndexes():
    indexes: str = "   "
    for x in range(12):
        indexes += "{0: <7}".format("|D{num}".format(num=x))
    print(indexes)


def printTerms(terms_array):
    indexes: str = "   "
    for term in terms_array:
        indexes += "{0: <10}".format("|{num}".format(num=term))
    print(indexes)


def printOutput(name, list):
    printLine()
    print(name)
    if name != "Terms" and name != "Students' terms":
        printIndexes()
    else:
        if name == "Terms":
            printTerms(terms)
        else:
            printTerms(students_terms)
    num: int = 0
    for array in list:
        text: str = ""
        for x in array:
            if name != "Terms" and name != "Students' terms":
                text += "{0: <7}".format("|{num}".format(num=x))
            else:
                text += "{0: <10}".format("|{num}".format(num=x))
        index = "{0: <3}".format("D{}".format(num))
        print("{}{}|\n".format(index, text))
        num += 1


def calculateMatrix(name, array_source):
    big_matrix = []
    for z in range(len(array_source)):
        matrix = []
        for x in range(len(array_source)):
            sum: float = 0
            czebyszew_array = []
            for y in range(12):
                array_one: float = float(array_source[z][y])
                array_two: float = float(array_source[x][y])
                # euklides
                if name == 'euklides':
                    sum += pow(abs((array_one - array_two)), 2)
                # manhattan
                if name == 'manhattan':
                    sum += abs(array_one - array_two)
                # czebyszew
                if name == 'czebyszew':
                    czebyszew_array.append(abs(array_one - array_two))
            if name == 'czebyszew':
                sum = max(czebyszew_array)
            if name == 'euklides':
                sum = math.sqrt(sum)
                matrix.append("{:.2f}".format(sum))
            else:
                matrix.append(int(sum))
        big_matrix.append(matrix)
    return big_matrix


def counter():
    szachy_counter: int = 0
    pozycja_counter: int = 0
    taktyka_counter: int = 0
    biale_counter: int = 0
    czarne_counter: int = 0
    wygrana_counter: int = 0
    przegrana_counter: int = 0
    blad_counter: int = 0
    strategia_counter: int = 0
    zwiazanie_counter: int = 0
    widelki_counter: int = 0
    partia_counter: int = 0

    sequence: str = ""
    text: str = ""
    result: str = ""
    words = defaultdict(int)

    for x in range(1, 13):
        szachy_counter = 0
        pozycja_counter = 0
        taktyka_counter = 0
        biale_counter = 0
        czarne_counter = 0
        wygrana_counter = 0
        przegrana_counter = 0
        blad_counter = 0
        strategia_counter = 0
        zwiazanie_counter = 0
        widelki_counter = 0
        partia_counter = 0
        sequence = ""

        file = "txt{number}.txt".format(number=x)
        array = []
        try:
            text_file = open(file, encoding="UTF-8")
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        else:
            for line in text_file:
                sequence += line
            text = nltk.word_tokenize(sequence)
            text_file.close()

        tagged_text = nltk.pos_tag(text)

        for pair in tagged_text:
            word: str = pair[0]
            word = word.lower()

            if word == "szachy" or word == "szachów" or word == "szachom" or word == "szachami" or word == "szachach":
                szachy_counter += 1
            elif word == "pozycja" or word == "pozycji" or word == "pozycję" or word == "pozycją" or word == "pozycje" \
                    or word == "pozycjom" or word == "pozycjami" or word == "pozycjach":
                pozycja_counter += 1
            elif word == "taktyka" or word == "taktyki" or word == "taktyce" or word == "taktykę" or word == "taktyką" \
                    or word == "taktyk" or word == "taktykami" or word == "taktykach":
                taktyka_counter += 1
            elif word == "białe" or word == "białych" or word == "białym" or word == "białymi":
                biale_counter += 1
            elif word == "czarne" or word == "czarnych" or word == "czarnym" or word == "czarnymi":
                czarne_counter += 1
            elif word == "wygrana" or word == "wygranej" or word == "wygraną" or word == "wygrane" \
                    or word == "wygranych" or word == "wygranym" or word == "wygranymi" or word == "wygrać":
                wygrana_counter += 1
            elif word == "przegrana" or word == "przegranej" or word == "przegraną" or word == "przegrane" \
                    or word == "przegranych" or word == "przegranym" or word == "przegranymi" or word == "przegrać":
                przegrana_counter += 1
            elif word == "błąd" or word == "błędu" or word == "błędowi" or word == "błędem" or word == "błędzie" \
                    or word == "błędy" or word == "błędów" or word == "błędom" or word == "błędami" or word == "błędach":
                blad_counter += 1
            elif word == "strategia" or word == "strategii" or word == "strategię" or word == "strategią" \
                    or word == "strategie" or word == "strategiom" or word == "strategiami" or word == "strategiach":
                strategia_counter += 1
            elif word == "związanie" or word == "związania" or word == "związaniu" or word == "związaniem" \
                    or word == "związań" or word == "związaniom" or word == "związaniami" or word == "związaniach":
                zwiazanie_counter += 1
            elif word == "widełki" or word == "widełek" or word == "widełkom" or word == "widełkami" \
                    or word == "widełkach":
                widelki_counter += 1
            elif word == "partia" or word == "partii" or word == "partię" or word == "partią" or word == "partie" \
                    or word == "partiom" or word == "partiami" or word == "partiach":
                partia_counter += 1

        array.append(szachy_counter)
        array.append(pozycja_counter)
        array.append(taktyka_counter)
        array.append(biale_counter)
        array.append(czarne_counter)
        array.append(wygrana_counter)
        array.append(przegrana_counter)
        array.append(blad_counter)
        array.append(strategia_counter)
        array.append(zwiazanie_counter)
        array.append(widelki_counter)
        array.append(partia_counter)

        array_counter.append(array)

    # zad1 (calculating distance between terms)
    euklides_calculator = calculateMatrix('euklides', array_counter)
    czebyszew_calculator = calculateMatrix('czebyszew', array_counter)
    manhattan_calculator = calculateMatrix('manhattan', array_counter)

    # zad1 - print output
    printOutput("Terms", array_counter)
    printOutput("Euklides's distance", euklides_calculator)
    printOutput("Czebyszew's distance", czebyszew_calculator)
    printOutput("Manhattan's distance", manhattan_calculator)
    printLine()

    # zad2 - recommendation (closest)
    closest: int = None
    closest_sum: float = 0
    user_vector: int = 3
    for x in range(12):
        check_sum: float = float(euklides_calculator[user_vector][x])
        if x != user_vector and check_sum != 0:
            if closest is None:
                closest = x
                closest_sum = check_sum
            else:
                if check_sum < closest_sum:
                    closest = x
                    closest_sum = check_sum

    # zad2 - print output
    print("Closest vector to the user vector ({user}) is vector {vector} (distance = {sum})"
          .format(user=user_vector, vector=closest, sum=closest_sum))
    printLine()

    # zad3 - good/bad client
    good_vector = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    bad_vector = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    neutral_vector = []
    for x in range(12):
        neutral_vector.append(random.randint(1, 10))
    client_vectors = [good_vector, bad_vector, neutral_vector]
    client_vectors_euklides = calculateMatrix('euklides', client_vectors)

    # zad3 - print output
    neutral_vector_string: str = ""
    verdict: str = ""
    for x in range(12):
        neutral_vector_string += "[" + str(neutral_vector[x]) + "] "
    print('Neutral vector: {}'.format(neutral_vector_string))
    if client_vectors_euklides[2][0] < client_vectors_euklides[2][1]:
        verdict = "good"
    else:
        verdict = "bad"
    print('Neutral vector is closer to {ver} vector (good={good}, bad={bad})'
          .format(ver=verdict, good=client_vectors_euklides[2][0], bad=client_vectors_euklides[2][1]))

    # zad4 - compare students
    students_vectors = []
    for x in range(12):
        student_vector = []
        for y in range(12):
            student_vector.append(random.randint(1, 100))
        students_vectors.append(student_vector)
    students_euklides = calculateMatrix('euklides', students_vectors)

    # zad4 - print output
    printOutput("Students' terms", students_vectors)
    printOutput("Students' distances", students_euklides)


if "__main__" == __name__:
    counter()

