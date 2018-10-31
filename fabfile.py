import os

from fabric.decorators import task
from fabric.api import local

import utils


@task
def setup():
    utils.print_info("Setting up cap-examples")
    if not os.path.exists("settings.py"):
        utils.print_info("Setting up settings.py")
        local("cp settings.example.py settings.py")
    if not os.path.exists("./data"):
        utils.print_info("Setting up /data directory")
        local("mkdir data")
        
    utils.print_info("Installing requirements")
    local("pip install -r requirements.txt")


@task
def get_cases(jurisdiction="Illinois"):
    """
    Gets 500 cases for jurisdiction
    """
    utils.get_cases(jurisdiction)
    return


@task
def show_api_url():
    url = utils.get_api_url()
    print(url)
    return url


@task
def list_jurisdictions():
    jurisdictions = utils.get_jurisdictions()
    for jurisdiction in jurisdictions:
        print(jurisdiction['name_long'])
    return jurisdictions


@task
def list_whitelisted_jurisdictions():
    jurisdictions = utils.get_jurisdictions()
    utils.print_info("Whitelisted jurisdictions")
    for jurisdiction in jurisdictions:
        if jurisdiction["whitelisted"]:
            print(jurisdiction['name_long'])
    return jurisdictions


@task
def list_blacklisted_jurisdictions():
    utils.print_info("Blacklisted jurisdictions")
    jurisdictions = utils.get_jurisdictions()
    for jurisdiction in jurisdictions:
        if not jurisdiction["whitelisted"]:
            print(jurisdiction['name_long'])
    return jurisdictions
