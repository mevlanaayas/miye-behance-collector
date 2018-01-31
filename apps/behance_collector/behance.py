from .web_automat import find_links
from selenium import webdriver

script_to_func = """
    function mine(){ 
        var link_array = [];
        var view_array = [];
        var like_array = [];
        for (i = 0; i < document.getElementsByClassName('rf-project-cover__image-container js-project-cover-image-link js-project-link').length ; i++){
        link_array[i] = document.getElementsByClassName('rf-project-cover__image-container js-project-cover-image-link js-project-link')[i].href;
        like_array[i] = document.getElementsByClassName('rf-project-cover__stat-number')[2*i].innerHTML;
        view_array[i] = document.getElementsByClassName('rf-project-cover__stat-number')[2*i + 1].innerHTML;
        }
        var total = [];
        total[0] = link_array;
        total[1] = like_array;
        total[2] = view_array;
        return total; 
    }
    return mine();
"""
driver = webdriver.Firefox()
url = 'https://www.behance.net/ummiyemazlec55'
default_array = find_links(url=url, driver=driver, script=script_to_func)
project_links = default_array[0]
# TODO: project_link ile projects sayısı çelişirse mail at
like_count = default_array[1]
view_count = default_array[2]
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
count = 0
for link in project_links:
    project_name = link.split('/')[5]
    project_array = find_links(url=link, driver=driver, script=script_to_func)
    image_links = project_array[0]
    keyword_array = project_array[1]
    published_date = project_array[2]
    description = project_array[3]
    tool_array = project_array[4]
    tag_array = project_array[5]

    image_links_tuple = tuple(image_links)
    keyword_array_tuple = tuple(keyword_array)
    tool_array_tuple = tuple(tool_array)
    tag_array_tuple = tuple(tag_array)

    projects[project_name + '_images'] = image_links_tuple
    projects[project_name + '_keywords'] = keyword_array_tuple
    projects[project_name + '_published'] = published_date
    projects[project_name + '_description'] = description
    projects[project_name + '_tools'] = tool_array_tuple
    projects[project_name + '_tags'] = tag_array_tuple
    projects[project_name + '_likes'] = like_count[count]
    projects[project_name + '_views'] = view_count[count]
    count = count + 1

driver.close()
