# ContextFreeGrammar

THEORY:

To generate random strings, we need an algorithm that generates random integers. An algorithm can’t generate truly random integers, but it can generate pseudo-random integers that seem random, even though they’re not. Python has its own random number generators, but for this project, the Park-Miller algorithm will be utilised. 

      The Park-Miller algorithm (named for its inventors) is a simple way to generate a sequence of pseudo-random integers. It works like this. Let n₀ be an integer called the seed. The seed is the first term of the sequence, and must be between 1 and 2³¹ − 2, inclusive. Starting from the seed, later terms n₁, n₂, ... are produced by the following equation.

  n<sub>k+1</sub> = (75 n<sub>k</sub>) % (2<sup>31</sup> − 1)

Here 7⁵ is 16807, and 2³¹ is 2147483648. The operator % returns the remainder after dividing one integer by another. We always get the same sequence of integers for a given seed. For example, if we start with the seed 101, then we get a sequence whose first few terms are 1697507, 612712738, 678900201, 695061696, 1738368639, 246698238, 1613847356, and 1214050682. 
      Some of these integers are large, but we can make them smaller by using the % operator again. If n is an integer from the sequence, then n % m gives us an integer between 0 and m − 1, inclusive. For example, if we need a pseudo-random integer from 0 to 9, then we write n % 10. We can use this fact to choose a random element from a Python list or tuple. If S is a list or tuple, then the Python expression S[n % len(S)] returns a randomly chosen element of S. 
      Now that we know how to generate pseudo-random integers, we can talk about what a grammar is like. The easiest way to do this is by showing an example. Here is the grammar that generated the simple sentences about boys, cats, dogs, and girls that appeared in the introduction.

1   Noun →  'cat' | 'boy' | 'dog' | 'girl'

2   Verb →  'bit' | 'chased' | 'kissed'

3   Phrase →  'the' Noun Verb 'the' Noun

4   Story  →  Phrase | Phrase 'and' Story

5  Start  →  Story '.'

Each line is a rule, identified by a number, so the grammar has five rules. The names in italics, like Noun, Verb, and Phrase, are called nonterminals. The strings in quotes, like 'girl', 'the', and '.', are called terminals. In each rule, the arrow ‘→’ means is replaced by, and the bar ‘|’ means or. As a result, rule 1 says that the nonterminal Noun can be replaced by one of the terminals 'cat', 'boy', 'dog', or 'girl'. Similarly, rule 5 says that the nonterminal Start can be replaced by the nonterminal Story and the terminal '.'. 
      To generate strings from the grammar, we play a kind of game. The game begins with the nonterminal Start. The object of the game is to use the rules to get rid of the nonterminals, replacing them by terminals. If we can do that, then the terminals left over at the end of the game are a string generated by the grammar. For example, we may begin with Start and use rule 5 to replace it, like this.

Story '.'

Now we have a new nonterminal, Story. According to rule 4, we can replace Story by either Phrase, or by Phrase 'and' Story. We choose the second option, so we have this.

Phrase 'and' Story '.'

We’ll use rule 4 again, but this time replace Story by Phrase.

Phrase 'and' Phrase '.'

We’ll use rule 3 to replace the first Phrase, so we get this.

'the' Noun Verb 'the' Noun 'and' Phrase '.'

According to rule 1, we can replace the first Noun by 'cat', and the second Noun by 'boy'.

'the' 'cat' Verb 'the' 'boy' 'and' Phrase '.'

And according to rule 2, we can replace Verb by 'chased'.

'the' 'cat' 'chased' 'the' 'boy' 'and' Phrase '.'

Continuing the game, we use rule 3 again to replace Phrase.

'the' 'cat' 'chased' 'the' 'boy' 'and' 'the' Noun Verb 'the' Noun '.'

We use rule 1 to replace the first Noun by 'boy', and the second Noun by 'cat'.

'the' 'cat' 'chased' 'the' 'boy' 'and' 'the' 'boy' Verb 'the' 'cat' '.'

Finally, we use rule 2 to replace Verb by 'kissed'.

'the' 'cat' 'chased' 'the' 'boy' 'and' 'the' 'boy' 'kissed' 'the' 'cat' '.'

We got rid of all the nonterminals, so we won the game. If we concatenate all the individual strings together, then we get the final string that was generated by the grammar. This is one of the example sentences that appeared in the introduction.

the cat chased the boy and the boy kissed the cat .

There are many different kinds of grammars, each with slightly different kinds of rules. The grammars we use for this assignment are called context-free grammars. Their rules have single nonterminals on the left side of the arrow ‘→’.
