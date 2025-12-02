blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
trending = 0

for views in blog_views:
    if views > 1000:
        print("trending")
        trending += 1
    elif views >= 500:
        print("average")
    else:
        print("low traffic")
print(sum(blog_views))
print(trending)