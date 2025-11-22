"""
Business logic for UniProt operations.

Functions:
- search_uniprot_by_gene(gene) -> Optional[str]
- download_fasta(uniprot_id) -> str
- save_fasta(fasta_str, gene, uniprot_id, directory=None) -> str (filepath)

Uses the UniProt REST API at https://rest.uniprot.org
Requires the `requests` library.
"""
from __future__ import annotations

import os
from typing import Optional

import requests

BASE_URL = "https://rest.uniprot.org"


def search_uniprot_by_gene(gene: str) -> Optional[str]:
    """Search UniProt for the given gene name and return the primary UniProt accession.

    Returns None if no matches were found.

    Example: gene='KRAS' -> returns something like 'P01116'
    """
    if not gene or not gene.strip():
        raise ValueError("Gene name must be provided")

    url = f"{BASE_URL}/uniprotkb/search"
    params = {
        "query": f"gene:{gene}",
        "format": "json",
        "size": 1,
    }

    resp = requests.get(url, params=params, timeout=15)
    resp.raise_for_status()

    data = resp.json()
    results = data.get("results") or []
    if not results:
        return None

    first = results[0]
    # UniProt JSON uses 'primaryAccession' for the accession
    accession = first.get("primaryAccession") or first.get("accession")
    return accession


def download_fasta(uniprot_id: str) -> str:
    """Download the FASTA sequence for a UniProt accession.

    Raises requests.HTTPError on non-200 response.
    Returns the raw FASTA text.
    """
    if not uniprot_id:
        raise ValueError("UniProt ID must be provided")

    url = f"{BASE_URL}/uniprotkb/{uniprot_id}.fasta"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def _sanitize_filename_component(s: str) -> str:
    """Sanitize a string for safe filenames: replace spaces and slashes."""
    return s.replace(" ", "_").replace("/", "_")


def save_fasta(fasta_str: str, gene: str, uniprot_id: str, directory: Optional[str] = None) -> str:
    """Save the FASTA string to a file named <gene>_<uniprot_id>.fasta.

    Returns the full path to the saved file.
    """
    if fasta_str is None:
        raise ValueError("fasta_str must be provided")
    if not gene or not uniprot_id:
        raise ValueError("gene and uniprot_id must be provided")

    gene_safe = _sanitize_filename_component(gene.upper())
    uid_safe = _sanitize_filename_component(uniprot_id)
    filename = f"{gene_safe}_{uid_safe}.fasta"

    if directory:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
    else:
        filepath = filename

    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(fasta_str)

    return filepath
