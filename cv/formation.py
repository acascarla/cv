#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Monlau():
    """
    Monlau is where I started my Higher Education IT focused. I studied in this
    school for 5 years doing 3 diferent courses, one Middle Level Vocational
    Training and two Advanced Vocational Trainings.
    """

    @property
    def middle_level_esi():
        """
        CF Grau Mig d'Informàtica::

            overview = {
                name: 'Explotació de Sistemes Informàtics',
                center: "Centre d'Estudis Monlau",
                duration: dateutils.relativedelta(years=2),
                contents: ['IT basics'],
            }
        """
        pass

    @property
    def advance_level_asix():
        """
        CF Grau Superior de Sistemes::

            overview = {
                name: 'Administració Sistemes Informàtics i Xarxes',
                center: "Centre d'Estudis Monlau",
                duration: dateutils.relativedelta(years=2),
                contents: ['SysAdmin knowledge', 'programming basics'],
            }
        """
        pass

    @property
    def advance_level_dam():
        """
        CF Grau Superior de Programació::

            overview = {
                name: "Desenvolupament d'Aplicacions Multiplataforma",
                center: "Centre d'Estudis Monlau",
                duration: dateutils.relativedelta(years=1),
                contents: [
                    'programming knowledge', 'OOP', 'relational databases'
                ],
            }
        """
        pass


class LaSalle():
    """
    After my 5th year in Monlau, La Salle just started a Multimedia Bachelor's
    degree of 3 years oriented to videogames. That would convalidate most
    of already coursed subjects, due to that, all the degree lasted just 2
    years instead of 3.
    """

    @property
    def multimedia_bachelor():
        """
        Batxelor Multimèdia::

            overview = {
                name: "Batxelor Multimèdia",
                center: "Open University La Salle",
                duration: dateutils.relativedelta(years=2),
                contents: [
                    'ux', 'ui', 'arduino', 'db', 'android', 'ios',
                    'game design', 'photography', 'video edition',
                    'programming an engine from zero', 'unity', '3d model',
                    '3d rigging', '3d animation', 'web projects',
                    'web videogames', 'phaser.js'
                ],
            }
        """
        pass
