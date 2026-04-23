import termcolor

genes = [
    {'gene': 'FRAT1', 'identifier':'ENSP00000360060'},
    {'gene': 'ADA', 'identifier':'ENSG00000196839'},
    {'gene': 'FXN', 'identifier':'ENSG00000165060'},
    {'gene': 'RNU6-269P', 'identifier':'ENSG00000212379'},
    {'gene': 'MIR633', 'identifier':'ENSG00000207552'},
    {'gene': 'TTTY4C', 'identifier':'ENSG00000228296'},
    {'gene': 'RBMY2YP', 'identifier':'ENSG00000227633'},
    {'gene': 'FGFR3', 'identifier':'ENSG00000068078'},
    {'gene': 'KDR', 'identifier':'ENSG00000128052'},
    {'gene': 'ANK2', 'identifier':'ENSG00000145362'}
]

if __name__ == "__main__":
    print("Dictionary of genes!")
    print(f"There are {len(genes)} genes in the database!")
    for gene in genes:
        print(f"{gene['gene']}: {gene['identifier']}")




