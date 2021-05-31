#!/usr/bin/env python3
import sys
import unittest

import nltk
import argparse
from collections import defaultdict
import unittest
from unittest.mock import patch, Mock, mock_open

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sequence", type=str, help='Write a sequence, which the program will analyze.')
parser.add_argument("-t", "--type", type=str,
                    help="Write a type of word, which the program will search in the sequence.")
parser.add_argument("-o", "--output", type=str, help="Write a path to output file.")
parser.add_argument("-i", "--input", type=str, help="Write a path to input file.")
args = parser.parse_args()


def counter(args):
    nnp_counter: int = 0
    nn_counter: int = 0
    vbz_counter: int = 0
    dt_counter: int = 0
    nns_counter: int = 0
    vbd_counter: int = 0
    in_counter: int = 0
    rb_counter: int = 0
    prp_counter: int = 0
    vbp_counter: int = 0
    to_counter: int = 0
    vb_counter: int = 0
    jj_counter: int = 0
    at_counter: int = 0
    beg_counter: int = 0
    ql_counter: int = 0
    cs_counter: int = 0
    bez_counter: int = 0
    other_counter: int = 0

    sequence: str = ""
    text: str = ""
    result: str = ""
    words = defaultdict(int)

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

    for pair in tagged_text:
        word: str = pair[0]
        word_type: str = pair[1]
        if word_type == "NNP":
            nnp_counter += 1
        elif word_type == "NN":
            nn_counter += 1
        elif word_type == "VBZ":
            vbz_counter += 1
        elif word_type == "DT":
            dt_counter += 1
        elif word_type == "NNS":
            nns_counter += 1
        elif word_type == "VBD":
            vbd_counter += 1
        elif word_type == "IN":
            in_counter += 1
        elif word_type == "RB":
            rb_counter += 1
        elif word_type == "PRP":
            prp_counter += 1
        elif word_type == "VBP":
            vbp_counter += 1
        elif word_type == "TO":
            to_counter += 1
        elif word_type == "VB":
            vb_counter += 1
        elif word_type == "JJ":
            jj_counter += 1
        elif word_type == "AT":
            at_counter += 1
        elif word_type == "BEG":
            beg_counter += 1
        elif word_type == "QL":
            ql_counter += 1
        elif word_type == "CS":
            cs_counter += 1
        elif word_type == "BEZ":
            bez_counter += 1
        else:
            other_counter += 1
        if word_type == args.type:
            words[word] += 1

    if args.output is None:
        if args.type is None:
            if nnp_counter > 0:
                print("Proper Noun (NNP): {}".format(nnp_counter))
                result += "Proper Noun (NNP): {}\n".format(nnp_counter)
            if nn_counter > 0:
                print("Common Noun (NN): {}".format(nn_counter))
                result += "Common Noun (NN): {}\n".format(nn_counter)
            if vbz_counter > 0:
                print("Verb 3rd person (VBZ): {}".format(vbz_counter))
                result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
            if dt_counter > 0:
                print("Determiners (DT): {}".format(dt_counter))
                result += "Determiners (DT): {}\n".format(dt_counter)
            if nns_counter > 0:
                print("Common noun plural (NNS): {}".format(nns_counter))
                result += "Common noun plural (NNS): {}\n".format(nns_counter)
            if vbd_counter > 0:
                print("Verb in past tense (VBD): {}".format(vbd_counter))
                result += "Verb in past tense (VBD): {}\n".format(vbd_counter)
            if in_counter > 0:
                print("Preposition (IN): {}".format(in_counter))
                result += "Preposition (IN): {}\n".format(in_counter)
            if rb_counter > 0:
                print("Adverb (RB): {}".format(rb_counter))
                result += "Adverb (RB): {}\n".format(rb_counter)
            if prp_counter > 0:
                print("Possessive pronoun (PRP): {}".format(prp_counter))
                result += "Possessive pronoun (PRP): {}\n".format(prp_counter)
            if vbp_counter > 0:
                print("Verb, sing. present (VBP): {}".format(vbp_counter))
                result += "Verb, sing. present (VBP): {}\n".format(vbp_counter)
            if to_counter > 0:
                print("To (TO): {}".format(to_counter))
                result += "To (TO): {}\n".format(to_counter)
            if vb_counter > 0:
                print("Verb (VB): {}".format(vb_counter))
                result += "Verb (VB): {}\n".format(vb_counter)
            if jj_counter > 0:
                print("Adjective (JJ): {}".format(jj_counter))
                result += "Adjective (JJ): {}\n".format(jj_counter)
            if at_counter > 0:
                print("At (AT): {}".format(at_counter))
                result += "At (AT): {}\n".format(at_counter)
            if beg_counter > 0:
                print("Beg (BEG): {}".format(beg_counter))
                result += "Beg (BEG): {}\n".format(beg_counter)
            if ql_counter > 0:
                print("Ql (QL): {}".format(ql_counter))
                result += "Ql (QL): {}\n".format(ql_counter)
            if cs_counter > 0:
                print("Cs (CS): {}".format(cs_counter))
                result += "Cs (CS): {}\n".format(cs_counter)
            if bez_counter > 0:
                print("Bez (BEZ): {}".format(bez_counter))
                result += "Bez (BEZ): {}\n".format(bez_counter)
            if other_counter > 0:
                print("Other (*): {}".format(other_counter))
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
            elif args.type == "NNS":
                print("Common noun plural (NNS): {}".format(nns_counter))
                result += "Common noun plural (NNS): {}\n".format(nns_counter)
            elif args.type == "VBD":
                print("Verb in past tense (VBD): {}".format(vbd_counter))
                result += "Verb in past tense (VBD): {}\n".format(vbd_counter)
            elif args.type == "IN":
                print("Preposition (IN): {}".format(in_counter))
                result += "Preposition (IN): {}\n".format(in_counter)
            elif args.type == "RB":
                print("Adverb (RB): {}".format(rb_counter))
                result += "Adverb (RB): {}\n".format(rb_counter)
            elif args.type == "PRP":
                print("Possessive pronoun (PRP): {}".format(prp_counter))
                result += "Possessive pronoun (PRP): {}\n".format(prp_counter)
            elif args.type == "VBP":
                print("Verb, sing. present (VBP): {}".format(vbp_counter))
                result += "Verb, sing. present (VBP): {}\n".format(vbp_counter)
            elif args.type == "TO":
                print("To (TO): {}".format(to_counter))
                result += "To (TO): {}\n".format(to_counter)
            elif args.type == "VB":
                print("Verb (VB): {}".format(vb_counter))
                result += "Verb (VB): {}\n".format(vb_counter)
            elif args.type == "JJ":
                print("Adjective (JJ): {}".format(jj_counter))
                result += "Adjective (JJ): {}\n".format(jj_counter)
            elif args.type == "AT":
                print("At (AT): {}".format(at_counter))
                result += "At (AT): {}\n".format(at_counter)
            elif args.type == "BEG":
                print("Beg (BEG): {}".format(beg_counter))
                result += "Beg (BEG): {}\n".format(beg_counter)
            elif args.type == "QL":
                print("Ql (QL): {}".format(ql_counter))
                result += "Ql (QL): {}\n".format(ql_counter)
            elif args.type == "CS":
                print("Cs (CS): {}".format(cs_counter))
                result += "Cs (CS): {}\n".format(cs_counter)
            elif args.type == "BEZ":
                print("Bez (BEZ): {}".format(bez_counter))
                result += "Bez (BEZ): {}\n".format(bez_counter)
            srt = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
            for key, value in srt.items():
                print("Word '{}' occurs {} time(s).".format(key, value))
                result += "Word '{}' occurs {} time(s).\n".format(key, value)
    else:
        if args.type is None:
            if nnp_counter > 0:
                result += "Proper Noun (NNP): {}\n".format(nnp_counter)
            if nn_counter > 0:
                result += "Common Noun (NN): {}\n".format(nn_counter)
            if vbz_counter > 0:
                result += "Verb 3rd person (VBZ): {}\n".format(vbz_counter)
            if dt_counter > 0:
                result += "Determiners (DT): {}\n".format(dt_counter)
            if nns_counter > 0:
                result += "Common noun plural (NNS): {}\n".format(nns_counter)
            if vbd_counter > 0:
                result += "Verb in past tense (VBD): {}\n".format(vbd_counter)
            if in_counter > 0:
                result += "Preposition (IN): {}\n".format(in_counter)
            if rb_counter > 0:
                result += "Adverb (RB): {}\n".format(rb_counter)
            if prp_counter > 0:
                result += "Possessive pronoun (PRP): {}\n".format(prp_counter)
            if vbp_counter > 0:
                result += "Verb, sing. present (VBP): {}\n".format(vbp_counter)
            if to_counter > 0:
                result += "To (TO): {}\n".format(to_counter)
            if vb_counter > 0:
                result += "Verb (VB): {}\n".format(vb_counter)
            if jj_counter > 0:
                result += "Adjective (JJ): {}\n".format(jj_counter)
            if at_counter > 0:
                result += "At (AT): {}\n".format(at_counter)
            if beg_counter > 0:
                result += "Beg (BEG): {}\n".format(beg_counter)
            if ql_counter > 0:
                result += "Ql (QL): {}\n".format(ql_counter)
            if cs_counter > 0:
                result += "Cs (CS): {}\n".format(cs_counter)
            if bez_counter > 0:
                result += "Bez (BEZ): {}\n".format(bez_counter)
            if other_counter > 0:
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
            elif args.type == "NNS":
                result += "Common noun plural (NNS): {}\n".format(nns_counter)
            elif args.type == "VBD":
                result += "Verb in past tense (VBD): {}\n".format(vbd_counter)
            elif args.type == "IN":
                result += "Preposition (IN): {}\n".format(in_counter)
            elif args.type == "RB":
                result += "Adverb (RB): {}\n".format(rb_counter)
            elif args.type == "PRP":
                result += "Possessive pronoun (PRP): {}\n".format(prp_counter)
            elif args.type == "VBP":
                result += "Verb, sing. present (VBP): {}\n".format(vbp_counter)
            elif args.type == "TO":
                result += "To (TO): {}\n".format(to_counter)
            elif args.type == "VB":
                result += "Verb (VB): {}\n".format(vb_counter)
            elif args.type == "JJ":
                result += "Adjective (JJ): {}\n".format(jj_counter)
            elif args.type == "AT":
                result += "At (AT): {}\n".format(at_counter)
            elif args.type == "BEG":
                result += "Beg (BEG): {}\n".format(beg_counter)
            elif args.type == "QL":
                result += "Ql (QL): {}\n".format(ql_counter)
            elif args.type == "CS":
                result += "Cs (CS): {}\n".format(cs_counter)
            elif args.type == "BEZ":
                result += "Bez (BEZ): {}\n".format(bez_counter)
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
    counter(args)


