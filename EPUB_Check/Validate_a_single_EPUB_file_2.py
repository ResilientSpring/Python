import pandas as pd
from epubcheck import EpubCheck

# Check to see if the epub file can be accessed by others in the same package.
dataframe = pd.read_csv(filepath_or_buffer='Neuronal_circuits_of_fear_extinction.epub')
# Good! The IDE did detect the epub file and auto-complete the remaining file name input.

result = EpubCheck(infile='Neuronal_circuits_of_fear_extinction.epub', lang='EN')
print(result.valid)
print('=' * 30)
print(result.messages)
