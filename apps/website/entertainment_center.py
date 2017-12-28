from apps.website import media
from apps.website import fresh_tomatoes
from apps.behance_collector.behance import project_image_links

dark_knight = None
keys = project_image_links.keys()
projects = []
for key in keys:
    projects.append(
        media.Project(key,
                      'description',
                      project_image_links[key][0],
                      project_image_links[key]
                      )
                  )

fresh_tomatoes.open_projects_page(projects)
