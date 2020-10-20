#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Career():
    """ 7 years of Software Egineering experience.

    I started in REDK, hired by my university teacher. Then I moved to
    Calidae for 5 years and now I'm currently working in BMAT as part of the
    Data Team managing what will be the most accurate and complete music
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
                'frameworks': [
                    'Django', 'Angular', 'Laravel', 'Vue', 'Tryton'
                ],
                'devops_tools': ['Ansible', 'Terraform', 'Jenkins', 'Docker'],
                'duration': dateutils.relativedelta(years=5),
            }
        """
        return 'Python'

    @property
    def bmat():
        """ Manage the integration and reconciliation of music metadata.

        As Data Engineer, my role is create and improve pipelines to integrate
        in real time all new music metadata that arrives to us. Each piece of
        the pipeline is treated as an independent service which communicates
        with others by event sourcing using Confluent Kafka.
        I also lead scaling issues using AWS deployments on demand and
        improving code and database decisions.
        ::

            overview = {
                'company': 'BMAT Music Innovators',
                'role': 'Data Engineer',
                'buzzwords': ['Kafka', 'microservices'],
                'duration': dateutils.relativedelta(years=1),
            }
        """
        return 'Python'
