# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Amrfinder(Package):
    """NCBI AMRFinderPlus: This software and the accompanying database identify
       acquired antimicrobial resistance genes in bacterial protein and/or
       assembled nucleotide sequences as well as known resistance-associated
       point mutations for several taxa. With AMRFinderPlus we added select
       members of additional classes of genes such as virulence factors,
       biocide, heat, acid, and metal resistance genes."""

    homepage = "https://github.com/ncbi/amr/wiki"
    url      = "https://github.com/ncbi/amr/releases/download/amrfinder_v3.10.24/amrfinder_binaries_v3.10.24.tar.gz"


    version('3.10.24', sha256='fce299c980cda740dcc4f53f9b2dc9061c856213e5bdbc2c339185a5fb7dcf6a')

    depends_on('blast-plus')
    depends_on('hmmer')
    depends_on('curl')


    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('amrfinder', prefix.bin)
        install('amrfinder_update', prefix.bin)
        install('amr_report', prefix.bin)
        install('dna_mutation', prefix.bin)
        install('fasta2parts', prefix.bin)
        install('fasta_check', prefix.bin)
        install('fasta_check', prefix.bin)
        install('gff_check', prefix.bin)
