from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django import template
register = template.Library()

@register.filter
def author_details(author):
    if not isinstance(author, user_model):
        # return empty string as safe default
        return ""

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

  
@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
    return "</div>"

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}