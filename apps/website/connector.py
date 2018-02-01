from apps.behance_collector.behance import project_list
import os

project_json_template = """
        {
            'project_title' : 'unique_project_name',
            'poster_image' : 'unique_cover_image',
            'publish_date' : 'unique_publish_date',
            'project_desc' : 'unique_project_desc',
            'keywords' : 'unique_keywords',
            'tags' : 'unique_tags',
            'tools' : 'unique_tools',
            'all_images_links' : 'unique_all_images_links',
            'view_count' : 'unique_view_count',
            'like_count' : 'unique_like_count'
        },
        {'next_project':'next'}
"""

script_dir = os.path.dirname(__file__)
rel_path = "/resumeBuilder.js"
temp_rel_path = "/template.js"
abs_file_path = script_dir + rel_path
temp_file_path = script_dir + temp_rel_path


def render_js_file(int_project_list):
    count_zero = 0
    for project in int_project_list:
        if count_zero > 0:
            file_path = abs_file_path
        else:
            file_path = temp_file_path

        with open(file_path, 'r') as file:
            file_data = file.read()
            rendered_content = file_data.replace("'unique_project_name'", "'" + project.project_name + "'")
            rendered_content = rendered_content.replace("'unique_cover_image'", "'" + project.cover_image + "'")
            rendered_content = rendered_content.replace("'unique_publish_date'", "'" + project.project_publish_date + "'")
            rendered_content = rendered_content.replace("'unique_project_desc'", "'" + project.description + "'")
            rendered_content = rendered_content.replace("'unique_keywords'", str(project.keywords))
            rendered_content = rendered_content.replace("'unique_tags'", str(project.tags))
            rendered_content = rendered_content.replace("'unique_tools'", str(project.tools))
            rendered_content = rendered_content.replace("'unique_all_images_links'", str(project.images))
            rendered_content = rendered_content.replace("'unique_view_count'", project.view_count)
            rendered_content = rendered_content.replace("'unique_like_count'", project.like_count)
            rendered_content = rendered_content.replace("{'next_project':'next'}", project_json_template)
            file.close()
        with open(abs_file_path, 'w') as file:
            file.write(rendered_content)
            file.close()
        count_zero = count_zero + 1
    print('success')


def task_celery():
    render_js_file(project_list)


if __name__ == "__main__":
    render_js_file(project_list)
