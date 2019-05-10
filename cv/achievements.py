#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CrossBox():
    """
    CrossBox is a webapp I did for a friend who started a crossfit gym. It
    handles users, training sessions and reservations. I used Django for
    the API and admin panel and VueJs with a responsive design for the frontend
    layout that users use to reservate their training sessions.
    To see the app you can use this link:

    (spam) https://reservations.crossboxpalau.com/

    For more information contact me and I put you in contact with the trainer.
    """

    @property
    def frontend():
        """
        There is served with Django Templates and VueJs components. In next
        phase of this project I will completly uncouple this two parts.
        """
        pass

    @property
    def backend():
        """
        I used Django for the API and the admin panel.
        """
        pass

    @property
    def code():
        """
        I have it currently private in bitbucket, after some reviews I will
        put it public on GitHub.
        """
        pass

    @property
    def cac():
        """
        Becouse of I don't want to be afraid if the server dies or if I change
        to another cloud provider, all is defined with Ansible, I love
        Configuration As Code, all this project has its configuration by
        Ansible and I can trigger the playbook with my Jenkins. This Ansible
        repository is private too on my Bitbucket account and after some
        reviews I will put it public on Github.
        """
        pass

    @property
    def gcp():
        """
        For DNS I used Google Domains and for hosting a VM of Google Cloud
        Platform, where I played my ansible book to configure nginx, uwsgi,
        local postgres, etc.
        """
        pass
