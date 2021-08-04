from epubcheck import EpubCheck

result = EpubCheck('Neuronal_circuits_of_fear_extinction.epub', lang='en')

print(result.valid)
print('=' * 30)
print(result.messages)
