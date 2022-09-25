### Tasks 1 - 4 (**staging**)

```bash
Running with gitlab-runner 15.3.0~beta.42.gdb7789ca (db7789ca)
  on blue-1.shared.runners-manager.gitlab.com/default j1aLDqxS
Preparing the "docker+machine" executor
00:09
Using Docker executor with image ruby:2.5 ...
Pulling docker image ruby:2.5 ...
Using docker image sha256:27d049ce98db4e55ddfaec6cd98c7c9cfd195bc7e994493776959db33522383b for ruby:2.5 with digest ruby@sha256:ecc3e4f5da13d881a415c9692bb52d2b85b090f38f4ad99ae94f932b3598444b ...
Preparing environment
00:01
Running on runner-j1aldqxs-project-38258104-concurrent-0 via runner-j1aldqxs-shared-1661669484-ec6f4de3...
Getting source from Git repository
00:01
$ eval "$CI_PRE_CLONE_SCRIPT"
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/uchakovm/ci-cd-08-01/.git/
Created fresh repository.
Checking out fa589703 as main...
Skipping Git submodules setup
Executing "step_script" stage of the job script
00:01
Using docker image sha256:27d049ce98db4e55ddfaec6cd98c7c9cfd195bc7e994493776959db33522383b for ruby:2.5 with digest ruby@sha256:ecc3e4f5da13d881a415c9692bb52d2b85b090f38f4ad99ae94f932b3598444b ...
$ echo "Do your deploy here to ${TARGET_ENV}"
Do your deploy here to staging
$ echo "MY_LOGIN = ${MY_LOGIN}"
MY_LOGIN = env_staging_login
$ echo "MY_PASSWORD = ${MY_PASSWORD}"
MY_PASSWORD = env_staging_password
Cleaning up project directory and file based variables
00:00
Job succeeded
```

### Tasks 1 - 4 (**prod**)

```bash
Running with gitlab-runner 15.3.0~beta.42.gdb7789ca (db7789ca)
  on blue-5.shared.runners-manager.gitlab.com/default -AzERasQ
Preparing the "docker+machine" executor
00:06
Using Docker executor with image ruby:2.5 ...
Pulling docker image ruby:2.5 ...
Using docker image sha256:27d049ce98db4e55ddfaec6cd98c7c9cfd195bc7e994493776959db33522383b for ruby:2.5 with digest ruby@sha256:ecc3e4f5da13d881a415c9692bb52d2b85b090f38f4ad99ae94f932b3598444b ...
Preparing environment
00:01
Running on runner--azerasq-project-38258104-concurrent-0 via runner-azerasq-shared-1661669408-0f04c92a...
Getting source from Git repository
00:01
$ eval "$CI_PRE_CLONE_SCRIPT"
Fetching changes with git depth set to 20...
Initialized empty Git repository in /builds/uchakovm/ci-cd-08-01/.git/
Created fresh repository.
Checking out fa589703 as main...
Skipping Git submodules setup
Executing "step_script" stage of the job script
00:01
Using docker image sha256:27d049ce98db4e55ddfaec6cd98c7c9cfd195bc7e994493776959db33522383b for ruby:2.5 with digest ruby@sha256:ecc3e4f5da13d881a415c9692bb52d2b85b090f38f4ad99ae94f932b3598444b ...
$ echo "Do your deploy here to ${TARGET_ENV}"
Do your deploy here to prod
$ echo "MyLogin ${MY_LOGIN}"
MyLogin env_prod_login
$ echo "MY_PASSWORD = ${MY_PASSWORD}"
MY_PASSWORD = env_prod_password
Cleaning up project directory and file based variables
00:00
Job succeeded
```

### Tasks 5

  <details>
    <summary>stop_pipelines.py</summary>

  ```python
  import requests
  import sys

  url = f"https://gitlab.com/api/v4/projects/{sys.argv[2]}/pipelines"
  headers = {"PRIVATE-TOKEN" : sys.argv[1] }
  r = requests.get(url, headers=headers)

  import json

  if(r.status_code == 200):
      for a in json.loads(r.text):
          if (a['ref'] == f"{sys.argv[3]}"):
              url = f"https://gitlab.com/api/v4/projects/{sys.argv[2]}/pipelines/{a['id']}/cancel"
              r = requests.post(url, headers=headers)
              if(r.status_code == 200):
                  print(f"{a['id']} is stopped")
  ```

  </details>

<br>

```bash
uchakov@ansible:~$ python3 stop_pipelines.py [masked] 38258104 main
624737489 is stopped
624736789 is stopped
624736009 is stopped
624735722 is stopped
624732781 is stopped
624729564 is stopped
624729348 is stopped
624728950 is stopped
624728525 is stopped
624728232 is stopped
624728184 is stopped
624721557 is stopped
624720237 is stopped
624716592 is stopped
624716303 is stopped
624715456 is stopped
624714107 is stopped
624714041 is stopped
624713507 is stopped
624713483 is stopped
```