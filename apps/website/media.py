
class Project:
    def __init__(self, project_title, poster_image, publish_date, project_desc, keywords, tags, tools,
                 all_images_links, view_count, like_count):
        self.project_name = project_title
        self.cover_image = poster_image
        self.project_publish_date = publish_date
        self.description = project_desc
        self.keywords = keywords
        self.tags = tags
        self.tools = tools
        self.images = all_images_links
        self.view_count = view_count
        self.like_count = like_count
