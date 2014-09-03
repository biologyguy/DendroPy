#! /usr/bin/env python

##############################################################################
##  DendroPy Phylogenetic Computing Library.
##
##  Copyright 2010-2014 Jeet Sukumaran and Mark T. Holder.
##  All rights reserved.
##
##  See "LICENSE.txt" for terms and conditions of usage.
##
##  If you use this work or any portion thereof in published work,
##  please cite it as:
##
##     Sukumaran, J. and M. T. Holder. 2010. DendroPy: a Python library
##     for phylogenetic computing. Bioinformatics 26: 1569-1571.
##
##############################################################################

"""
Models of canonical tree shapes.
"""

import dendropy

def star_tree(taxon_namespace):
    "Builds and returns a star tree from the given taxa block."
    star_tree = dendropy.Tree(taxon_namespace=taxon_namespace)
    for taxon in taxon_namespace:
        star_tree.seed_node.new_child(taxon=taxon)
    return star_tree

