
def venn_ways(options):
    if not options.c:
        return 2
    if not options.d:
        return 3
    if not options.e:
        return 4
    if not options.f:
        return 5
    if options.f:
        return 6

def get_name(fname):
    return op.splitext(op.basename(fname))[0]


def actual_intersection(a, b):
    return len(a.intersect(b, u=True))

def jaccard_of_a(a, b):
    return a.jaccard(b,u=True)['jaccard']

#Calculate the fisher 
def fisher_of_a(a, b):
    return a.fisher(b,genome='mm9').two_tail

#Calculate the reldist 
def reldist_of_a(a, b):
    #return mean(a.reldist(b)['reldist'])
    return float(sum(a.reldist(b)['reldist'])) / max(len(a.reldist(b)['reldist']), 1)

def frac_of_a(a, b):
    len_a = float(len(a))
    return len(a.intersect(b, u=True)) / len_a

def enrichment_score(a, b, genome_fn, iterations=None, processes=None):
    results = a\
            .randomstats(b, new=True, genome_fn=genome_fn, iterations=iterations, processes=processes)
    return (results['actual'] + 1) / (results['median randomized'] + 1)

def create_matrix(beds, func, verbose=False, **kwargs):
    nfiles = len(beds)
    total = nfiles ** 2
    i = 0
    matrix = collections.defaultdict(dict)
    for fa in beds:
        a = BedTool(fa)
        for fb in beds:
            i += 1
            b = BedTool(fb)

            if verbose:
                sys.stderr.write(
                        '%(i)s of %(total)s: %(fa)s + %(fb)s\n' % locals())
                sys.stderr.flush()

            matrix[get_name(fa)][get_name(fb)] = func(a, b, **kwargs)

    return matrix

def pairewise_inter(args):
    if args.test:
    # insulator binding sites from ChIP-chip -- 4 proteins, 2 cell types
    # Genes Dev. 2009 23(11):1338-1350
        args.beds = [example_filename(i) for i in  [
                'Cp190_Kc_Bushey_2009.bed',
                'Cp190_Mbn2_Bushey_2009.bed',
                'CTCF_Kc_Bushey_2009.bed',
                'CTCF_Mbn2_Bushey_2009.bed',
                'SuHw_Kc_Bushey_2009.bed',
                'SuHw_Mbn2_Bushey_2009.bed',
                'BEAF_Mbn2_Bushey_2009.bed',
                'BEAF_Kc_Bushey_2009.bed'
                ]]

    if args.enrichment:
        FUNC = enrichment_score
        genome_fn = pybedtools.chromsizes_to_file(pybedtools.chromsizes(args.genome))
        kwargs = dict(genome_fn=genome_fn, iterations=args.iterations,
                processes=args.processes)

    elif args.frac:
        FUNC = frac_of_a
        kwargs = {}

    elif args.jaccard:
        FUNC = jaccard_of_a
        kwargs = {}

    elif args.fisher:
        FUNC = fisher_of_a
        kwargs = {}

    elif args.reldist:
        FUNC = reldist_of_a
        kwargs = {}

    else:
        FUNC = actual_intersection
        kwargs = {}

    t0 = time.time()
    matrix = create_matrix(beds=args.beds, func=FUNC, verbose=args.verbose, **kwargs)
    t1 = time.time()

    nfiles = len(args.beds)

    if args.verbose:
        sys.stderr.write('Time to construct %s x %s matrix: %.1fs' \
                % (nfiles, nfiles, (t1 - t0)) + '\n')
    keys = sorted(matrix.keys())

    sys.stdout.write("\t" + "\t".join(keys) + '\n')
    for k in keys:
        sys.stdout.write(k)
        for j in keys:
            sys.stdout.write('\t' + str(matrix[k][j]))
        sys.stdout.write('\n')
