#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Career():
    """ 7 years of Software Egineering experience.

    I started in REDK, hired by my university teacher. Then I moved to
    Calidae for 5 years and now I'm currently working in BMAT as part of the
    Data team managing what will be the most accurate and complete music
    metadata database in the world.
    """

    @property
    def redk():
        """
        ::

            overview = {
                'company': 'REDK Software Enginering',
                'role': 'Software Engineer',
                'frameworks': ['SugarCRM'],
                'duration': dateutils.relativedelta(years=1),
            }
        """
        return 'PHP'

    @property
    def calidae():
        """
        ::

            overview = {
                'company': 'Sistemes i Xarxes Informàtiques Calidae'
                'role': 'Software Engineer'
                'frameworks': ['Django', 'Tryton'],
                'devops_tools': ['AWS', 'Ansible', 'Terraform', 'Jenkins'],
                'culture': [
                    'agile', 'kanban', 'testing', 'self-organized teams',
                    'show&tells', 'paellas', 'free beer',
                ],
                'old_frameworks': ['Angular', 'Laravel'],
                'duration': dateutils.relativedelta(years=5),
            }
        """
        return 'Python'

    @property
    def bmat():
        """
        ::

            overview = {
                'company': 'BMAT Music Innovators',
                'role': 'Data Engineer',
                'tasks': [],
                'duration': dateutils.relativedelta(years=1),
            }
        """
        return 'Python'
