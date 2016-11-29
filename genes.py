from .ucscdb import DbWrapper

db = DbWrapper()


def genes_crossing_position(chrom_id, position):
    """
    Returns all genes starting before and ending after the given position
    :param chrom_id: alt locus or chrom id
    :param position: offset
    :return: Returns a list of dicts (each element representing one gene)
    """
    query = r"SELECT k.*, r.geneSymbol as gname FROM knownGene k, kgXref r where r.kgID = k.name AND k.chrom LIKE '%s' and k.txStart < %d and k.txEnd > %d" % (chrom_id, position, position)
    res = db.fetch_all(query)
    return _genes_to_dict(res)


def get_alt_genes():
    """
    Returns all genes starting before and ending after the given position
    :param chrom_id: alt locus or chrom id
    :param position: offset
    :return: Returns a list of dicts (each element representing one gene)
    """
    query = r'SELECT g.*, k.geneSymbol FROM knownGene g, kgXref k where k.kgID=g.name AND g.chrom like "%alt%"'
    res = db.fetch_all(query)
    return _genes_to_dict(res)


def get_main_genes():
    """
    Returns all genes starting before and ending after the given position
    :param chrom_id: alt locus or chrom id
    :param position: offset
    :return: Returns a list of dicts (each element representing one gene)
    """
    query = r'SELECT g.*, k.geneSymbol FROM knownGene g, kgXref k where k.kgID=g.name AND g.chrom not like "%\_%"'
    res = db.fetch_all(query)
    return _genes_to_dict(res)


def get_gene(gene_id):
    """
    :param self:
    :param gene_id: The ucsc gene id (NOT gene symbol)
    :return: Returns a dict with the gene information
    """
    query = r"""SELECT g.*, k.geneSymbol FROM knownGene g, kgXref k
                where k.kgID=g.name AND name='%s'""" % gene_id
    res = db.fetch_all(query)
    return _genes_to_dict(res)[0]


def _genes_to_dict(genes):
    """
    Takes a list of raw genes dicts from db,
    returns a nicer dict (e.g. exons into list)
    """
    out = []
    for gene in genes:

        gene["exonStarts"] = [int(p) for p in
                gene["exonStarts"].decode('utf8').split(",")[:-1]]  # remove last, which always is empty
        gene["exonEnds"] = [int(p) for p in
                gene["exonEnds"].decode('utf8').split(",")[:-1]]  # remove last, which always is empty
        out.append(gene)

    return out


if __name__ == "__main__":
    #gene = get_gene("uc011jmc.2")
    genes = get_alt_genes()
    print(genes)

