# -*- coding: utf-8 -*-

import operator
from . import util


class Translator:
    def __init__(self, deinflector, dictionary):
        self.deinflector = deinflector
        self.dictionary = dictionary


    def findTerm(self, text, wildcards=False):
        groups = {}
        if wildcards and isinstance(text,list):
            self.processTerm(groups,u"".join(text),u"".join(text),root=text,wildcards=True)
        else:
            text = util.sanitize(text, wildcards=wildcards)

            for i in range(len(text), 0, -1):
                term = text[:i]

                dfs = self.deinflector.deinflect(term, self.validator)
                if dfs is None:
                    self.processTerm(groups, term, term, wildcards=wildcards)
                else:
                    for df in dfs:
                        self.processTerm(groups, term, **df)

        definitions = [self.formatResult(group) for group in groups.items()]
        definitions = sorted(
            definitions,
            reverse=True,
            key=lambda d: (
                len(d['source']),
                'P' in d['tags'],
                -len(d['rules']),
                d['expression']
            )
        )

        length = 0
        for result in definitions:
            length = max(length, len(result['source']))

        return definitions, length


    def findKanji(self, text):
        text = util.sanitize(text, kana=False)
        results = list()

        processed = dict()
        for c in text:
            if c not in processed:
                match = self.dictionary.findCharacter(c)
                if match is not None:
                    results.append(match)
                processed[c] = match

        return results


    def processTerm(self, groups, term, source, rules=list(), root=str(), wildcards=False):
        root = root or source

        for entry in self.dictionary.findTerm(root, wildcards):
            key = entry['expression'], entry['reading'], entry['glossary']
            if key not in groups:
                groups[key] = term, entry['defs'], entry['refs'], entry['tags'], source, rules


    def formatResult(self, group):
        (expression, reading, glossary), (term, defs, refs, tags, source, rules) = group
        return {
            'defs': defs,
            'refs': refs,
            'expression': expression,
            'reading': reading,
            'glossary': glossary,
            'rules': rules,
            'source': source,
            'term': term,
            'tags': tags,
            'language': u'Japanese'
        }


    def validator(self, term):
        return [d['tags'] for d in self.dictionary.findTerm(term)]
