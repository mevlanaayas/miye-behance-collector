from .web_automat import find_links
from selenium import webdriver

# terrible syntax but only way it works that is. otherway it will reach 180 char limit. :Smiley
a = "return mine(); "
b = "function mine(){ "
c = "var link_array = []; "
d = "for (i = 0; i < document.getElementsByClassName('rf-project-cover__image-container "
e = "js-project-cover-image-link js-project-link').length ; i++){ "
f = "link_array[i] = document.getElementsByClassName('rf-project-cover__image-container "
g = "js-project-cover-image-link js-project-link')[i].href "
h = "} "
j = "return link_array; "
k = "} "
script_to_func = a + b + c + d + e + f + g + h + j + k

"""
return mine(); 
function mine(){ 
    var link_array = [];
    for (i = 0; i < document.getElementsByClassName('rf-project-cover__image-container
    js-project-cover-image-link js-project-link').length ; i++){
    link_array[i] = document.getElementsByClassName('rf-project-cover__image-container
    js-project-cover-image-link js-project-link')[i].href 
    }
    return link_array; 
}
"""
driver = webdriver.Firefox()
url = 'https://www.behance.net/ummiyemazlec55'
project_links = find_links(url=url, driver=driver, script=script_to_func)

a = "return mine(); "
b = "function mine(){ "
c = "var link_array = []; "
d = "for (i = 0; i < document.getElementsByClassName('js-project-lightbox-link "
e = "project-module-image-inner-wrap lightbox-link hover-icon-enabled').length ; i++){ "
f = "link_array[i] = document.getElementsByClassName('js-project-lightbox-link "
g = "project-module-image-inner-wrap lightbox-link hover-icon-enabled')[i].children[1].src "
h = "} "
j = "return link_array; "
k = "} "
script_to_func = a + b + c + d + e + f + g + h + j + k
"""
return mine();
function mine(){ 
    var link_array = [];
    for (i = 0; i < document.getElementsByClassName('js-project-lightbox-link
    project-module-image-inner-wrap lightbox-link hover-icon-enabled').length ; i++){
    link_array[i] = document.getElementsByClassName('js-project-lightbox-link
    project-module-image-inner-wrap lightbox-link hover-icon-enabled')[i].children[1].src 
    }
    return link_array; 
}
"""
project_image_links = {}
for link in project_links:
    project_name = link.split('/')[5]
    image_links = find_links(url=link, driver=driver, script=script_to_func)
    image_links_tuple = tuple(image_links)
    project_image_links[project_name] = image_links_tuple

driver.close()

# we have PROJECT_NAME : LINKS list here.
# lets use it
