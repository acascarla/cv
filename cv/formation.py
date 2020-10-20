#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Monlau():
    """5 years and 3 IT courses, one Middle and two Advanced Vocational Trainings."""  # noqa e501

    @property
    def middle_level_it():
        """CF Grau Mig d'Informàtica
        ::

            overview = {
                'name': 'System Administration',
                'center': "Centre d'Estudis Monlau",
                'duration': dateutils.relativedelta(years=2),
                'contents': ['IT basics'],
            }
        """
        pass

    @property
    def advance_level_sysadmin():
        """CF Grau Superior de Sistemes
        ::

            overview = {
                'name': 'Networks and Informatic Systems Administration',
                'center': "Centre d'Estudis Monlau",
                'duration': dateutils.relativedelta(years=2),
                'contents': ['System Administration', 'programming basics'],
            }
        """
        pass

    @property
    def advance_level_software():
        """CF Grau Superior de Programació
        ::

            overview = {
                'name': 'Development of Multiplatform Apps',
                'center': "Centre d'Estudis Monlau",
                'duration': dateutils.relativedelta(years=1),
                'contents': [
                    'Software Engineering', 'Relational Databases'
                ],
            }
        """
        pass


class LaSalle():
    """A Multimedia Bachelor degree of 3 years oriented to videogames."""

    @property
    def multimedia_bachelor():
        """Batxelor Multimèdia
        ::

            overview = {
                'name': 'Multimedia Bachelor',
                'center': 'Open University La Salle',
                'duration': dateutils.relativedelta(years=3),
                'contents': [
                    'DBs', 'Android', 'IOS', 'Web Videogames', 'phaser.js'
                    'Game Design', 'Video Edition', 'Web Projects',
                    'Programming an engine from scratch', 'c++', 'libsdl',
                    'Unity', '3d modeling', '3d rigging', '3d animation',
                ],
            }
        """
        pass
