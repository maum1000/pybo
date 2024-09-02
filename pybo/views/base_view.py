from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question ,Comment

def index(request):


    #입력값
    page = request.GET.get('page','1')
    #조회
    question_list = Question.objects.order_by('-create_date')

    paginator = Paginator(question_list,10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request,'pybo/question_list.html',context)


def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question,pk=question_id)

    #조회수 증가하기
    question.view_count += 1

    #print(question.view_count)
    question.save()

    # 댓글이 있으면 댓글정보까지 넘겨주기

    #comments = Comment.objects.filter(parent__isnull=True).prefetch_related('replies')

    #질문에 있는 연결된 정보 넘겨주기
    #
    comments = question.comments.filter(parent__isnull=True)
    #print(str(question.comments.filter(parent__isnull=True).query))
    # 등록된 모든 댓글을 보기
    # all_comments = Comment.objects.filter(question=question)
    # print(all_comments)
    #comments = question.comments.filter(parent__isnull=True).order_by('-create_date').prefetch_related('replies')
    #comments_reply = Comment.objects.filter(parent__in=comments).order_by('-create_date')
    #context = {'question': question, 'comments': comments,'comments_reply': comments_reply}
    context = {'question': question , 'comments': comments}

    return render(request,'pybo/question_detail.html',context)