class CounterTests(unittest.TestCase):
    @patch('builtins.print')
    def test_argument_sequence(self, mock_print):
        args.sequence = "Ala"
        counter(args)
        mock_print.assert_called_with("Common Noun (NN): 1")

    @patch('builtins.print')
    def test_argument_type(self, mock_print):
        args.type = "NNP"
        args.sequence = "Ala has a cat."
        counter(args)
        mock_print.assert_called_with("Word 'Ala' occurs 1 time(s).")

    @patch('builtins.print')
    def test_argument_input(self, mock_print):
        test_file = open("test_file_input.txt", "w")
        test_file.write("Ala")
        test_file.close()
        args.input = "test_file_input.txt"
        counter(args)
        mock_print.assert_called_with("Common Noun (NN): 1")

    @patch('builtins.print')
    def test_argument_output(self, mock_print):
        args.sequence = "Ala has a cat."
        args.output = "test_file_output.txt"
        counter(args)
        mock_print.assert_called_with("Result has been saved to file 'test_file_output.txt'.")

    @patch('builtins.print')
    def test_arguments_sequence_and_input(self, mock_print):
        args.sequence = "Ala has a cat."
        test_file = open("test_file_input.txt", "w")
        test_file.write("Ala")
        test_file.close()
        args.input = "test_file_input.txt"
        counter(args)
        mock_print.assert_called_with("Common Noun (NN): 1")
