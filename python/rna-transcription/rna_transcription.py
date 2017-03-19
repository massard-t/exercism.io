def to_rna(dna):
    d = {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U'
            }
    try:
        return ''.join([d[e] for e in dna])
    except KeyError:
        return ''
