#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Career():
    """
    In my "Monlau's life" I did some working practice hours but I really
    started to like "real-life programming" on my first job. When I was in
    University my Web Projects teacher hired me on his company, REDK, to work
    as PHP Developer with SugarCRM. After completing my Bachelor’s degree,
    I started in Calidae, the place where I work now. When I arrived
    we were working with Laravel and Angular and a bit later we started to use
    Django and VueJS.
    """

    @property
    def redk():
        """
        ::

            overview = {
                'company': 'REDK Software Enginering',
                'role': 'PHP Developer',
                'frameworks': ['SugarCRM'],
                'date_from': datetime.date(day=8, month=1, year=2014)
                'date_to': datetime.date(day=31, month=11, year=2014)
            }
        """
        return 'PHP'

    @property
    def calidae():
        """
        ::

            overview = {
                company: 'Sistemes i Xarxes Informàtiques Calidae'
                role: 'Python Developer + DevOps advocate'
                frameworks: ['Django', 'Tryton'],
                devops_tools: ['AWS', 'Ansible', 'Terraform', 'Jenkins'],
                culture: [
                    'agile', 'kanban', 'testing', 'self-organized teams',
                    'show&tells', 'paellas', 'free beer',
                ],
                old_frameworks: ['Angular', 'Laravel'],
                date_from: datetime.date(day=1, month=9, year=2015),
                date_to: None,
            }
        """
        return 'Python'
