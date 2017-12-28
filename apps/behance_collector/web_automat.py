import time


def find_links(url, driver, script):
    # Create a new instance of the Firefox driver
    # go to the google home page
    driver.get(url)

    # the page is ajax so the title is originally this:
    print(driver.title)

    # wait until web page loads
    time.sleep(10)

    # save projects links from page
    links = driver.execute_script(script=script)
    time.sleep(3)
    return links
