## Game Mechanics

* Professors have an area of expertise
* Students have interests in certain areas
* Student acceptance mechanics
* The manager builds classrooms and alocate professors to them
* Money, wages, investments
* Education comittee evaluates the instituition

## Code Organization
* Python 3.5.2 and PyGame 1.9.4
* ThisIsAClass, this_is_an_attribute, thisIsAMethod()

## Git
The `master` and `develop` [approach](https://nvie.com/posts/a-successful-git-branching-model/).
### Main Branches
#### master
The origin/master is the main branch where HEAD always reflects a _production-ready_ state.

### develop
The origin/develop is the main branch where HEAD always reflects a state with the lates delivered development changes for the next release. When develop is stable and ready to be released, all changes should be merged back into master and tagged with a release number. Every time changes are merged back into master, this is a new production release.

### Supporting Branches
#### Feature Branches
May only branch off from develop and must merge back into develop.

To create: `git checkout -b myfeature develop`

Finishing the branch:
```
git checkout develop
git merge --no-ff myfeature
git branch -d myfeature
git push origin develop
```

#### Release Branches
May only branch off from develop and must merge back into develop and master. Naming convention is "release-x.y.z".

To create:
```
git checkout -b release-x.y.z develop
# bump version
git commit -a -m "Bumped version number to x.y.z"
```

Finishing the branch:
```
git checkout master
git merge --no-ff release-x.y.z
git tag -a x.y.z
```
To keep changes in the release branch, merge it back into develop and remove release branch:
```
git checkout develop
git merge --no-ff release-x.y.z
git branch -d release-x.y.z
```

### Versioning

[Semver approach](https://semver.org/). Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards-compatible bug fixes.

Adicional labels: `a` for alpha, `b` for beta, `rc` for release candidate. They can receive incremental numbers too, eg. 0.0.1rc1
