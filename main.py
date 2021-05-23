#!/usr/bin/env python3
import sys
import nltk
import argparse
from collections import defaultdict

nnp_counter: int = 0
nn_counter: int = 0
vbz_counter: int = 0
dt_counter: int = 0
other_counter: int = 0

sequence: str = ""
text: str = ""
result: str = ""
words = defaultdict(int)

parser = argparse.ArgumentParser()
parser.add_argument("-s", type=str)
parser.add_argument("-t", type=str)
parser.add_argument("-o", type=str)
parser.add_argument("-i", type=str)
args = parser.parse_args()

if args.s is not None:
    text = nltk.word_tokenize(args.s)
    sequence = args.s
elif args.i is not None:
    try:
        text_file = open(args.i)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    else:
        sequence = text_file.read()
        text = nltk.word_tokenize(sequence)
        text_file.close()
else:
    sequence = input("Write a sequence: ")
    text = nltk.word_tokenize(sequence)

print("Sequence: {}".format(sequence))
result += "Sequence: {}\n".format(sequence)
tagged_text = nltk.pos_tag(text)

for num in range(len(tagged_text)):
    word: str = tagged_text[num][0]
    word_type: str = tagged_text[num][1]
    if word_type == "NNP":
        nnp_counter += 1
    elif word_type == "NN":
        nn_counter += 1
    elif word_type == "VBZ":
        vbz_counter += 1
    elif word_type == "DT":
        dt_counter += 1
    else:
        other_counter += 1
    if word_type == args.t:
        words[word] += 1

if args.t is None:
    print("Proper Noun (NNP): {}".format(nnp_counter))
    print("Common Noun (NN): {}".format(nn_counter))
    print("Verb 3rd person (VBZ): {}".format(vbz_counter))
    print("Determiners (DT): {}".format(dt_counter))
    print("Other (*): {}".format(other_counter))

    result += "Proper Noun (NNP): {}\n".format(nnp_counter)
    result += "Common Noun (NN): {}\n".format(nn_counter)
    result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
    result += "Determiners (DT): {}\n".format(dt_counter)
    result += "Other (*): {}\n".format(other_counter)
else:
    if args.t == "NNP":
        print("Proper Noun (NNP): {}".format(nnp_counter))
        result += "Proper Noun (NNP): {}\n".format(nnp_counter)
    elif args.t == "NN":
        print("Common Noun (NN): {}".format(nn_counter))
        result += "Common Noun (NN): {}\n".format(nn_counter)
    elif args.t == "VBZ":
        print("Verb 3rd person (VBZ): {}".format(vbz_counter))
        result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
    elif args.t == "DT":
        print("Determiners (DT): {}".format(dt_counter))
        result += "Determiners (DT): {}\n".format(dt_counter)
    srt = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
    for key, value in srt.items():
        print("Word '{}' occurs {} time(s).".format(key, value))
        result += "Word '{}' occurs {} time(s).\n".format(key, value)

if args.o is not None:
    try:
        text_file = open(args.o, "w")
    except FileNotFoundError as e:
        print("Error {}: File '{}' doesn't exist.".format(e, args.o), file=sys.stderr)
    else:
        text = text_file.write(result)
        text_file.close()
    finally:
        if result != "":
            print("Result has been saved to file '{}'.".format(args.o))
        else:
            print("There is no content to save.")
