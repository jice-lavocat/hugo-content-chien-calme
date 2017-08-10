# pip install --upgrade algoliasearch
# pip3 install python-frontmatter
# pip3 install markdown
from algoliasearch import algoliasearch
import os
import frontmatter
import markdown

# Set the directory you want to start from
rootDir = './content/'


client = algoliasearch.Client("AR1LZLFH32", '5f96ac4b0b350803db25786ca8c19e8a')

for dirName, subdirList, fileList in os.walk(rootDir):
    # Actualites
    if "./content/actualites" in dirName:
        index = client.init_index("blog_posts")
        print('Found directory: %s' % dirName)

        for fname in fileList:
            print('\t%s' % fname)
            with open(dirName + "/" + fname) as f:
                post = frontmatter.load(f)
                # Content in markdown
                # print(post.content)
                # Metadata
                # print(post.metadata)

                md = markdown.Markdown()
                html_content = md.convert(post.content)

                # Building link
                base_url = "http://www.chien-calme.com/actualites/"
                if "url" in post.metadata:
                    url = post.metadata["url"]
                elif "slug" in post.metadata:
                    url = base_url + post.metadata["slug"]
                else:
                    if ".md" in fname:
                        url = base_url + fname[:-3] + "/"
                    elif ".html" in fname:
                        url = base_url + fname[:-5] + "/"

                algolia_object = post.metadata
                algolia_object["content"] = html_content
                try:
                    algolia_object["thumbnail"] = "http://www.chien-calme.com" + algolia_object["thumbnail"]
                except:
                    algolia_object["thumbnail"] = None
                algolia_object["url"] = url

                # print(algolia_object)

                res = index.add_object(algolia_object, url)

    # print('Found directory: %s' % dirName)
    # for fname in fileList:
    #     print('\t%s' % fname)
