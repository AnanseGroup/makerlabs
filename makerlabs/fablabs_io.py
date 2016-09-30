# -*- encoding: utf-8 -*-
#
# Access data from fablabs.io
#
# Author: Massimo Menichinelli
# Homepage: http://www.openp2pdesign.org
# License: LGPL v.3
#
#

import requests

# Endpoints
fablabs_io_labs_api_url_v0 = "https://api.fablabs.io/v0/labs.json"
fablabs_io_projects_api_url_v0 = "https://api.fablabs.io/v0/projects.json"


class FabLab(object):
    """Represents a Fab Lab as it is described on fablabs.io."""

    def __init__(self):
        self.address_1 = ""
        self.address_2 = ""
        self.address_notes = ""
        self.avatar = ""
        self.blurb = ""
        self.capabilities = ""
        self.city = ""
        self.country_code = ""
        self.county = ""
        self.description = ""
        self.email = ""
        self.header_image_src = ""
        self.id = ""
        self.kind_name = ""
        self.latitude = ""
        self.longitude = ""
        self.links = ""
        self.name = ""
        self.parent_id = ""
        self.phone = ""
        self.postal_code = ""
        self.slug = ""
        self.url = ""


class Project(object):
    """Represents a project as it is described on fablabs.io."""

    def __init__(self):
        self.id = ""
        self.title = ""
        self.description = ""
        self.github = ""
        self.web = ""
        self.dropbox = ""
        self.bitbucket = ""
        self.lab_id = ""
        self.owner_id = ""
        self.created_at = ""
        self.updated_at = ""
        self.vimeo = ""
        self.flickr = ""
        self.youtube = ""
        self.drive = ""
        self.twitter = ""
        self.facebook = ""
        self.googleplus = ""
        self.instagram = ""
        self.status = ""
        self.version = ""
        self.faq = ""
        self.scope = ""
        self.community = ""
        self.lookingfor = ""
        self.cover = ""


def data_from_fablabs_io(endpoint):
    """Gets data from fablabs.io."""

    data = requests.get(endpoint).json()

    return data


def get_labs(format):
    """Gets Fab Lab data from fablabs.io."""

    fablabs_json = data_from_fablabs_io(fablabs_io_labs_api_url_v0)
    fablabs = {}

    # Load all the FabLabs
    for i in fablabs_json["labs"]:
        current_lab = FabLab()
        current_lab.address_1 = i["address_1"]
        current_lab.address_2 = i["address_2"]
        current_lab.address_notes = i["address_notes"]
        current_lab.avatar = i["avatar"]
        current_lab.blurb = i["blurb"]
        current_lab.capabilities = i["capabilities"]
        current_lab.city = i["city"]
        current_lab.country_code = i["country_code"]
        current_lab.county = i["county"]
        current_lab.description = i["description"]
        current_lab.email = i["email"]
        current_lab.header_image_src = i["header_image_src"]
        current_lab.id = i["id"]
        current_lab.kind_name = i["kind_name"]
        current_lab.latitude = i["latitude"]
        current_lab.longitude = i["longitude"]
        current_lab.links = i["links"]
        current_lab.name = i["name"]
        current_lab.parent_id = i["parent_id"]
        current_lab.phone = i["phone"]
        current_lab.postal_code = i["postal_code"]
        current_lab.slug = i["slug"]
        current_lab.url = i["url"]
        fablabs[i["slug"]] = current_lab

    if format.lower() == "dict" or format.lower() == "json":
        output = {}
        for j in fablabs:
            output[j] = fablabs[j].__dict__
    elif format.lower() == "geojson" or format.lower() == "geo":
        pass
    elif format.lower() == "object" or format.lower() == "obj":
        output = fablabs
    else:
        output = fablabs

    return output


def labs_count():
    """Gets the number of current Fab Labs registered on fablabs.io."""

    fablabs = data_from_fablabs_io(fablabs_io_labs_api_url_v0)

    return len(fablabs["labs"])


def get_projects(format):
    """Gets projects data from fablabs.io."""

    projects_json = data_from_fablabs_io(fablabs_io_projects_api_url_v0)
    projects = {}
    project_url = "https://www.fablabs.io/projects/"

    # Load all the FabLabs
    for i in projects_json["projects"]:
        i = i["projects"]
        current_project = Project()
        current_project.id = i["id"]
        current_project.title = i["title"]
        current_project.description = i["description"]
        current_project.github = i["github"]
        current_project.web = i["web"]
        current_project.dropbox = i["dropbox"]
        current_project.bitbucket = i["bitbucket"]
        current_project.lab_id = i["lab_id"]
        current_project.owner_id = i["owner_id"]
        current_project.created_at = i["created_at"]
        current_project.updated_at = i["updated_at"]
        current_project.vimeo = i["vimeo"]
        current_project.flickr = i["flickr"]
        current_project.youtube = i["youtube"]
        current_project.drive = i["drive"]
        current_project.twitter = i["twitter"]
        current_project.facebook = i["facebook"]
        current_project.googleplus = i["googleplus"]
        current_project.instagram = i["instagram"]
        current_project.status = i["status"]
        current_project.version = i["version"]
        current_project.faq = i["faq"]
        current_project.scope = i["scope"]
        current_project.community = i["community"]
        current_project.lookingfor = i["lookingfor"]
        current_project.cover = i["cover"]
        projects[project_url + str(current_project.id)] = current_project

    if format.lower() == "dict" or format.lower() == "json":
        output = {}
        for j in projects:
            output[j] = projects[j].__dict__
    elif format.lower() == "geojson" or format.lower() == "geo":
        pass
    elif format.lower() == "object" or format.lower() == "obj":
        output = projects
    else:
        output = projects

    return output


def projects_count():
    """Gets the number of current projects submitted on fablabs.io."""

    projects = data_from_fablabs_io(fablabs_io_projects_api_url_v0)

    return len(projects["projects"])


if __name__ == "__main__":
    pass
