from epubcheck import EpubCheck

result = EpubCheck('Neuronal_circuits_of_fear_extinction.epub')

print(result.valid)
print('=' * 30)
print(result.messages)

# References:
# 1. https://www.w3.org/publishing/epubcheck/about/
# 2. https://w3c.github.io/epubcheck/docs/apps-and-tools/
# 3. https://pypi.org/project/epubcheck/
