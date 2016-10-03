# enon
A Python object that does everything while doing nothing.

## Usage
```
from enon import Enon, enon

with enon.open() as enon:
    enon.append(enon['horse'])
    enon_items = enon[1:5]
    zero = len(enon_items)
    enon.zero = zero
    if enon.zero is zero:
        raise Enon('Attribute assignment does nothing!')
    elif enon.zero is enon:
        # But this is correct.
        enon.write(str(enon))

other_enon = Enon('Init ignores...', all='Arguments')
if enon is other_enon:
    raise Enon('Not possible! They are not the same Enon!')
elif other_enon == enon:
    same_enon = other_enon('Enon is callable.',
                           more='It always returns itself.')
    assert other_enon is same_enon
```

## Best practices
No thank you.
