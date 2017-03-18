def to_rna(dna):
    d = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
            }
    try:
        rna = ''.join([d[e] for e in dna])
        return rna
    except KeyError:
        return ''
