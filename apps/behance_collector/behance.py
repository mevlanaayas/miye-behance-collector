from apps.website.media import Project
from .web_automat import find_links
from selenium import webdriver


def gatherer():
    script_to_func = """
        function mine(){ 
            var link_array = [];
            var view_array = [];
            var like_array = [];
            var project_name_array = [];
            for (i = 0; i < document.getElementsByClassName('rf-project-cover__image-container js-project-cover-image-link js-project-link').length ; i++){
            link_array[i] = document.getElementsByClassName('rf-project-cover__image-container js-project-cover-image-link js-project-link')[i].href;
            like_array[i] = document.getElementsByClassName('rf-project-cover__stat-number')[2*i].innerHTML;
            view_array[i] = document.getElementsByClassName('rf-project-cover__stat-number')[2*i + 1].innerHTML;
            project_name_array[i] = document.getElementsByClassName('rf-project-cover__title js-project-cover-title-link')[i].innerText;
            }
            var total = [];
            total[0] = link_array;
            total[1] = like_array;
            total[2] = view_array;
            total[3] = project_name_array;
            return total; 
        }
        return mine();
    """
    driver = webdriver.Firefox()
    url = 'https://www.behance.net/selingurbuz'
    # url = 'https://www.behance.net/ummiyemazlec55'
    # TODO: send get request to url, if not found warn user
    # TODO: use try-except to handle and report script fault
    default_array = find_links(url=url, driver=driver, script=script_to_func)
    project_links = default_array[0]
    # TODO: update script to retrieve project names
    # TODO: if project_links and project_count does not match, warn user
    like_count = default_array[1]
    view_count = default_array[2]
    project_names = default_array[3]
    script_to_func = """
        function mine(){ 
            var link_array = [];
            var keyword_array = [];
            var published_date;
            var description;
            var tag_array = [];
            var tool_array = [];
            for (i = 0; i < document.getElementsByClassName('js-project-lightbox-link project-module-image-inner-wrap lightbox-link hover-icon-enabled').length ; i++){
                link_array[i] = document.getElementsByClassName('js-project-lightbox-link project-module-image-inner-wrap lightbox-link hover-icon-enabled')[i].children[1].src; 
            }
            for (i = 0; i < document.getElementsByClassName('project-fields-field').length / 2 ; i++){
                keyword_array[i] = document.getElementsByClassName('project-fields-field')[i].innerText;
            }
            if(document.getElementsByClassName('project-tools__list-item').length != 0){
                for (i = 0; i < document.getElementsByClassName('project-tools__list-item').length ; i++){
                    tool_array[i] = document.getElementsByClassName('project-tools__list-item')[i].innerText;
                }
            }else{
                for (i = 0; i < document.getElementsByClassName('tooltipi-container').length ; i++){
                    tool_array[i] = document.getElementsByClassName('tooltipi-container')[0].children[0].title
                }
            }
            if (document.getElementsByClassName('object-tag').length != 0){
                for (i = 0; i < document.getElementsByClassName('object-tag').length ; i++){
                    tag_array[i] = document.getElementsByClassName('object-tag')[i].innerText;
                }
            }
            if (document.getElementsByClassName('js-format-timestamp').length != 0){
                published_date = document.getElementsByClassName('js-format-timestamp')[0].innerText;
            }
            if (document.getElementsByClassName('js-basic-info-description').length != 0){
                description = document.getElementsByClassName('js-basic-info-description')[0].innerText;
            }
            var return_array = [];
            return_array[0] = link_array;
            return_array[1] = keyword_array;
            return_array[2] = published_date;
            return_array[3] = description;
            return_array[4] = tool_array;
            return_array[5] = tag_array;
            return return_array;
        }
        return mine();
    """
    projects = {}
    project_list = []
    count = 0
    for link in project_links:
        project_name = project_names[count]
        project_name = project_name.replace("'", "")
        project_array = find_links(url=link, driver=driver, script=script_to_func)
        image_links = project_array[0]
        keyword_array = project_array[1]
        published_date = project_array[2]
        description = project_array[3]
        tool_array = project_array[4]
        tag_array = project_array[5]
        tool_array = list(set(tool_array))

        if description is None:
            description = 'There is no given description.'
        else:
            description = description.replace("'", "")
        if tool_array is None:
            tool_array = ['There is no given tools used.']
        if tag_array is None:
            tag_array = ['There is no given tag.']

        project_list.append(
            Project(
                project_title=project_name,
                poster_image=image_links[0],
                publish_date=published_date,
                project_desc=description,
                keywords=keyword_array,
                tags=tag_array,
                tools=tool_array,
                all_images_links=image_links,
                view_count=view_count[count],
                like_count=like_count[count],
            )
        )
        count = count + 1
    driver.close()
    return project_list
