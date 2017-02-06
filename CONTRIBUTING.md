# How to contribute

In order to contribute to this repository, please consult with the main contributors. 

If you have write permission to the repo, please follow the instructions below to make contributions. Use forks of the repo _only when necessary_ to make your contributions. A properly labelled branch is preferred over a fork (see below under __feature branches__). This allows people within the team to more easily track the work being done, especially in regards to issues.

## Branches

### master

This branch is the stable branch that is used for creating releases. 

In order to create a release, the developer should ensure all changes are pushed to this branch and create a tag.

### develop

Changes should not be made _directly_ to this branch (rather, via pull requests using __feature branches__). Changes in this branch are intended for preview purposes and, when ready, to be merged into the master branch.

### feature branches

In order to contribute a new feature or to fix a bug, please follow these recommended rules:

- Create a new branch from `develop`.
     * Use the naming convention `feature/<relevant name>`.
     * The name of the branch should reflect the work being done on the branch.
     * If you've created the branch locally, be sure to push your branch to GitHub.
- Once the branch has been created, associate a GitHub issue with the branch and assign a developer to the issue.
     * Please create an issue if one does not exist.
- Once the feature is deemed ready, a pull request should be created and used to pull the changes into develop. 
