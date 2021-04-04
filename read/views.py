from django.shortcuts import render
from read.models import Chapter, Course
# Create your views here.
def index(request):
    return render(request, 'read/index.html')

def read(request):
    return render(request, 'read/read.html')


def get_chapter(request, chapter_id):
    chapter = Chapter.objects.get(id = int(chapter_id))
    course = chapter.course
    chapter_list = Chapter.objects.filter(course = course)

    all_chapter = Chapter.objects.all()
        # 判断chaper_id是否为1或者最后一个
    if chapter.id == 1:
        previous_id = 1
        next_id = 2
        previous_chapter = Chapter.objects.get(id = previous_id)
        next_chapter = Chapter.objects.get(id = next_id)
        previous_text = "当前页是第一章"
        next_text = "下一篇：" + next_chapter.name

    elif chapter.id == len(all_chapter):
        previous_id = chapter.id-1
        next_id = chapter.id
        previous_chapter = Chapter.objects.get(id = previous_id)
        next_chapter = Chapter.objects.get(id = next_id)
        previous_text = "上一篇：" + previous_chapter.name
        next_text = "当前页是最后一章"

    # 如果不，则取到平常状态下的前一篇和后一篇的id
    else:
        previous_id = chapter.id - 1
        next_id = chapter.id + 1
        previous_chapter = Chapter.objects.get(id = previous_id)
        next_chapter = Chapter.objects.get(id = next_id)
        previous_text = "上一篇：" + previous_chapter.name
        next_text = "下一篇：" + next_chapter.name

    # 根据id取出前一篇和后一篇章节的数据
    # previous_chapter = Chapter.objects.get(id = previous_id)
    # next_chapter = Chapter.objects.get(id = next_id)

    return render(request, 'read/chapter.html',{
        'chapter':chapter,
        'chapter_list': chapter_list,
        'course': course,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter,
        'previous_text': previous_text,
        'next_text': next_text,
        })

def get_course(request, course_id):
    course = Course.objects.get(id = int(course_id))
    chapter_list = Chapter.objects.filter(course = course)
    leibie = course.leibie
    relat_course_list = Course.objects.filter(leibie = leibie)
    return render(request, 'read/course.html',{
        'course':course,
        'chapter_list':chapter_list,
        'relat_course_list': relat_course_list
        })