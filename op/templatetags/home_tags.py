# from django import template
#
# from blog.models import Category, Article, Blog
# from user.models import UserArticleViewed
#
# register = template.Library()
#
#
# @register.simple_tag
# def category():
#     return Category.objects.all()
#
# 
# @register.simple_tag
# def article_all():
#     return Article.objects.all().order_by('?')
#
#
# @register.simple_tag
# def user_last_view(request):
#     return UserArticleViewed.objects.filter(user=request.user).order_by("-modify_at")
#
#
# @register.simple_tag
# def blog_all():
#     return Blog.objects.all().order_by("?")
#
#
# @register.simple_tag
# def blog_fav(request):
#     return Blog.objects.filter(BlogUserFav__user=request.user).order_by("?")
#
#
# @register.filter
# def order_by(queryset, args):
#     args = [x.strip() for x in args.split(',')]
#     return queryset.order_by(*args)
#
#
#
