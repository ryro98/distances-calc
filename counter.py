#!/usr/bin/env python3
import sys
import nltk
import argparse
from collections import defaultdict


def counter():
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
    parser.add_argument("-s", "--sequence", type=str, help='Write a sequence, which the program will analyze.')
    parser.add_argument("-t", "--type", type=str, help="Write a type, which the program will use.")
    parser.add_argument("-o", "--output", type=str, help="Write a path to output file.")
    parser.add_argument("-i", "--input", type=str, help="Write a path to input file.")
    args = parser.parse_args()

    if args.sequence is not None:
        if args.input is not None:
            print("Error: You cannot use 'sequence' and 'input' parameters at the same time.", file=sys.stderr)
            sys.exit(1)
        text = nltk.word_tokenize(args.sequence)
        sequence = args.sequence
    elif args.input is not None:
        try:
            text_file = open(args.input)
        except FileNotFoundError as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        else:
            for line in text_file:
                sequence += line
            text = nltk.word_tokenize(sequence)
            text_file.close()
    else:
        sequence = input("Write a sequence: ")
        text = nltk.word_tokenize(sequence)

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
        if word_type == args.type:
            words[word] += 1

    if args.output is None:
        if args.type is None:
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
            if args.type == "NNP":
                print("Proper Noun (NNP): {}".format(nnp_counter))
                result += "Proper Noun (NNP): {}\n".format(nnp_counter)
            elif args.type == "NN":
                print("Common Noun (NN): {}".format(nn_counter))
                result += "Common Noun (NN): {}\n".format(nn_counter)
            elif args.type == "VBZ":
                print("Verb 3rd person (VBZ): {}".format(vbz_counter))
                result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
            elif args.type == "DT":
                print("Determiners (DT): {}".format(dt_counter))
                result += "Determiners (DT): {}\n".format(dt_counter)
            srt = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
            for key, value in srt.items():
                print("Word '{}' occurs {} time(s).".format(key, value))
                result += "Word '{}' occurs {} time(s).\n".format(key, value)
    else:
        if args.type is None:
            result += "Proper Noun (NNP): {}\n".format(nnp_counter)
            result += "Common Noun (NN): {}\n".format(nn_counter)
            result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
            result += "Determiners (DT): {}\n".format(dt_counter)
            result += "Other (*): {}\n".format(other_counter)
        else:
            if args.type == "NNP":
                result += "Proper Noun (NNP): {}\n".format(nnp_counter)
            elif args.type == "NN":
                result += "Common Noun (NN): {}\n".format(nn_counter)
            elif args.type == "VBZ":
                result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
            elif args.type == "DT":
                result += "Determiners (DT): {}\n".format(dt_counter)
            srt = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
            for key, value in srt.items():
                result += "Word '{}' occurs {} time(s).\n".format(key, value)
        try:
            text_file = open(args.output, "w")
        except FileNotFoundError as e:
            print("Error {}: File '{}' doesn't exist.".format(e, args.output), file=sys.stderr)
        else:
            text_file.write(result)
            text_file.close()
        finally:
            if result != "":
                print("Result has been saved to file '{}'.".format(args.output))
            else:
                print("There is no content to save.")


if "__main__" == __name__:
    counter()
