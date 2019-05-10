#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Career():
    """
    In my "Monlau's life" I did some working practice hours but I really
    started to like "real-life programming" on my first job. When I was on
    University my Web Projects teacher hired me on his company, REDK, for
    working as PHP Developer with SugarCRM. After Bachelor, I started in
    Calidae, a completly diferent place with a very healthy philosophy and
    too much more close to home than REDK. I'm from Palau-solità i Plegamans
    and working in Caldes de Montbui and not spending like two hours every
    day is amazing.
    """

    @property
    def redk():
        """
        >>> {
        >>>     'company': 'REDK Software Enginering',
        >>>     'role': 'PHP Developer',
        >>>     'frameworks': ['SugarCRM'],
        >>>     'date_from': datetime.date(day=1, month=2, year=2014)
        >>>     'date_to': datetime.date(day=1, month=8, year=2014)
        >>> }
        """
        return 'PHP'

    @property
    def calidae():
        """
        >>> {
        >>>     company: 'Sistemes i Xarxes Informàtiques Calidae'
        >>>     role: 'Python Developer + DevOps and now Team Lead'
        >>>     frameworks: ['Django', 'Tryton'],
        >>>     devops_tools: ['AWS', 'Ansible', 'Terraform', 'Jenkins'],
        >>>     culture: [
        >>>         'agile', 'kanban', 'testing', 'self-organized teams',
        >>>         'show&tells', 'paellas', 'free beer',
        >>>     ],
        >>>     old_frameworks: ['Angular', 'Laravel'],
        >>>     date_from: datetime.date(day=1, month=11, year=2015),
        >>>     date_to: None,
        >>> }
        """
        return 'Python'
