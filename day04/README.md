# day04 — UniProt FASTA fetcher

This small project fetches a protein FASTA sequence from UniProt using a gene name.

What it does
- Prompts the user to enter a gene name (for example: `KRAS`).
- Searches the UniProt REST API for that gene and takes the first search result.
- Downloads the FASTA sequence for that UniProt entry.
- Saves the FASTA to a local file named `<GENE>_<UNIPROT_ID>.fasta` (for example: `KRAS_P01116.fasta`).

Which API it uses
- UniProt REST API: https://rest.uniprot.org

Dependencies / Installation
1. Create (or activate) your Python environment.
2. Install the required package(s):

```powershell
python -m pip install -r requirements.txt
```

(At minimum this installs `requests`.)

How to run
- From the `day04` folder run the CLI and follow the prompt:

```powershell
python uniprot_cli.py
```

- The program prints progress messages and the path to the saved FASTA file.

Files included
- `uniprot_logic.py` — pure business logic:
  - `search_uniprot_by_gene(gene)` — search UniProt and return the first accession (or `None`).
  - `download_fasta(uniprot_id)` — download FASTA text for the accession.
  - `save_fasta(fasta_str, gene, uniprot_id, directory=None)` — save to file and return path.
- `uniprot_cli.py` — simple interactive CLI that calls the business logic.
- `requirements.txt` — lists `requests`.

How AI was used
- I used GitHub Copilot to help generate the project files and to suggest code snippets for calling the UniProt REST API and handling responses.
- Prompt example used to generate the initial implementation (shortened):

```
Create a small project in a folder called `day04` that asks the user for a gene name, searches the UniProt REST API for that gene, takes the first UniProt entry, downloads its FASTA sequence, and saves it to a local file named `<gene>_<uniprot_id>.fasta`. Provide `uniprot_logic.py` (pure business logic) and `uniprot_cli.py` (interactive CLI). Use `requests` and handle basic errors.
```

License / Notes
- This is a small educational example for a course assignment. Use responsibly and respect UniProt usage policies when performing large numbers of queries.
