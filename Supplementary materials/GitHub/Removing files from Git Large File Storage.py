# Note that defining the file types Git LFS should track will not, by itself,
# convert any pre-existing files to Git LFS, such as files on other branches or
# in your prior commit history. To do that, use the git lfs migrate[1] command,
# which has a range of options designed to suit various potential use cases.[2]

# After you "remove" files from Git LFS, the Git LFS objects still exist on the remote storage
# and will continue to count toward your Git LFS storage quota.[3]

# "Convert" files in a Git repository to or from Git LFS pointers,
# or summarize Git file sizes by file type. The import mode converts Git files (i.e., blobs)
# to Git LFS, while the export mode does the reverse, and the info mode provides an informational
# summary which may be useful in deciding which files to import or export.[1]
#
# In all modes, by default git lfs migrate operates only on the currently checked-out branch,
# and only on files (of any size and type) added in commits which do not exist on any remote.
# Multiple options are available to override these defaults.[1]
#
# When converting files to or from Git LFS, the git lfs migrate command will only make changes
# to your local repository and working copy, never any remotes.
# This is intentional as the import and export modes are generally "destructive" in the sense
# that they rewrite your Git history, changing commits and generating new commit SHAs.
# (The exception is the "no-rewrite" import sub-mode; see [IMPORT (NO REWRITE)] for details.)[1]
#
# You should therefore always first commit or stash any uncommitted work before using the import
# or export modes, and then validate the result of the migration before pushing the changes
# to your remotes,
# for instance by running the info mode and by examining your rewritten commit history.[1]
#
# Once you are satisfied with the changes, you will need to force-push the new Git history of
# any rewritten branches to all your remotes.
# This is a step which should be taken with care, since you will be altering the Git history
# on your remotes.[1]

# You can "convert" your repository back to a plain Git repository with git lfs migrate export.[4]

# References:
# 1. https://github.com/git-lfs/git-lfs/blob/main/docs/man/git-lfs-migrate.1.ronn?utm_source=gitlfs_site&utm_medium=doc_man_migrate_link&utm_campaign=gitlfs
# 2. https://git-lfs.github.com/
# 3. https://docs.github.com/en/github/managing-large-files/removing-files-from-git-large-file-storage
# 4. https://github.com/git-lfs/git-lfs#getting-started
