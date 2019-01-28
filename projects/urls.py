from django.conf.urls import url
from .views import(
    home,
    profile,
    projects,
    post_projects,
    search_projects,
    update_profile,
    draft_idea,
    search_projects,
    sign_out
)

urlpatterns=[
    url(r'^home/',home,name='home'),
    url(r'^profile/',profile,name='profile'),
    url(r'^update_profile/',update_profile,name='update_profile'),
    url(r'^projects/',projects,name='projects'),
    url(r'^draft_idea/',draft_idea,name='drafts'),
    url(r'^post_projects/',post_projects,name='post_projects'),
    url(r'^search_projects/',search_projects,name='search'),
    url(r'^sign_out/',sign_out,name='sign_out'),
]