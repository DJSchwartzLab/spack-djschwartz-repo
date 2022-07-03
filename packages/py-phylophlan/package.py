# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyPhylophlan(PythonPackage):
    """PhyloPhlAn 3.0 is an integrated pipeline for large-scale
    phylogenetic profiling of genomes and metagenomes."""

    homepage = "https://github.com/biobakery/phylophlan"
    url      = "https://github.com/biobakery/phylophlan/archive/refs/tags/3.0.2.tar.gz"

    version('3.0.2', sha256='c342116662bbfbb49f0665291fc7c0be5a0d04a02a7be2da81de0322eb2256b4')

    depends_on('python@3:')
    depends_on('py-numpy@1.12.1:')
    depends_on('py-biopython@1.70:')
    depends_on('py-dendropy@4.2.0:')
    depends_on('muscle')
    depends_on('blast-plus')
    depends_on('diamond')
