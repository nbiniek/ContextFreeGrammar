'''
Context-Free Grammar String Generator
by Noah Biniek (binie005@umn.edu)
'''
class Random: #Pseudo-random integer generator using Park-Miller algorithm 
    def __init__(self,seed):
        self.seed = seed #Precondition: seed must be between 1 and (2^31 -2)
            
    def next(self):
        self.seed = (16807*self.seed) % (2147483648-1)
        return self.seed
    
    def choose(self,objects):
        return objects[self.next() % len(objects)]

class Grammar:
    def __init__(self,seed):
        self.rand = Random(seed)
        self.rules = {}
        
    def rule(self,left,rights):
        if self.rules.has_key(left):
            raise Exception, "Rule is already present."
        else:
            self.rules[left] = rights
            
    def generate(self):
        if self.rules.has_key('Start'):
            return self.generating(('Start',))
        else:
            raise Exception, "No 'Start' rule is present."
    def generating(self,right):
        result = ''
        for e in right:
            if self.rules.has_key(e):
                result += self.generating(self.rand.choose(self.rules[e]))
            else:
                result += (e + ' ')
        return result
    
    def setSeed(self,seed):
        self.rand = Random(seed)

G = Grammar(101)
G.rule('Noun',   (('cat',), ('boy',), ('dog',), ('girl',)))  
G.rule('Verb',   (('bit',), ('chased',), ('kissed',)))  
G.rule('Phrase', (('the', 'Noun', 'Verb', 'the', 'Noun'),))  
G.rule('Story',  (('Phrase',), ('Phrase', 'and', 'Story')))  
G.rule('Start',  (('Story', '.'),))

print(G.generate())         # the cat bit the dog .
print(G.generate())         # the girl chased the boy .
print(G.generate())         # the cat chased the boy and the boy kissed the cat .

G.setSeed(101)
print(G.generate())         # the cat bit the dog .

G.setSeed(102)
print(G.generate())         # the dog bit the dog and the girl chased the girl .
                