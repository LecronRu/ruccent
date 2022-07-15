## Simple word accent setter.

Pure Python, no dependencies. Based on ngram model.

Trained for the Russian language, on a corpus of ~1000000 word forms, taking into account their frequency in real 
texts.  Accuracy ~97-98%. Speed ~10000 words per second.

```Python
from ruccent import Accent

accenter = Accent()
accenter.predict('пробойник')  # -> 4
```

You can train the model yourself for your language or corpus.
```Python
from ruccent import Accent, AccentTrain

# iterable of tuple (accent position, weight/frequency, word)
dataset = [(3, 10, 'begin'), (1, 1, 'happy')]
train = AccentTrain()
train.fit(dataset, ngram=(3,7))
train.save('path/yourself.model')

accenter = Accent('path/yourself.model')
accenter.predict('begin')
```
