from django.core.management.base import BaseCommand
import os
from os.path import dirname
import json
from api.models import *
from bs4 import BeautifulSoup as BS
from os.path import basename, splitext


def process_image_src_html(html, standard, subject, book, topics):
    base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
    location = base_dir + 'books' + '/' + standard + '/' + subject + '/' + book + '/html' + '/' + topics + '/' + 'img' + '/'
    soup = BS(html, features='html.parser')
    for img in soup.findAll('img'):
        img['src'] = location + splitext(basename(img['src']))[0]
    converted_html = str(soup)
    return converted_html

class Command(BaseCommand):
    help = ''' Make sure you have run all the migrations to the database.
           this command will look for all the json files inside books folder present in root directory'''

    def handle(self, *args, **kwargs):
        base_dir = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))

        for standard in os.listdir(base_dir + '/books'):
            if len(Standard.objects.filter(standard=standard)) > 0:
                std = Standard.objects.get(standard=standard)
            else:
                std = Standard.objects.create(standard=standard)
            for subject in os.listdir(base_dir + '/books' + '/' + standard):
                if len(Subject.objects.filter(standard=standard, subject=subject)) > 0:
                    subj = Subject.objects.get(standard=std, subject=subject)
                else:
                    subj = Subject.objects.create(standard=std, subject=subject)
                for book in os.listdir(base_dir + '/books' + '/' + standard + '/' + subject):
                    if len(Source.objects.filter(standard = std, source_name=book)) > 0:
                        source = Source.objects.get(standard = std, source_name = book)
                    else:
                        source = Source.objects.create(standard = std, source_name = book)
                    for topics in os.listdir(
                            base_dir + '/books' + '/' + standard + '/' + subject + '/' + book + '/html'):
                        topic_id, topic_name = topics.split('_', 1)
                        if len(Topic.objects.filter(topic_id=topic_id, topic=topic_name, subject=subj)) > 0:
                            topic = Topic.objects.get(topic_id=topic_id, topic=topic_name, subject=subj)
                        else:
                            topic = Topic.objects.create(topic_id=topic_id, topic=topic_name, subject=subj)
                        for file in os.listdir(
                                base_dir + '/books' + '/' + standard + '/' + subject + '/' + book + '/html' + '/' + topics):
                            if '.json' in file:
                                # print(file)
                                with open(
                                        base_dir + '/books' + '/' + standard + '/' + subject + '/' + book + '/html' + '/' + topics + '/' + file,
                                        'r') as f:
                                    data = json.load(f)
                                    for jsonobject in data['data']:
                                        if len(InQuestion.objects.filter(topic=topic,  source = source, question_id = jsonobject['id'])) > 0:
                                            question = InQuestion.objects.get(topic=topic, source = source, question_id = jsonobject['id'])
                                        else:
                                            question = InQuestion.objects.create(topic=topic, source=source, question_id=jsonobject['id'])
                                        try:
                                            question.question_id = jsonobject['id']
                                        except:
                                            pass
                                        try:
                                            question.question_html = jsonobject['questionHtml']
                                            question.question_html = process_image_src_html(question.question_html, standard, subject, book, topics)
                                        except:
                                            pass
                                        try:
                                            question.solution_html = jsonobject['solutionHtml']
                                        except:
                                            pass
                                        try:
                                            question.is_publish = jsonobject['isPublish']
                                        except:
                                            pass
                                        try:
                                            question.is_active = jsonobject['isActive']
                                        except:
                                            pass
                                        try:
                                            question.tc_map_id = jsonobject['tcMapId']
                                        except:
                                            pass
                                        try:
                                            question.text_book_id = jsonobject['textbookId']
                                        except:
                                            pass
                                        try:
                                            question.chapter_id = jsonobject['chapterId']
                                        except:
                                            pass
                                        try:
                                            question.exercise_id = jsonobject['exerciseId']
                                        except:
                                            pass
                                        try:
                                            question.flow = jsonobject['flow']
                                        except:
                                            pass
                                        try:
                                            question.page_flow = jsonobject['pageFlow']
                                        except:
                                            pass
                                        try:
                                            question.set_no = jsonobject['setNo']
                                        except:
                                            pass
                                        try:
                                            question.page_no = jsonobject['pageNo']
                                        except:
                                            pass
                                        try:
                                            question.question_no = jsonobject['questionNo']
                                        except:
                                            pass
                                        try:
                                            question.exercise_flow = jsonobject['exerciseFlow']
                                        except:
                                            pass
                                        try:
                                            question.edition = jsonobject['edition']
                                        except:
                                            pass
                                        try:
                                            question.edition = jsonobject['edition']
                                        except:
                                            pass
                                        try:
                                            question.tc_map_is_active = jsonobject['tcMapIsActive']
                                        except:
                                            pass
                                        try:
                                            question.slo_id = jsonobject['sloId']
                                        except:
                                            pass
                                        try:
                                            question.slo_map_id = jsonobject['sloMapId']
                                        except:
                                            pass
                                        try:
                                            question.slo_mao_is_active = jsonobject['sloMapIsActive']
                                        except:
                                            pass
                                        try:
                                            question.exercise_name = jsonobject['exerciseName']
                                        except:
                                            pass
                                        question.save()
                    print(book + 'migration complete')
