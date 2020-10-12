#!/usr/bin/env python

import random
import csv


class Word:
    def __init__(self, cases, gender):
        self.cases = cases
        self.gender = gender
        
    def __str__(self):
        return self.cases[0]

def create_adj(adj):
    if adj[-1] == "í":
        mas = [adj, adj + "ho", adj + "m"]
        fem = [adj, adj, adj]
        neu = mas
        return {"mas":mas,"fem":fem,"neu":neu}
    else:
        sub = adj[:-1]
        mas = [sub + "ý",sub + "ého",sub + "ém"]
        fem = [sub + "á",sub + "é",sub + "é"]
        neu = [sub + "é",sub + "ého",sub + "ém"]
        return {"mas":mas,"fem":fem,"neu":neu}
    
NOUNS = []
ADJS = []
with open("words.csv","r",encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        NOUNS.append(Word([row["nom"],row["gen"],row["lok"]],row["gender"]))
        ADJS.append(create_adj(row["adj"]))
    

def course(length):
    if length == 1: return noun()
    split = random.randrange(1,length)
    i = random.randrange(6)
    if i == 0: return adj(course(length-1))
    elif i == 1: return teorie(course(length-1))
    elif i == 2: return nauka(course(length-1))
    elif i == 3: return uvod(course(length-1))
    elif i == 4: return v(course(split),course(length-split))
    elif i == 5: return a(course(split),course(length-split))

def noun():
    return random.choice(NOUNS)
    '''
    if case == "nom": return random.choice(NOUNS).nom
    elif case == "gen": return random.choice(NOUNS).gen
    else: return random.choice(NOUNS).lok
    '''

def adj(word):
    cases = []
    for i in range(3):
        cases.append(random.choice(ADJS)[word.gender][i] + " " + word.cases[i])
    return Word(cases, word.gender)

def teorie(word):
    cases = []
    cases.append("teorie " + word.cases[1])
    cases.append("teorie " + word.cases[1])
    cases.append("teorii " + word.cases[1])
    return Word(cases, "fem")

def nauka(word):
    cases = []
    cases.append("nauka o " + word.cases[2])
    cases.append("nauky o " + word.cases[2])
    cases.append("nauce o " + word.cases[2])
    return Word(cases, "fem")

def uvod(word):
    cases = []
    cases.append("úvod do " + word.cases[1])
    cases.append("úvodu do " + word.cases[1])
    cases.append("úvodu do " + word.cases[1])
    return Word(cases, "mas")

def v(word1,word2):
    cases = []
    vve = " v "
    if word2.cases[2][0] in ["v","š"]: vve = " ve "
    for i in range(3):
        cases.append(word1.cases[i] + vve + word2.cases[2])
    return Word(cases, word1.gender)

def a(word1,word2):
    cases = []
    for i in range(3):
        cases.append(word1.cases[i] + " a " + word2.cases[i])
    return Word(cases, word1.gender)
    


random.seed()
for i in range(2000):
	text = course(random.randint(2,4)).cases[0] # set number of words
	words = text.split()
	if len(words) == len(set(words)): print(text)

