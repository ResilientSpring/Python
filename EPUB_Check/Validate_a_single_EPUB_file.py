from epubcheck import EpubCheck

result = EpubCheck()

print(result.valid)
print(result.messages)

# References:
# 1. https://www.w3.org/publishing/epubcheck/about/
# 2. https://w3c.github.io/epubcheck/docs/apps-and-tools/
# 3. https://pypi.org/project/epubcheck/
