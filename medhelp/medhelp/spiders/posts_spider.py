import os

import scrapy
from bs4 import BeautifulSoup
from scrapy.exceptions import CloseSpider


class MedHelpPostSpider(scrapy.Spider):


    DIRECTORY = "posts"
    name = "medhelp"
    count = 0
    def start_requests(self):
        urls = [

            "http://www.medhelp.org/forums/General-Health/show/164?page=1"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # if self.count > 50:
        #     raise CloseSpider('bandwidth_exceeded')

        self.count+=1
        print(self.count)

        page = ""
        curr_url = response.url
        # print(curr_url)
        # yielding a request here will go to the next page


        # this is the pipeline:
        # we go to a regular listing page, then we yield a SET of post pages (potentially with arguments; else we can just call a method)
        # to the next pages


        # OK, so we just need to use extractors/selectors to get the stuff we want. Their post class seems to be "subj_entry"
        # subj_entry -- GOOD
        # now, we just: nned to extract the content from each
        # good, this is what i want: response.css(".subj_entry .subj_title a::attr(href)")[0].extract()

        # we can yield a response.follow, and we will go to this page!
        # we could get the next page from the css, but instead we can just do this as an argument
        # keep going: once we get to the last one, then just dip (exit gracefully)


        # This also works: response.css(".page_nav")[-1].extract()

        # OK, but a more scalable approach is:

        # Process the individual posts
        # posts = response.css(".subj_entry .subj_title a::attr(href)")[0].extract()
        posts = response.css(".subj_entry .subj_title a::attr(href)").extract()
        # for each post, make sure to yield a new page to follow to
        for post in posts:
            # print(post)
            # construct the new url
            next_url = response.urljoin(post)
            yield scrapy.Request(next_url, callback=self.post_parse)


        # Process the top-level pages
        x = response.css(".page_nav")[-1]
        next_page = x.css("a::attr(href)").extract_first()

        next_url = response.urljoin(next_page)
        yield scrapy.Request(next_url, callback=self.parse)


    def post_parse(self,response):
        print("parsing " + response.url)
        # for now, we only get the title and the post contents, and save it to a file (we can build the concat func later)
        title = response.css(".subj_title::text").extract_first().replace("/", "-")

        # The pseudo selector is failing us here
        # contents = response.css("#subject_msg::text").extract_first()
        contents = response.css("#subject_msg::text").extract() # the contents might be a bit... (make sure to look over all of it)

        final_string_content = ''.join(contents)
        # for content in contents:

        # hence, we pass it into BS4
        # soup = BeautifulSoup(contents)
        # print(soup.div.string)
        # contents = soup.div.string
        # do VERY minor preprocessing here:
        final_string_content = final_string_content.replace(u'\xa0', u'')

        # now, let's save everything

        filename = title + "#" + response.url.split('/')[-1]

        # the output directory depends on where you invoke scrapy--make sure you do it in a folder or else it's gonna blow up
        # with open(os.path.join(self.DIRECTORY,filename), "w") as file:
        with open(filename, "w") as file:
            file.write(response.url + "\r\n")
            file.write("{}\r\n{}".format(title, final_string_content ))
            # file.write(contents)

        # print (response.url)
        return

