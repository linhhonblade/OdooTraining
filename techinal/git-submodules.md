# [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)

Submodules allow you to keep a Git repository as a subdirectory of another Git repository.

## Starting with Submodules

Add a new submodule

```shell
$ Git submodule add https://github.com/chaconinc/DbConnector
Cloning into 'DbConnector'...
remote: Counting objects: 11, done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 11 (delta 0), reused 11 (delta 0)
Unpacking objects: 100% (11/11), done.
Checking connectivity... done.

$ Git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "Git reset HEAD <file>..." to unstage)

	new file:   .gitmodules
	new file:   DbConnector
```

`.gitmodules` is a configuration file that stores the mapping between your project's url and the local subdirectory you've pulled into:

```sheel
[submodule "DbConnector"]
	path = DbConnector
	url = https://github.com/chaconinc/DbConnector
```

Although `DbConnector` is a subdirectory in your working directory, Git sees it as a submodule and doesn’t track its contents when you’re not in that directory. Instead, Git sees it as a particular commit from that repository.

```shell
$ git commit -am 'Add DbConnector module'
[master fb9093c] Add DbConnector module
 2 files changed, 4 insertions(+)
 create mode 100644 .gitmodules
 create mode 160000 DbConnector
```

Push the changes:
```shell
$ git push origin master
```

## Cloning a project with submodules

When you clone such a project, by default you get the directories that contain submodules, but none of the files within them yet.

The DbConnector directory is there, but empty. You must run two commands: `git submodule init` to initialize your local configuration file, and `git submodule update` to fetch all the data from that project and check out the appropriate commit listed in your superproject

If you pass `--recurse-submodules` to the git clone command, it will automatically initialize and update each submodule in the repository, including nested submodules if any of the submodules in the repository have submodules themselves.

You can combine the `git submodule init` and `git submodule update` steps by running `git submodule update --init`

To also initialize, fetch and checkout any nested submodules, you can use the foolproof `git submodule update --init --recursive`.

## Working on a Project with Submodules


