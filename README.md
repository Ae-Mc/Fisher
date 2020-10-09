# Fisher
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Ae-Mc/Fisher/Python%20package)](https://github.com/Ae-Mc/Fisher/actions?query=workflow:"Python+package")
[![PyPI](https://img.shields.io/pypi/v/FisherExactTest?color=orange)](https://pypi.org/project/FisherExactTest/)

Pure Python realization of Fisher's exact test

Usage example:
```python
from FisherExactTest import FisherExact


print(FisherExact(504, 539,
                  504, 468))  # Decimal('0.1187334465023821683418832686')
```
