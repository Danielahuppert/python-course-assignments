"""
Simple CLI for fetching UniProt FASTA by gene name.

Usage:
    python uniprot_cli.py

It will prompt for a gene name, search UniProt, download the first result's FASTA,
and save it as <GENE>_<UNIPROT_ID>.fasta in the current directory.

Requires `requests` (used by uniprot_logic).
"""
from __future__ import annotations

import sys

from uniprot_logic import search_uniprot_by_gene, download_fasta, save_fasta


def main() -> int:
    try:
        gene = input("Enter gene name (e.g. KRAS): ").strip()
        if not gene:
            print("No gene provided. Exiting.")
            return 1

        print(f"Searching UniProt for gene '{gene}'...")
        accession = search_uniprot_by_gene(gene)
        if not accession:
            print(f"No UniProt entries found for gene '{gene}'.")
            return 1

        print(f"Found UniProt accession: {accession}")
        print(f"Downloading FASTA for {accession}...")
        fasta = download_fasta(accession)

        filename = save_fasta(fasta, gene, accession)
        print(f"Saved FASTA to: {filename}")
        return 0

    except Exception as exc:
        print(f"Error: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
