# Environment setup

## Create jenkins docker container for tests execution
```bash
Ubuntu:
cd hello_pytest
docker build -t jenkins:pytest .
docker run -p 8080:8080 -v /user/home/var/jenkins_home jenkins:pytest

Windows:
cd hello_pytest
docker build -t jenkins:pytest .
docker run -p 8080:8080 -v /user/home/var/jenkins_home jenkins:pytest
```


## Create and configure jenkins pipeline
```bash
Create ci/cd pipeline project and configure script path to "ci_cd.jenkinsfile" from repository
Activate "Poll SCM" and put "* * * * *" to Schedule field
Choose in "Additional Behaviours" option "Don't trigger a build on commit notifications"
```
## Run pipeline
```bash
Run created ci/cd pipeline
```