#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Add all projects in the maintainers team
"""
from __future__ import absolute_import, print_function

from . import github_login


# <Team [Core Maintainers]>
CORE_TEAM_ID = 1269917


def main():
    gh = github_login.login()
    org = gh.organization('oca')
    team = org.team(CORE_TEAM_ID)
    for repo in org.iter_repos():
        if not team.has_repo(repo):
            team.add_repo(repo)
            print('Added repository "%s"' % repo.name)

if __name__ == '__main__':
    main()
