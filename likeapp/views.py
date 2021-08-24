from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])

        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)
        # 이 유저가 이 게시글에 좋아요를 찍었는지 찾아봄

        if like_record.exists():
            # 좋아요 반영 X
            messages.add_message(request, messages.ERROR, '좋아요는 한 번만 가능합니다')
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk': kwargs['article_pk']}))
        else:
            # 좋아요 반영 O
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()
        # save를 꼭 해줘야 like 추가한 게 반영이 됨

        messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다')

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})
