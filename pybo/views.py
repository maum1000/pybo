from lib2to3.fixes.fix_input import context

from Tools.scripts.var_access_benchmark import read_dict
from django.db.transaction import commit
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Question, Answer,Comment
from django.utils import timezone
from .form import QuestionForm, AnswerForm,CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


