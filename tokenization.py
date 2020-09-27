#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:58:09 2020

@author: ridhhi
"""

import nltk

paragraph = """
            Madan Bhandari's contribution in Nepal's communist movement should be positively assessed for his successful democratization of the communist party and communist organization.
            Madan Bhandari is one politician of the Left on whom there has been significant discussion in the mainstream polity of Nepal. And yet, one feels that the narrative is inadequate. Despite all that has been written and said, the very fact that that he led a communist party makes academicians and writers hesitate to properly locate his contributions in Nepal’s 70 years of democratic struggle.
            On the one hand, Bhandari's admirers, particularly those who were his comrades during the democratic struggle and the workers of his party, venerate him to superhuman levels. They tend to focus on his positive personality traits, charismatic Marxist oratory informed by oriental philosophy and literature, which tends to overlook his concrete political contributions for the restoration and consolidation of multiparty democracy.
            On the other hand, his critics limit him to the ‘communist’ bracket informed by international experience and tropes, which in fact he had broken while leading his party into the democratic era of Nepal, working to make it accept universal democratic values through its fifth General Convention in 1993, just few months before the mysterious-looking car accident on the highway between Mugling and Narayanghat in central Nepal which took his life. He was only 41 at the time of his passing.
            Madan Kumar Bhandari, popularly addressed by his first and last name as Madan Bhandari, was born on 27 June 1951 in a village of Nepal's northeast mountain district of Taplejung. He completed his early schooling in a local Sanskrit school, and then went to Varanasi in India for further studies. In Nepal, those were the times when a brief window of democracy that people had opened through their struggle against the century old Rana oligarchy had just been forcefully closed; popularly elected Prime Minister and social-democrat leader BP Koirala was ousted in a coup led by King Mahendra; and many pro-democracy leaders had exiled themselves to India for safety, which also allowed them to continue their political activism.
            In Varanasi, the northern cultural city of India, Bhandari pursued Sanskrit literature and then went to Dehradun for two years where he came in contact with Nepali youths influenced by communist ideology. On his return to Varanasi in 1969, Bhandari got admission in Banaras Hindu University (BHU). His political leanings immediately drew him to the communist party led by Pushpa Lal Shrestha.
            Bhandari's interaction with Nepali Congress leaders, his education in BHU and Pushpa Lal's guidance shaped his early political ideas to a great extent. The Nepali Congress (NC), professing social-democratic ideology, used to keep a distance from the communists. Pushpa Lal, the founder of the Nepal Communist Party, however, had a firm belief that the NC and communists needed to join hands to have any realistic chance to restore multi-party democracy in Nepal.
            In 1968, BP Koirala was released from prison following international as well as Indian pressure on King Mahendra. ‘BP’, as he was known, moved to India and established contact with his Nepali and international friends. In that era, coinciding with the height of Cold War, BP was under pressure to maintain a distance from the communists. The idea of a joint democratic movement of the NC and the communists never gained traction until as long as BP and Pushpa Lal lived despite both leaders having reconciled in principle the need for this.
            Madan Bhandari, as a student and as one of the editors of the party's mouthpiece 'Mukti Morcha', was closely following these political developments. With the prospect of a joint mass struggle looking distant, Madan Bhandari, still keeping a low profile among 'senior' comrades, rebelled against Pushpa Lal and reached out to the communist group in Jhapa district which had come into the limelight in 1972 by 'physically eliminating class enemies', drawing inspirations from the Naxalite movement in the West Bengal state of India just across the border.
            """
            
#Tokenization
sentences = nltk.sent_tokenize(paragraph)

#Tokenization
words = nltk.word_tokenize(paragraph)