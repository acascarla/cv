#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CrossBox():
    """
    CrossBox is a webapp I did for a friend who started a CrossFit gym. It
    handles users, training sessions and reservations. I used Django for
    the API and admin panel and VueJs with a responsive design for the frontend
    layout that users use to reserve their training sessions.
    """

    @property
    def frontend():
        """
        It's served with Django Templates and VueJs components. In next
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
    def cac():
        """
        I love Configuration As Code, all this project has been configured by
        Ansible and also there is a Jenkins job to reconfigure or perform a
        deploy.
        """
        pass

    @property
    def gcp():
        """
        It's currently running on a VM of Google Cloud Platform and for DNS I'm
        using Google Domains.
        """
        pass
