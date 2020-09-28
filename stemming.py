#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:14:04 2020

@author: ridhhi
"""

import nltk

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """
            Hello America!

            I want to thank all the speakers and performers today for reminding us, through song and through words, just what it is that we love about America. I want to thank all of you for braving the cold and the crowds and traveling in some cases thousands of miles to join us here today. Welcome to Washington, and welcome to this celebration of American renewal.

            In the course of our history, only a handful of generations have been asked to confront challenges as serious as the ones we face right now. Our nation is at war. Our economy is in crisis. Millions of Americans are losing their jobs and their homes. They're worried about how they'll afford college for their kids or pay the stack of bills on their kitchen table. And most of all, they're anxious and uncertain about the future -- about whether this generation of Americans will be able to pass on what's best about this country to our children and their children.

            I won't pretend that meeting any one of these challenges will be easy. It will take more than a month or a year, and it will likely take many. Along the way there will be setbacks and false starts and days that test our resolve as a nation.

            But despite all this -- despite the enormity of the task that lies ahead -- I stand here today as hopeful as ever that the United States of America will endure, that it will prevail, that the dream of our Founders will live on in our time.

            What gives me hope is what I see when I look out across this mall. For in these monuments are chiseled those unlikely stories that affirm our unyielding faith -- a faith that anything is possible in America. Rising before us stands a memorial to a man who led a small band of farmers and shopkeepers in revolution against the army of an empire, all for the sake of an idea. 

            On the ground below is a tribute to a generation that withstood war and depression -- men and women like my grandparents who toiled on bomber assembly lines and marched across Europe to free the world from tyranny's grasp. Directly in front of us is a pool that still reflects the dream of a King, and the glory of a people who marched and bled so that their children might be judged by their character's content. And behind me, watching over the union he saved, sits the man who in so many ways made this day possible.

            And yet, as I stand here today, what gives me the greatest hope of all is not the stone and marble that surrounds us, but what -- what fills the spaces in between. It is you -- Americans of every race and region and station who came here because you believe in what this country can be and because you want to help us get there.
            """
            
sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ''.join(words)