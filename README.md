# Python Templating for CodeSpace

## About
This is Python sample application to work with Github Codesapce. Built using Python3.11 and Poetry.

## How to
### Use codespace
- make a fork of current repository
- open the subfolder in codespace
- build container
	- press f1
	- run build container command
- run `poetry run codespace`
- should be showing either `Hello World` or open at port 8080 on the `aiohttp` branch

Alternatively, you can also:
- create new repo
- run
```
git clone --bare https://github.com/exampleuser/public_repo.git
cd public_repo.git
git push --mirror https://github.com/yourname/private_repo.git
cd ..
rm -rf public-repo.git
```
- open with codespace
