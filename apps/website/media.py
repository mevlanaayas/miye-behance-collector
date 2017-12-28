
class Project:
    def __init__(self, project_title: object, project_desc: object, poster_image: object,
                 all_images_links: object) -> object:
        self.title = project_title
        self.description = project_desc
        self.poster_image_url = poster_image
        self.links = all_images_links
