# pip install python-wordpress-xmlrpc
from wordpress_xmlrpc import Client, WordPressPost, WordPressPage
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import posts


wp = Client('http://ridicurious.com/xmlrpc.php', 'prateek@ridicurious.com', 'Durg@v@ti@123')
#posts = wp.call(GetPosts())
#posts = Client.call(posts.GetPosts())
pages = Client.call(posts.GetPosts({'post_type': 'page'}, results_class=WordPressPage))

print(dir(pages))

#print(dir(posts[0]))
#for post in posts:
#    print('title: {}, status: {}, id: {}, link: {}'.format(post.title, post.post_status, post.id, post.link))
