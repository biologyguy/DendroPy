#! /usr/bin/env python

import dendropy
from dendropy.calculate import treestat

tree = dendropy.Tree.get_from_path("pythonidae.mle.nex", "nexus")
pdm = treestat.PatristicDistanceMatrix(tree)
for i, t1 in enumerate(tree.taxon_namespace):
    for t2 in tree.taxon_namespace[i+1:]:
        print("Distance between '%s' and '%s': %s" % (t1.label, t2.label, pdm(t1, t2)))
