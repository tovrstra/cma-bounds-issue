# Sticky bounds issue

This is just a temporary repository to demonstrate a sticky-bounds issue with CMA.

Steps to reproduce:

```bash
git clone git@github.com:tovrstra/cma-bounds-issue.git
cd cma-bounds-issue
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python bounds.py
python plot.py
```

The script `bounds.py` takes about xx minutes to complete.
It performs many CMA optimizations on the same surface, ...

The histograms of solutions plotted by the last script show a large number of solutions coinciding with the bounds.
