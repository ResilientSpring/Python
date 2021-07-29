# Reference: https://git-lfs.github.com/

# About storage and bandwidth usage
# When you commit and push a change to a file tracked with Git LFS,
# a new version of the entire file is pushed and the total file size is counted against
# the repository owner's storage limit.
# When you download a file tracked with Git LFS, the total file size is counted against
# the repository owner's bandwidth limit.
#
# Git LFS uploads do not count against the bandwidth limit.
# If you push a 500 MB file to Git LFS, you'll use 500 MB of your allotted storage and
# none of your bandwidth.
# If you make a 1 byte change and push the file again, you'll use another 500 MB of storage
# and no bandwidth, bringing your total usage for these two pushes to 1 GB of storage and
# zero bandwidth.
#
# If you download a 500 MB file that's tracked with LFS, you'll use 500 MB of the repository
# owner's allotted bandwidth.
# If a collaborator pushes a change to the file and you pull the new version to your local
# repository, you'll use another 500 MB of bandwidth, bringing the total usage for these two
# downloads to 1 GB of bandwidth.

# Every account using Git Large File Storage receives 1 GB of free storage and 1 GB a month of
# free bandwidth.

# Reference:
# https://docs.github.com/en/github/managing-large-files/versioning-large-files/about-storage-and-bandwidth-usage
